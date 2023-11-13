# FROM node:20 AS build-env
FROM public.ecr.aws/docker/library/node:20.0 as build-env
COPY . /app
WORKDIR /app

RUN npm ci --omit=dev

FROM gcr.io/distroless/nodejs20-debian11
COPY --from=build-env /app /app
WORKDIR /app
CMD ["app.js"]

