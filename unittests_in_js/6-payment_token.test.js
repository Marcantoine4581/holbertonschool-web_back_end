const getPaymentRequestToApi = require('./6-payment_token')
var expect = require('chai').expect
var sinon = require("sinon");

describe('getPaymentRequestToApi', function () {
  it('returns the message if argument is true', function (done) {
    getPaymentRequestToApi(true)
      .then((response) => {
        expect(response).to.include({data: 'Successful response from the API' })
        done();
    });
  });
});
