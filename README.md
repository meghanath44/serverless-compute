## Serverless Computing Platform using Docker & NGINX:

---
## Introduction

This project presents a **lightweight, self-hosted serverless compute platform** that enables rapid function deployment and execution using a minimal tech stack—**Docker**, **NGINX**, **Python**, and **Kafka**. Unlike cloud-native FaaS platforms (e.g., AWS Lambda, Google Cloud Run), our platform emphasizes **speed, simplicity, and developer control** by eliminating heavy orchestration layers like Kubernetes or Firecracker.

The core idea is to reduce cold-start latency and deployment overhead by using pre-warmed containers and a direct request-routing mechanism. It's built to serve small, time-sensitive applications in edge or local environments.

---

## Why This Project?

While major serverless platforms are optimized for scalability and resource efficiency, they often compromise on:

* **Cold-start latency**
* **Deployment complexity**
* **Developer autonomy**

This project aims to:

* **Minimize latency** in function deployment and execution
* **Simplify** serverless infrastructure with self-hosting support
* **Provide a fast, responsive** alternative for small- to medium-scale use cases

---

## Features

* 🔹 Stateless, containerized function execution
* 🔹 Automated Docker container creation and NGINX route generation
* 🔹 Kafka-based asynchronous processing for deployment tasks
* 🔹 Lightweight and portable single-node deployment
* 🔹 HTTPS-enabled service URLs with custom subdomains
* 🔹 Developer-friendly UI for function creation and monitoring

---

## How to Use

### Requirements

* Docker
* Python 3.x
* NGINX
* Apache Kafka
* Node.js (for backend)
* React.js (for frontend)
* A Linux-based environment (tested on Ubuntu)

### 📦 Setup Instructions

1. **Clone the repository:**

   ```bash
   gh repo clone meghanath44/serverless-compute
   cd <your-project-directory>
   ```

2. **Start Kafka and Zookeeper** (or use Docker Compose):

   ```bash
   docker-compose up -d zookeeper kafka
   ```

3. **Build and run the backend & frontend apps:**

   * Backend:

     ```bash
     cd backend
     npm install
     npm start
     ```
   * Frontend:

     ```bash
     cd frontend
     npm install
     npm run build
     ```

4. **Start the Python services:**

   * Kafka consumer for Docker deployment
   * Kafka consumer for NGINX config generation
   * (Each script should be run in its own terminal or set up with systemd/pm2)

5. **Push Docker image to registry:**
   Make sure your function image is available at:
   `registry.csci-b516.me`

6. **Use the UI to deploy a function:**

   * Provide function name, Docker image URL, container port, and select region (currently only Indiana).
   * On successful deployment, you'll receive a service URL like:

     ```
     https://<your-service>.csci-b516.me
     ```

---

## ⚙️ How It Works

1. **User submits a function request** via a React + Node.js frontend.
2. The backend publishes this request to a Kafka topic.
3. Two Python consumers listen for:

   * **NGINX Config Requests**: Generates a route for the service.
   * **Docker Deployment Requests**: Pulls the image and starts a container.
4. Once complete:

   * NGINX is reloaded to apply the new route.
   * User is notified with a unique HTTPS-accessible URL.

Each function is fully isolated in a container, and public access is only available via the configured domain.

---

## Results

* Average cold start time: Under 1 second
* Secure subdomain-based access (via HTTPS)
* Successfully deployed multiple services concurrently (with noted limitations under high load)

---

## ⚠Limitations

* No support for CPU/RAM limits per function
* No autoscaling of containers
* No persistent storage for function data
* Limited to a single-node deployment for now

---

## Future Improvements

* Multi-node deployment with centralized load balancing
* Autoscaling via event triggers or usage metrics
* Persistent volumes and stateful containers
* Enhanced user metrics and logs for deployed services

---

## Contributors

* **Sashank Talakola** – NGINX, Docker Automation, Custom Registry Setup
* **Meghanath Rao Penchala** – Frontend (React + TypeScript), Backend (Node.js)
* **Jagath Kumar Reddy Katama Reddy** – Kafka Integration, Database APIs


