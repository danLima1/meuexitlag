import time
from network_monitor import monitor_network
from latency_monitor import monitor_latency
from route_manager import add_route, delete_route
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    hosts_to_check = ["8.8.8.8", "1.1.1.1"]
    duration = 60  # Monitorar por 60 segundos

    # Monitorar a rede
    logging.info("Monitorando a rede...")
    monitor_network(duration)


    logging.info("Monitorando a latência...")
    monitor_latency(hosts_to_check, duration)


    logging.info("Ajustando as rotas...")
    add_route("exemplo.com", "192.168.1.1")

    # delete_route("")
