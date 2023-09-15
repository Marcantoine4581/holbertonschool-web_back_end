const express = require('express');

const app = express();
const PORT = 7865;

app.use(express.json());

app.get('/', (req, res) => {
  res.status(200);
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  const id = req.params.id;
  res.set('Content-Type', 'text/plain');
  res.status(200)
    .send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
  const object = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  }
  res.status(200).send(object);
});

app.post('/login', (req, res) => {
  const userName = req.body.userName;

  res.status(200)
    .send(`Welcome ${userName}`);
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
