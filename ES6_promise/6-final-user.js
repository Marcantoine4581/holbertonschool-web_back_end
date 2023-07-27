import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName),
    uploadPhoto(fileName)];

  return Promise.allSettled(promises)
    .then((results) => {
      const array = [];
      results.forEach((result) => {
        if (result.status === 'fulfilled') {
          array.push(result);
        } else {
          array.push({
            status: result.status,
            value: `Error: ${result.reason.message}`,
          });
        }
      });
      return array;
    });
}
