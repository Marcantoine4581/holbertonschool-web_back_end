const Utils = require('./utils')
const sendPaymentRequestToApi = require('./3-payment')
var expect = require('chai').expect
var sinon = require("sinon");

describe('sendPaymentRequestToApi', function () {
  it('stub the Utils.calculateNumber function', function () {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.returns(10);

    const spyConsole = sinon.spy(console, 'log');
    resultPrinted = sendPaymentRequestToApi(100, 20);

    expect(stub.alwaysCalledWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledWithExactly('The total is: 10')).to.be.true;

    stub.restore();
    spyConsole.restore();
  });
});
