const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8').split('\n');
    let students = data.filter((item) => item);
    students = students.map((item) => item.split(','));
    const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
    console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);

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
      console.log(
        `Number of students in ${key}: ${fields[key].length}. \
        List: ${fields[key].join(', ')}`,
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
