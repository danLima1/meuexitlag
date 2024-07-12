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

    # Monitorar a latência
    logging.info("Monitorando a latência...")
    monitor_latency(hosts_to_check, duration)

    # Adicionar ou ajustar rotas conforme necessário
    logging.info("Ajustando as rotas...")
    add_route("52.95.110.1", "192.168.0.1")
    # Para deletar uma rota, descomente a linha abaixo
    # delete_route("52.95.110.1")
