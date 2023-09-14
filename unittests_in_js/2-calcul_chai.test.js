const calculateNumber = require('./1-calcul');
var expect = require('chai').expect

describe('calculateNumber test using Chai', function () {
  describe('SUM', function () {
    it('should add two positive round numbers', function () {
      expect(calculateNumber('SUM', 10.15, 15.11)).to.equal(25);
      expect(calculateNumber('SUM', 10.15, 15.11)).to.be.an('number');
    });
  });
  describe('SUM', function () {
    it('should add two negative round numbers', function () {
      expect(calculateNumber('SUM', -10.1, -5.11)).to.equal(-15);
      expect(calculateNumber('SUM', 10.15, 15.11)).to.be.an('number');
    });
  });
  describe('SUBTRACT', function () {
    it('should substract two round numbers', function () {
      expect(calculateNumber('SUBTRACT', 10.15, 15.11)).to.equal(-5);
      expect(calculateNumber('SUM', 10.15, 15.11)).to.be.an('number');
    });
  });
  describe('DIVIDE', function () {
    it('should divide two round numbers', function () {
      expect(calculateNumber('DIVIDE', 15.1, 3.2)).to.equal(5);
      expect(calculateNumber('SUM', 10.15, 15.11)).to.be.an('number');
    });
  });
  describe('DIVIDE', function () {
    it('should return the string Error if divided by 0', function () {
      expect(calculateNumber('DIVIDE', 10.15, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 10.15, 0)).to.be.a('String');
    });
  });
});
