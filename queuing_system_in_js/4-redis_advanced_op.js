import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

const key = 'HolbertonSchools';
const values = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const field in values) {
  if (values) {
    redisClient.hset(key, field, values[field], redis.print);
  }
}

redisClient.hgetall(key, (err, value) => {
  console.log(value);
});
