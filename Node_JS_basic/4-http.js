// curl localhost:1245 && echo ""
const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200);
  res.end('Hello Holberton School!');
});

app.listen(1245);
