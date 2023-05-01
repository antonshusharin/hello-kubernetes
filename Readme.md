# Hello Kubernetes

This is one of the practical tasks for the 2023 "Grid and Cloud Computing" course at Saint Petersburg state University.

## Description

This is a fairly simple hello world application. It consists of two parts: a frontend and a backend. The backend is replicated by Kubernetes and is not exposed to the internet. The frontend is exposed, it communicates with the backend using the service discovery facilities provided by Kubernetes.

## Prerequisits
To deploy the application, you will need the following:

- [Docker](https://www.docker.com)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

Note: the following instructions assume that Windows is your operating system. With one exception, they should also be suitable for other platforms supported by the tools above.

## Setup
Clone the repository:
`git clone https://github.com/antonshusharin/hello-kubernetes.git`
`cd hello-kubernetes`

Create and start a local Kubernetes cluster with Minikube:
`minikube start`

Configure your Docker client to communicate with the cluster's Docker daemon (command will be different for non-Windows platforms, see the output of `minikube docker-env` for the correct version):
`@FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env --shell cmd') DO @%i`

Build the Docker images for the frontend and backend:
`docker build -t hello_kubernetes/frontend frontend`
`docker build -t hello_kubernetes/backend backend`

Initialize the deployments and services. IMPORTANT: applying the files in a different order might lead to the environment variables required for the frontend to discover the backend not being set correctly!
`kubectl apply -f backend_deployment.yaml`
`kubectl apply -f backend_service.yaml`
`kubectl apply -f frontend_deployment.yaml`
`kubectl apply -f frontend_service.yaml`

## Testing
Use the following command to discover the url of the frontend service:
`minikube service --url hello-frontend`
Then make requests to the provided endpoint:
`curl http://127.0.0.1:36396`

If everything was set up correctly, you will see a greeting followed by the uid of the pod that served the request. By making multiple requests to the same endpoint you should see several different ids, proving that the backend is replicated correctly.