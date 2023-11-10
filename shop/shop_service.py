import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

PRODUCT_SERVICE_URL = os.environ.get(
    'PRODUCT_SERVICE_URL', "http://product-service:8000")


class ShopItem(BaseModel):
    id: int
    name: str
    description: str
    review: str
    rating: int
    in_stock: int
    warehouse_location: str


@app.get("/shop/item/{item_id}", response_model=ShopItem)
def get_shop_item(item_id: int):
    print("PRODUCT_SERVICE_URL: ", PRODUCT_SERVICE_URL)
    # Fetch product data from the product microservice
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}/product/{item_id}")
        product_data = response.json()

        # Enrich product data with shop-specific data
        product_data["in_stock"] = 10  # Sample in-stock quantity
        # Sample warehouse location
        product_data["warehouse_location"] = "A1-B2"
        return product_data

    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Error fetching product")

    return product_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
