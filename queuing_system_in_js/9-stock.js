import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Database
const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 0 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function renameKeys(list) {
  const newlist = list.map((obj) => ({
    itemId: obj.Id,
    itemName: obj.name,
    price: obj.price,
    initialAvailableQuantity: obj.stock,
  }));
  return newlist;
}

const list_products = renameKeys(listProducts);

// Express Server
const app = express();
const PORT = 1245;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

//  Redis server
const redisClient = redis.createClient();
const asyncGet = promisify(redisClient.get).bind(redisClient);

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Utils functions
function getItemById(id) {
  return list_products.filter((item) => item.itemId === id)[0];
}

function reserveStockById(itemId, stock) {
  redisClient.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await asyncGet(`item.${itemId}`);
  return stock;
}

// Routes
app.get('/list_products', (req, res) => {
  res.status(200).json(list_products);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = Number(req.params.itemId);
  // Check if an item is found.
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: 'Product not found' });
  }
  res.status(200).json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  // Check if an item is found.
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  let current_stock = await getCurrentReservedStockById(itemId);
  if (current_stock === null) {
    current_stock = item.initialAvailableQuantity;
  }
  if (current_stock === 0) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }
  reserveStockById(itemId, current_stock);
  res.status(200).json({ status: 'Reservation confirmed', itemId });
});
