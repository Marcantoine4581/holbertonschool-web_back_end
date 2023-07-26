import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const array = [19, 20, 34];

  return array.map((num) => new ClassRoom(num));
}
