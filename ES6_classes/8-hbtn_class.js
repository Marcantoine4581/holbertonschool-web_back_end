export default class HolbertonClass {
  constructor(size, location) {
    this._size = size; // number
    this._location = location; // string
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') {
      return this._location;
    }
    return this._size;
  }
}
