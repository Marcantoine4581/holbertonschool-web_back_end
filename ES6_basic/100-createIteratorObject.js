export default function createIteratorObject(report) {
  let names = [];
  for (const value of Object.values(report.allEmployees)) {
    names = [...names, ...value];
  }
  return names;
}
