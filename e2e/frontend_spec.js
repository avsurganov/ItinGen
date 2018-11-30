module.exports = {
  'Testing FrontEnd' : function (browser) {
    browser
      .url('http://localhost:3000/')
      .waitForElementVisible('body', 1000)
      .pause(1000)
      .assert.title('ItinGen')
    .pause(1000)
      .end();
  }
};
