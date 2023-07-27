export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand; // string
    this._motor = motor; // string
    this._color = color; // string
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const CarModel = this.constructor[Symbol.species];
    return new CarModel();
  }
}
