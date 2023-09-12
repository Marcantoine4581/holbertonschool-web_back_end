const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;
const database = process.argv[2];

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(200);
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  countStudents(database)
    .then((contents) => {
      res.set('Content-Type', 'text/plain');
      res.status(200);
      res.send(`This is the list of our students\n${contents.join('\n')}`);
    })
    .catch((error) => {
      res.status(404).send(error.message);
    });
});

app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
});

module.exports = app;
