export default function getStudentsByLocation(arrayOfObjects, city) {
  return arrayOfObjects.filter((obj) => obj.location === city);
}
