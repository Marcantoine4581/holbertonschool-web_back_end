const calculateNumber = require('./0-calcul');
var assert = require('assert');

describe('calculateNumber', function () {
  it('should add two number', function () {
    assert.equal(calculateNumber(10, 15), 25);
  });  
  it('should return a round number', function () {
    assert.equal(calculateNumber(2.5, 5.1), 8);
  });
  it('should add 2 negative numbers', function () {
    assert.equal(calculateNumber(-2.5, -5.1), -7);
  });
});