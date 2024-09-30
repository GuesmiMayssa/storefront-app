# Storefront App

A storefront application for electronics built using Flask and deployed on Kubernetes.

## Features
- Browse a variety of electronic products.
- View product details and images.
- Add items to a shopping cart.
- Responsive web design.

## Technologies Used
- **Frontend**: HTML, CSS.
- **Backend**: Flask.
- **Containerization**: Docker.
- **Orchestration**: Kubernetes.

## Setup Instructions

### Prerequisites
- Docker installed.
- Minikube or a similar Kubernetes setup running.
- GitHub account.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/storefront-app.git
   cd storefront-app
   
2. Build the Docker image:
  docker build -t storefront-app .

4. Deploy to Kubernetes
   kubectl apply -f deployment.yaml -n electronics-store-namespace
   kubectl apply -f service.yaml -n electronics-store-namespace
   
#### Horizontal Pod Autoscaler (HPA)
The Horizontal Pod Autoscaler (HPA) is configured to automatically adjust the number of pods in your deployment based on observed CPU utilization.

Applying HPA
If you need to apply the HPA configuration, you can do so with the following steps:
  kubectl apply -f hpa.yaml -n electronics-store-namespace
Testing HPA
To test the functionality of the HPA:

1. Check HPA Status:
  kubectl get hpa -n storefront-namespace
2. Generate Load: You can simulate load on your application to trigger scaling. A simple way to do this is by using tools like Apache Benchmark (ab) or hey:
  ab -n 1000 -c 10 http://<minikube-ip>:<NodePort>/
3. Monitor Pods: After generating load, monitor the number of pods:
  kubectl get pods -n storefront-namespace
4. Check Logs: You can check the logs to see the scaling events:
   kubectl logs -l app=storefront-app -n storefront-namespace
 


   
