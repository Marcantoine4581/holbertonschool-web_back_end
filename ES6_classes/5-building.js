export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !(this.evacuationWarningMessage)) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    if (typeof sqft !== 'number') {
      throw TypeError('sqft should be a number');
    }
    this._sqft = sqft;
  }

  // Setter & Getter sqft
  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw TypeError('sqft should be a number');
    }
    this._sqft = newSqft;
  }

  get sqft() {
    return this._sqft;
  }
}
