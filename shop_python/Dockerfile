# shop_service.Dockerfile
FROM public.ecr.aws/docker/library/python:3.9.18-slim-bullseye

WORKDIR /app

COPY shop/shop_service.py .
COPY shop/requirements.txt .

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD ["uvicorn", "shop_service:app", "--host", "0.0.0.0", "--port", "8002"]
