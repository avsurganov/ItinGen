var express = require('express')
var app = express();
var dotenv = require('dotenv');
dotenv.load();
var morgan = require('morgan');
var mongoose = require('mongoose');
mongoose.Promise = require('bluebird').Promise
var User = require('./app/models/user');
var bodyParser = require('body-parser');
var path = require('path');
var passport = require('passport');
var social = require('./app/passport/passport')(app, passport);
var appRoutes = require('./app/routes/api');
var cors = require('cors');
port = process.env.PORT || 5000;
console.log(port)

app.use(cors());
app.use(morgan('dev'));
app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type, Authorization');
    next();
});
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : true}));
app.use(express.static(__dirname + './public'));
app.use('/api', appRoutes);

mongoose.connect('mongodb://administrator:administrator60@ds125684.mlab.com:25684/itingen', (err) => {
	if (err){
		console.log("Not connected to database" + err);
	}
	else {
		console.log("Successfully connected to database");
	}
});

app.get('*', (req, res) => {
	res.sendFile(path.join(__dirname + './public/index.html'));
});

app.listen(port, () => {
	console.log('Running the server');
});
