const sendPaymentRequestToApi = require('./5-payment')
var expect = require('chai').expect
var sinon = require("sinon");

describe('sendPaymentRequestToApi', function () {
  let spyConsole;
  beforeEach(() => {
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyConsole.restore();
  });
  it('is logging the string and only called once', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });
  it('is logging the string and only called once', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spyConsole.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });
});
