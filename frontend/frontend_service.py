from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import requests
import os

app = FastAPI()

SHOP_SERVICE_URL = os.environ.get('SHOP_SERVICE_URL', "http://localhost:8081")
templates = Jinja2Templates(directory="templates")


@app.get("/item/{item_id}")
def get_item(request: Request, item_id: int):
    print("SHOP_SERVICE_URL: ", SHOP_SERVICE_URL)
    try:
        url = f"{SHOP_SERVICE_URL}/shop/item/{item_id}"
        response = requests.get(url)
        item_data = response.json()
    except requests.RequestException as exc:
        print(f"Error fetching item details from URL: {url}")
        raise HTTPException(
            status_code=500, detail="Error fetching item details") from exc

    return templates.TemplateResponse("item.html", {"request": request, "item": item_data})


@app.get("/hello")
def hello(request: Request):
    content = {"hello": "from another world"}
    return JSONResponse(content=content)


@app.get("/")
def base(request: Request):
    content = {"hello": "world"}
    return JSONResponse(content=content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
