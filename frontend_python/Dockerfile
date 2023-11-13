# frontend_service.Dockerfile
FROM public.ecr.aws/docker/library/python:3.9.18-slim-bullseye

WORKDIR /app

COPY frontend/frontend_service.py .
COPY frontend/templates templates/
COPY frontend/requirements.txt .

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD ["uvicorn", "frontend_service:app", "--host", "0.0.0.0", "--port", "8001"]

