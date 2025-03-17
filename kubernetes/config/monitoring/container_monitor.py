# container_monitor.py

import os
import logging
import smtplib
from email.message import EmailMessage
import time

# Kubernetes için:
try:
    from kubernetes import client, config
    K8S_ENABLED = True
except ImportError:
    K8S_ENABLED = False

# Docker Swarm için:
# try:
#     import docker
#     DOCKER_ENABLED = True
# except ImportError:
#     DOCKER_ENABLED = False

DOCKER_ENABLED = False

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class ContainerMonitor:
    def __init__(self):
        self.email_from = "test@example.com"
        self.email_to = "admin@example.com"
        self.smtp_server = "localhost"  
        
        # Kubernetes config
        if K8S_ENABLED:
            try:
                config.load_incluster_config()
                logger.info("Kubernetes in-cluster config yüklendi.")
            except:
                try:
                    config.load_kube_config()
                    logger.info("Kubernetes local config yüklendi.")
                except:
                    logger.error("Kubernetes config yüklenemedi.")
                    pass
            self.k8s_client = client.CoreV1Api() if K8S_ENABLED else None

        # Docker client
        if DOCKER_ENABLED:
            try:
                self.docker_client = docker.from_env()
                logger.info("Docker client init başarılı.")
            except Exception as e:
                logger.error(f"Docker client init hatası: {e}")
                self.docker_client = None

    def check_k8s_pods(self):
        if not K8S_ENABLED or not self.k8s_client:
            logger.info("Kubernetes modülü bulunamadı veya devre dışı.")
            return

        try:
            pods = self.k8s_client.list_pod_for_all_namespaces(watch=False)
            for pod in pods.items:
                status = pod.status.phase
                if status != "Running":
                    msg = f"[K8S] Pod Hatası: {pod.metadata.name} - Durum: {status}"
                    self.log_and_alert(msg)
        except Exception as e:
            logger.error(f"K8s kontrol hatası: {str(e)}")

    def check_swarm_services(self):
        if not DOCKER_ENABLED or not self.docker_client:
            logger.info("Docker Swarm modülü bulunamadı veya devre dışı.")
            return

        try:
            services = self.docker_client.services.list()
            for service in services:
                tasks = service.tasks()
                # Eğer hiçbir task 'running' değilse hata
                if not any(task['Status']['State'] == 'running' for task in tasks):
                    msg = f"[Swarm] Servis Hatası: {service.name}"
                    self.log_and_alert(msg)
        except Exception as e:
            logger.error(f"Swarm kontrol hatası: {str(e)}")

    def log_and_alert(self, message):
        return
        logger.warning(message)
        self.send_email_alert(message)

    def send_email_alert(self, message):
        """ İsterseniz e-posta kısmını tamamen kapatabilirsiniz. """
        try:
            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = 'Container Monitor Alarm!'
            msg['From'] = self.email_from
            msg['To'] = self.email_to
            
            with smtplib.SMTP(self.smtp_server, 25) as server:
                server.send_message(msg)

            logger.info("E-posta bildirimi gönderildi.")
        except Exception as e:
            logger.error(f"E-posta gönderilemedi: {str(e)}")

if __name__ == "__main__":
    while True:
        logger.info("Monitoring başlatılıyor...")
        monitor = ContainerMonitor()
        monitor.check_k8s_pods()
        monitor.check_swarm_services()
        logger.info("Kontrol tamamlandı.")
        time.sleep(600) 

