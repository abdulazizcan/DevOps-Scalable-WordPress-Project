# DevOps: Multi-Environment Scalable WordPress

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker Compose](https://img.shields.io/badge/docker-compose-blue.svg)
![Kubernetes](https://img.shields.io/badge/kubernetes-deployment-brightgreen.svg)

This project aims to run WordPress + MySQL + phpMyAdmin with Docker Compose, Swarm, and Kubernetes in a scalable, SSL-enabled, and monitoring-supported environment.

## Structure:
```bash
📦 # DevOps: Multi-Environment Scalable WordPress
┣ 📂 docker-compose  
┃ ┗ 📜 docker-compose.yaml  
┣ 📂 docker-swarm  
┃ ┗ 📜 swarm-stack.yaml  
┣ 📂 kubernetes  
┃ ┣ 📂 config  
┃ ┃ ┗ 📜 monitoring  
┃ ┣ 📂 deployments  
┃ ┃ ┣ 📜 monitoring.yaml  
┃ ┃ ┣ 📜 mysql-statefulset.yaml  
┃ ┃ ┣ 📜 phpmyadmin-deployment.yaml  
┃ ┃ ┗ 📜 wordpress-deployment.yaml  
┃ ┣ 📂 ingress  
┃ ┃ ┗ 📜 ingress.yaml  
┃ ┣ 📂 rbac  
┃ ┃ ┗ 📜 rbac.yaml  
┃ ┣ 📂 services  
┃ ┃ ┣ 📜 mysql-service.yaml  
┃ ┃ ┣ 📜 phpmyadmin-service.yaml  
┃ ┃ ┗ 📜 wordpress-service.yaml  
┃ ┗ 📂 monitoring  
┃ ┣ 📜 Dockerfile  
┃ ┣ 📜 container_monitor.py  
┃ ┗ 📜 requirements.txt  
┗ 📜 .env
```
[go to CONTRIBUTING.md file](https://github.com/abdulazizcan/DevOps-Scalable-WordPress-Project/blob/main/CONTRIBUTING.md)

## Features

- Docker Compose / Swarm / Kubernetes
- MySQL cluster (optional)
- SSL (Let’s Encrypt / Self-signed)
- Python monitoring
- Performance testing (1M requests, JMeter / Locust)

## Quick Start (Docker Compose)

```bash
cd docker-compose
docker-compose up -d
WordPress: http://localhost:8080
phpMyAdmin: http://localhost:8081
```

### Transition to Kubernetes

```bash
kubectl apply -f kubernetes/config/
kubectl apply -f kubernetes/deployments/
kubectl apply -f kubernetes/services/
kubectl apply -f kubernetes/ingress/
```

### Monitoring

`config/monitoring/container_monitor.py` is a simple example script.

## Contribution

To contribute, please refer to the CONTRIBUTING.md file.

## License

MIT

### Author

[Abdulaziz Can](mailto:abdulazizcaan@gmail.com)
