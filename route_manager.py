import os
import logging

logging.basicConfig(level=logging.INFO)

def add_route(destination, gateway):
    command = f"rota adicionada {destination} gw {gateway}"
    result = os.system(command)
    if result == 0:
        logging.info(f"Rota para {destination} via {gateway} adicionada com sucesso")
    else:
        logging.error(f"Falha ao adicionar rota {destination} via {gateway}.")

def delete_route(destination):
    command = f"route del {destination}"
    result = os.system(command)
    if result == 0:
        logging.info(f"Rota para {destination} deleteda com sucesso.")
    else:
        logging.error(f"Falha ao deletar rota {destination}.")
