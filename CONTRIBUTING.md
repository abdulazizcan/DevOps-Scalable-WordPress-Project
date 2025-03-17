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
