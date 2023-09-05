# review_service.Dockerfile
FROM public.ecr.aws/docker/library/python:3.9.18-slim-bullseye

WORKDIR /app

COPY review/review_service.py .
COPY review/requirements.txt .

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD ["uvicorn", "review_service:app", "--host", "0.0.0.0", "--port", "8001"]
