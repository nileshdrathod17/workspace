# Python DevOps Demo

Python Flask frontend and backend with Docker, Docker Compose,
Helm, Kubernetes, and GitHub Actions.

## Requirements
- Docker
- Minikube or Docker Desktop Kubernetes
- kubectl
- Helm 3

## Run locally

    docker compose up --build

Frontend: http://localhost:8080
Backend: http://localhost:5000

Stop:

    docker compose down

## Deploy to Minikube

    minikube start
    docker build -t devops-frontend:latest ./frontend
    docker build -t devops-backend:latest ./backend
    minikube image load devops-frontend:latest
    minikube image load devops-backend:latest

    helm lint ./helm/devops-app
    helm template devops-demo ./helm/devops-app
    helm install devops-demo ./helm/devops-app
    minikube service devops-demo-frontend

## Upgrade and uninstall

    helm upgrade devops-demo ./helm/devops-app
    helm uninstall devops-demo

## CI

Push to main or master. GitHub Actions validates Python,
builds both Docker images, and validates the Helm chart.

The workflow does not publish images or deploy to Kubernetes.
