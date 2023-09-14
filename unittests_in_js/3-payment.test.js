const Utils = require('./utils')
const sendPaymentRequestToApi = require('./3-payment')
var expect = require('chai').expect
var sinon = require("sinon");

describe('sendPaymentRequestToApi', function () {
  it('Spy the Utils.calculateNumber function', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(10, 20);
    expect(spy.calledOnce).to.be.true;
  });
});
