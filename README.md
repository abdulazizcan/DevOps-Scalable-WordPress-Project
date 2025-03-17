# DevOps: Multi-Environment Scalable WordPress

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker Compose](https://img.shields.io/badge/docker-compose-blue.svg)
![Kubernetes](https://img.shields.io/badge/kubernetes-deployment-brightgreen.svg)

This project aims to run WordPress + MySQL + phpMyAdmin with Docker Compose, Swarm, and Kubernetes in a scalable, SSL-enabled, and monitoring-supported environment.

## Structure:

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

# Contributing to DevOps: Scalable WordPress

Thank you! To contribute to this project, please follow the steps below.

## How to Contribute

1. Fork the repository
2. Create a new Branch (feature/your-feature)
3. Make your changes
4. Open a Pull Request

## Code Guidelines

- Use consistent indentation in YAML files
- Follow PEP8 for Python
- Use English in commit messages

## Project Structure

- `docker-compose/`: Compose files
- `docker-swarm/`: Swarm stack files
- `kubernetes/`: K8s manifests (config, deployments, services, ingress)
- `monitoring/`: Python monitoring scripts
- `docs/`: Installation, testing, troubleshooting
- `tests/`: Load tests (JMeter, Locust, Wrk)

Thank you & good luck!

# 11. Frequently Asked Questions (FAQ)

### Let’s Encrypt Error on Localhost Domain

Let’s Encrypt does not issue certificates for invalid TLDs such as localhost.  
**Solution**: Use a real domain or a self-signed certificate.

### Docker Desktop M1/M2 Kernel Issue

`mysql:5.7` does not have ARM support; use `mysql:8.0` or `mariadb` instead.

### MySQL Access Error (ERROR 1045)

Update user privileges:

```sql
ALTER USER 'wp_user'@'%' IDENTIFIED BY '...';
```

### Forgot sudo Password

On a Mac, enter Recovery Mode and reset the password, or use the `passwd` command.

### Performance Test Rate Limit

If you are using a real domain in JMeter/Locust, you might encounter Let’s Encrypt rate limit errors. Use the staging environment instead.

### Author

[Abdulaziz Can](mailto:abdulazizcaan@gmail.com)
