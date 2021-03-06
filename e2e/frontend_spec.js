module.exports = {
  'Testing FrontEnd' : function (browser) {
    browser
      .url('http://localhost:3000/')
      .waitForElementVisible('body', 1000)
      .pause(1000)
      .assert.title('Plan.it')
      .waitForElementVisible('.ng-isolate-scope', 1000)
      .waitForElementVisible('#map-btn-container', 1000)
      .waitForElementVisible('#Generate', 1000)
      .end();
  }
};
