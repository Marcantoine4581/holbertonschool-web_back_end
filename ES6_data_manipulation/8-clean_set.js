export default function cleanSet(set, startString) {
  if (!startString || !startString.length) {
    return '';
  }
  let result = '';
  for (const element of set) {
    if (element && element.startsWith(startString)) {
      if (result.length === 0) {
        result += element.replace(startString, '');
      } else {
        result += element.replace(startString, '-');
      }
    }
  }
  return result;
}
