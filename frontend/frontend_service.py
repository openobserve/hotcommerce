from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI()

SHOP_SERVICE_URL = os.environ.get('SHOP_SERVICE_URL', "http://localhost:8002")


@app.get("/item/{item_id}")
def get_item(item_id: int):
    print("SHOP_SERVICE_URL: ", SHOP_SERVICE_URL)
    try:
        url = f"{SHOP_SERVICE_URL}/shop/item/{item_id}"
        response = requests.get(url)
        item_data = response.json()
    except requests.RequestException as exc:
        print(f"Error fetching item details from URL: {url}")
        raise HTTPException(
            status_code=500, detail="Error fetching item details") from exc

    return item_data


@app.get("/")
def base():
    content = {"hello": "from frontend"}
    return JSONResponse(content=content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
