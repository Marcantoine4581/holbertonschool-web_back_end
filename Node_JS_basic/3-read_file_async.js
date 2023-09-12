const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
      } else {
        const response = [];
        let message = '';

        const dataList = data.split('\n');
        let students = dataList.filter((item) => item);
        students = students.map((item) => item.split(','));

        const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
        message = `Number of students: ${NUMBER_OF_STUDENTS}`;
        console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);
        response.push(message);

        const fields = {};
        for (const i in students) {
          if (i !== 0) {
            if (!fields[students[i][3]]) {
              fields[students[i][3]] = [];
            }
            fields[students[i][3]].push(students[i][0]);
          }
        }
        delete fields.field;

        for (const key of Object.keys(fields)) {
          message = `Number of students in ${key}: ${fields[key].length}. List: ${fields[
            key
          ].join(', ')}`;
          console.log(message);
          response.push(message);
        }

        resolve(response);
      }
    });
  });
}

module.exports = countStudents;
