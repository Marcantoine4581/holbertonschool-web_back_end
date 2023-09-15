const { expect } = require('chai');
const request = require('request');

describe('test the payement system API', function () {
  const baseUrl = 'http://localhost:7865';

  describe('GET /', function () {
    it('test status code 200', function (done) {
      request(baseUrl, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(200);
        done()
      });
    });
    it('test the correct message', function (done) {
        request.get(baseUrl, function (error, response, body) {
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
    it('test status code 200', function (done) {
      request(`${baseUrl}/cart/10`, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(200);
        done()
      });
    });
    it('test the correct message', function (done) {
        request(`${baseUrl}/cart/10`, function (error, response, body) {
          if (error) {
            done(error)
          }
          expect(body).to.equal('Payment methods for cart 10');
          expect(body).to.be.a('string')
          done()
        });
      });
    it('respond with 404 statusCode', (done) => {
      request(`${baseUrl}/cart/string`, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('POST /login', function () {
    const userName = 'Marc';
    const options = {
      url: `${baseUrl}/login`,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ userName }),
    };
    it('test status code 200', function (done) {
      request.post(options, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(response.statusCode).to.equal(200);
        done()
      });
    });
    it('test the correct message', function (done) {
      request.post(options, function (error, response, body) {
        if (error) {
          done(error)
        }
        expect(body).to.equal(`Welcome ${userName}`);
        expect(body).to.be.a('string')
        done()
      });
    });
  });

  describe(`GET /available_payments`, () => {
    it('test status code 200 and the correct message ', (done) => {
      const expectedResponse = {
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      };
  
      request.get(`${baseUrl}/available_payments`, (err, response, body) => {
        if (err) {
          done(err);
        }
  
        expect(response.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.eql(expectedResponse);
        done();
      });
    });
  });

});