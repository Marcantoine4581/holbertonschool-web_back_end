export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Setter & Getter code
  set code(newCode) {
    this.code = newCode;
  }

  get code() {
    return this._code;
  }

  // Setter & Getter name
  set name(newName) {
    this.name = newName;
  }

  get name() {
    return this._name;
  }

  // Method displayFullCurrency
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
