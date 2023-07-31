export default function updateUniqueItems(map) {
  if (typeof (map) !== 'object') {
    throw Error('Cannot process');
  }
  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
  return map;
}
