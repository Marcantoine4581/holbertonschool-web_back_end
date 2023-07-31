export default function getListStudentIds(arrayOfObjects) {
  if (typeof arrayOfObjects !== 'object') {
    return [];
  }
  return arrayOfObjects.map((value) => value.id);
}
