const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
      } else {
        const studentsList = data
          .split('\n')
          .filter((item) => item)
          .slice(1)
          .map((item) => item.split(','));

        const fields = {};
        for (let i = 0; i < studentsList.length; i += 1) {
          if (!fields[studentsList[i][3]]) fields[studentsList[i][3]] = [];

          fields[studentsList[i][3]].push(studentsList[i][0]);
        }
        resolve(fields);
      }
    });
  });
}

module.exports = readDatabase;

// readDatabase('database.csv')
//     .then((data) => {
//         console.log(data);
//         console.log("Done!");
//     })
//         .catch((error) => {
//         console.log(error);
//     });
