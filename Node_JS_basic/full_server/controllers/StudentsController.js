const readDatabase = require('../utils');

const database = '../database.csv';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(database)
      .then((contents) => {
        const firstLine = 'This is the list of our students\n';
        let message = '';
        const display = [];
        for (const key of Object.keys(contents)) {
          const NB_STUDENTS = contents[key].length;
          const LIST_OF_FIRSTNAMES = contents[key].join(', ');
          message = `Number of students in ${key}: ${
            NB_STUDENTS}. List: ${LIST_OF_FIRSTNAMES}`;

          display.push(message);
        }
        response.set('Content-Type', 'text/plain');
        response.status(200)
          .send(`${firstLine}${display.join('\n')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
    }
    readDatabase(database)
      .then((contents) => {
        const LIST_OF_FIRSTNAMES = contents[major].join(', ');
        const message = `List: ${LIST_OF_FIRSTNAMES}`;

        response.set('Content-Type', 'text/plain');
        response.status(200)
          .send(message);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
