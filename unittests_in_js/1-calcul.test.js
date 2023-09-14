const calculateNumber = require('./1-calcul');
var assert = require('assert');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should add two positive round numbers', function () {
      assert.equal(calculateNumber('SUM', 10.15, 15.11), 25);
    });
  });
  describe('SUM', function () {
    it('should add two negative round numbers', function () {
      assert.equal(calculateNumber('SUM', -5, -2), -7);
    });
  });
  describe('SUBTRACT', function () {
    it('should substract two round numbers', function () {
      assert.equal(calculateNumber('SUBTRACT', 20.5, 5.1), 16);
    });
  });
  describe('DIVIDE', function () {
    it('should divide two round numbers', function () {
      assert.equal(calculateNumber('DIVIDE', 15, 3), 5);
    });
  });
  describe('DIVIDE', function () {
    it('should return the string Error if divided by 0', function () {
      assert.equal(calculateNumber('DIVIDE', 10.15, 0), 'Error');
    });
  });
});
