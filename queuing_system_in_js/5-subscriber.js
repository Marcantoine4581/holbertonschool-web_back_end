import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.subscribe('holberton school channel');

redisClient.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
  }
  if (message === 'KILL_SERVER') {
    redisClient.unsubscribe(channel);
    redisClient.quit();
  }
});
