# HOT commerce

HOT Commerce is a sample microservices application for demonstrating auto-instrumentation of microservices using OpenTelemetry operator.


frontend (go) -> shop (nodejs) -> product (java) -> review (python)


This application has been intentionally kept very simple. It has 4 microservices. Each microservice has a single endpoint. The frontend service calls the shop service which in turn calls the product service which in turn calls the review service.

## Prerequisites

1. An existing kubernetes cluster. 
1. OpenObserve-collector installed in the cluster.

## Deploy the application

```
kubectl create ns hotcommerce
kubectl apply -f deployment.yaml
```

port-forward the frontend service

```
kubectl port-forward svc/frontend 8001:80
```

now access the frontend service at http://localhost:8001/item/1 in your browser.

## Visualize traces

Open traces UI in OpenObserve. You should see traces for the requests made to the frontend service along with other dependent services.
