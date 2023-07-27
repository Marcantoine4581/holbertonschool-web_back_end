import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqlt, floors) {
    super(sqlt);
    if (typeof floors !== 'number') {
      throw TypeError('floors should be a number');
    }
    this._floors = floors;
  }

  // Setter & Getter floors
  set floors(newFloors) {
    if (typeof newFloors !== 'number') {
      throw TypeError('floors should be a number');
    }
    this._floors = newFloors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
