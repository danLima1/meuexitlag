import psutil
import time
import logging

logging.basicConfig(level=logging.INFO)

def get_network_info():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }

def monitor_network(duration=60):
    start_time = time.time()
    while time.time() - start_time < duration:
        net_info = get_network_info()
        logging.info(f"Bytes Enviados: {net_info['bytes_sent']}, Bytes Recebidos: {net_info['bytes_recv']}")
        time.sleep(100)
