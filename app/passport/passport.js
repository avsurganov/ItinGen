var FacebookStrategy = require('passport-facebook').Strategy; // Import Passport-Facebook Package
var User = require('../models/user'); // Import User Model
var session = require('express-session'); // Import Express Session Package
var jwt = require('jsonwebtoken'); // Import JWT Package
var secret = 'itingen'; // Create custom secret to use with JWT

module.exports = function(app, passport) {
    // Start Passport Configuration Settings
    app.use(passport.initialize());
    app.use(passport.session());
    app.use(session({ secret: 'itingen', resave: false, saveUninitialized: true, cookie: { secure: false } }));
    // End Passport Configuration Settings

    // Serialize users once logged in   
    passport.serializeUser(function(user, done) {
        token = jwt.sign({ email: user.email}, secret, { expiresIn: '24h' }); // Logged in: Give user token
        done(null, user.id); // Return user object
    });

    // Deserialize Users once logged out    
    passport.deserializeUser(function(id, done) {
        User.findById(id, function(err, user) {
            done(err, user); // Complete deserializeUser and return done
        });
    });

    // Facebook Strategy    
    passport.use(new FacebookStrategy({
            clientID: '357949704772980', // Replace with your Facebook Developer App client ID
            clientSecret: '63b37d927bd048fc98b9209d1f078a72', // Replace with your Facebook Developer client secret
            callbackURL: "https://itingen2.herokuapp.com/auth/facebook/callback", // Replace with your Facebook Developer App callback URL
            profileFields: ['id', 'displayName', 'email']
        },
        function(accessToken, refreshToken, profile, done) {
            console.log(profile._json.email);
            User.findOne({'email' : profile._json.email}).select('email').exec(function(err, user) {
                if(err){
                    done(err);
                    return;
                } else {
                    if (user && user != null){
                        //Found user
                        done(null, user);
                    } else {
                        //No user, create a new 
                        console.log("Creating new user: " + profile._json.email);
                        var newUser = new User();
                        newUser.email = profile._json.email;
                        newUser.save();
                        done(null, user);
                        // return;
                    }
                }
            });
        }
    ));

    // Facebook Routes
    app.get('/auth/facebook/callback', passport.authenticate('facebook', { failureRedirect: '/login' }), function(req, res) {
        res.redirect('/facebook/' + token); // Redirect user with newly assigned token
    });
    app.get('/auth/facebook', passport.authenticate('facebook', { scope: 'email' }));

    return passport; // Return Passport Object
};