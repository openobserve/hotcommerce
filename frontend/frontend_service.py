from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
import requests
import os

app = FastAPI()

SHOP_SERVICE_URL = os.environ.get('SHOP_SERVICE_URL', "http://shop-service:8002")
templates = Jinja2Templates(directory="templates")

@app.get("/item/{item_id}")
def get_item(request: Request, item_id: int):
    try:
        response = requests.get(f"{SHOP_SERVICE_URL}/shop/item/{item_id}")
        item_data = response.json()
    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Error fetching item details")

    return templates.TemplateResponse("item.html", {"request": request, "item": item_data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
