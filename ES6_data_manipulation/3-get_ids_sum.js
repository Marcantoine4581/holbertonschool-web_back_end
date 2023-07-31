export default function getStudentIdsSum(arrayOfObjects) {
  return arrayOfObjects.reduce((acc, cur) => acc + cur.id, 0);
}
