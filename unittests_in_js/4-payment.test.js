const Utils = require('./utils')
const sendPaymentRequestToApi = require('./4-payment')
var expect = require('chai').expect
var sinon = require("sinon");

describe('sendPaymentRequestToApi', function () {
  it('stub the Utils.calculateNumber function', function () {
    const stubUtils = sinon.stub(Utils, 'calculateNumber');
    stubUtils.returns(10);

    const spyConsole = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);

    expect(stubUtils.alwaysCalledWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledWithExactly('The total is: 10')).to.be.true;

    stubUtils.restore();
    spyConsole.restore();
  });
});
