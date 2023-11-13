const express = require('express');
const axios = require('axios');
const app = express();

const PRODUCT_SERVICE_URL = process.env.PRODUCT_SERVICE_URL || "http://localhost:8003";

app.get('/shop/item/:item_id', async (req, res) => {
  console.log("PRODUCT_SERVICE_URL: ", PRODUCT_SERVICE_URL);
  try {
    const response = await axios.get(`${PRODUCT_SERVICE_URL}/product/${req.params.item_id}`);
    const product_data = response.data;

    // Enrich product data with shop-specific data
    product_data["in_stock"] = 10;  // Sample in-stock quantity
    // Sample warehouse location
    product_data["warehouse_location"] = "A1-B2";

    res.json(product_data);
  } catch (error) {
    res.status(500).send('Error fetching product');
  }
});

app.get('/', (req, res) => {
  const content = { "hello": "from shop" };
  res.json(content);
});

const PORT = process.env.PORT || 8002;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

