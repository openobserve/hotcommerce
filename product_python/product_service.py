import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os

app = FastAPI()

REVIEW_SERVICE_URL = os.environ.get(
    'REVIEW_SERVICE_URL', "http://review-service:8001")


@app.get("/product/{product_id}")
def get_product(product_id: int):
    print("REVIEW_SERVICE_URL: ", REVIEW_SERVICE_URL)
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

    except requests.RequestException as exc:
        raise HTTPException(
            status_code=500, detail="Error fetching review") from exc

    return sample_product


@app.get("/")
def base():
    content = {"hello": "from product"}
    return JSONResponse(content=content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
