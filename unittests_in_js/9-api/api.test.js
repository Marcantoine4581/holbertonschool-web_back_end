const { expect } = require('chai');
const request = require('request');

describe('test the payement system API', function () {
  describe('GET /', function () {
    const url = 'http://localhost:7865/'
    it('test status code 200', function (done) {
      request(url, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(200);
        done()
      });
    });
    it('test the correct message', function (done) {
        request(url, function (error, response, body) {
          if (error) {
            done(error)
          }
          expect(body).to.equal('Welcome to the payment system');
          expect(body).to.be.a('string')
          done()
        });
      });
  });

  describe('GET /cart/:id', function () {
    const url = 'http://localhost:7865/cart/10'
    it('test status code 200', function (done) {
      request(url, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(200);
        done()
      });
    });
    it('test the correct message', function (done) {
        request(url, function (error, response, body) {
          if (error) {
            done(error)
          }
          expect(body).to.equal('Payment methods for cart 10');
          expect(body).to.be.a('string')
          done()
        });
      });
    it('respond with 404 statusCode', (done) => {
      request('http://localhost:7865/cart/string', function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});