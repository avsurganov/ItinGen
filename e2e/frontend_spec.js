module.exports = {
  'Testing FrontEnd' : function (browser) {
    browser
      .url('http://localhost:3000/')
      .waitForElementVisible('body', 1000)
      .pause(1000)
      .assert.title('ItinGen')
      .waitForElementVisible('.ng-isolate-scope', 1000)
      .waitForElementVisible('#map-btn-container', 1000)
      .waitForElementVisible('#like', 1000)
      .waitForElementVisible('#dislike', 1000)
      .end();
  }
};
