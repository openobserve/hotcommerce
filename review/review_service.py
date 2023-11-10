from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Review(BaseModel):
    product_id: int
    review: str
    rating: int  # From 1 to 5

@app.get("/review/{product_id}", response_model=Review)
def get_review(product_id: int):
    # For simplicity, we're returning the same review for any product ID.
    return {
        "product_id": product_id,
        "review": "This is a great product!",
        "rating": 5
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)

