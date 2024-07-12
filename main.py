import time
from network_monitor import monitor_network
from latency_monitor import monitor_latency
from route_manager import add_multiple_routes, delete_multiple_routes
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

    # Adicionar múltiplas rotas
    logging.info("Ajustando as rotas...")
    routes_to_add = {
        "162.159.192.10": "192.168.1.1",  # IP identificado do servidor de Fortnite
        "52.95.110.1": "192.168.1.1"  # Outro exemplo de IP
    }
    add_multiple_routes(routes_to_add)

    # Para deletar múltiplas rotas, descomente as linhas abaixo
    # routes_to_delete = ["162.159.192.10", "52.95.110.1"]
    # delete_multiple_routes(routes_to_delete)
