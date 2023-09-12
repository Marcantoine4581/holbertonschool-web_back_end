// curl localhost:1245 && echo ""
const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;
const database = process.argv[2];

const app = http.createServer((req, res) => {
  switch (req.url) {
    case '/':
      res.setHeader('Content-Type', 'text/plain');
      res.writeHead(200);
      res.end('Hello Holberton School!');
      break;
    case '/students':
      res.setHeader('Content-Type', 'text/plain');
      res.writeHead(200);
      res.write('This is the list of our students\n');
      countStudents(database)
        .then((contents) => {
          res.end(contents.join('\n'));
        })
        .catch((error) => {
          res.end(error.message);
        });
      break;
    default:
      res.writeHead(404);
      res.end('Resource not found');
  }
});

app.listen(port, () => {
  // console.log(`Server running on port ${port}`);
});

module.exports = app;
