import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

REVIEW_SERVICE_URL = os.environ.get('REVIEW_SERVICE_URL', "http://review-service:8001")

class Product(BaseModel):
    id: int
    name: str
    description: str
    review: str
    rating: int

@app.get("/product/{product_id}", response_model=Product)
def get_product(product_id: int):
    sample_product = {
        "id": product_id,
        "name": "Sample Product",
        "description": "This is a sample product."
    }

    # Fetch review from the review microservice
    try:
        response = requests.get(f"{REVIEW_SERVICE_URL}/review/{product_id}")
        review_data = response.json()

        # Update product with review information
        sample_product["review"] = review_data["review"]
        sample_product["rating"] = review_data["rating"]

    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Error fetching review")

    return sample_product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)

