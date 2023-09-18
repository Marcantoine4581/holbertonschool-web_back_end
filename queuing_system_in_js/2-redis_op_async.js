import redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();
const asyncGet = promisify(redisClient.get).bind(redisClient);

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const value = await asyncGet(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
