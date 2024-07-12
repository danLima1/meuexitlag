import os
import platform
import logging

logging.basicConfig(level=logging.INFO)


def add_route(destination, gateway):
    system = platform.system()
    if system == "Windows":
        command = f"route ADD {destination} MASK 255.255.255.255 {gateway}"
    else:  # Assume Linux/macOS
        command = f"sudo route add -host {destination} gw {gateway}"

    logging.info(f"Executando comando: {command}")
    result = os.system(command)
    if result == 0:
        logging.info(f"Rota para {destination} via {gateway} adicionada com sucesso.")
    else:
        logging.error(f"Falha ao adicionar rota para {destination} via {gateway}.")


def delete_route(destination):
    system = platform.system()
    if system == "Windows":
        command = f"route DELETE {destination}"
    else:  # Assume Linux/macOS
        command = f"sudo route del -host {destination}"

    logging.info(f"Executando comando: {command}")
    result = os.system(command)
    if result == 0:
        logging.info(f"Rota para {destination} removida com sucesso.")
    else:
        logging.error(f"Falha ao remover rota para {destination}.")


def add_multiple_routes(routes):
    for destination, gateway in routes.items():
        add_route(destination, gateway)


def delete_multiple_routes(destinations):
    for destination in destinations:
        delete_route(destination)
