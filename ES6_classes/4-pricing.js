import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount === 'number') this._amount = amount;
    if (currency instanceof Currency) this._currency = currency;
  }

  // Setter & Getter amount
  set amount(newAmount) {
    if (typeof amount === 'number') this.amount = newAmount;
  }

  get amount() {
    return this._amount;
  }

  // Setter & Getter currency
  set currency(newCurrency) {
    if (newCurrency instanceof Currency) this.currency = newCurrency;
  }

  get currency() {
    return this._currency;
  }

  // Method displayFullPrice return amount currency_name (currency_code)
  displayFullPrice() {
    return `${this._amount} ${this.currency.displayFullCurrency()}`;
  }

  // static method convertPrice
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
