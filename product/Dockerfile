# product_service.Dockerfile
# FROM python:3.9-slim
FROM public.ecr.aws/docker/library/python:3.9.18-slim-bullseye

WORKDIR /app

COPY product/product_service.py .
COPY product/requirements.txt .

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD ["uvicorn", "product_service:app", "--host", "0.0.0.0", "--port", "8000"]

