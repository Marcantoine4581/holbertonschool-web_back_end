// curl localhost:1245 && echo ""
const http = require('http');

port = 1245

const app = http.createServer((req, res) => {
  res.end('Hello Holberton School!');
});

app.listen(port);

module.exports = app;
