from scapy.all import sr1, IP, ICMP
import time
import logging

logging.basicConfig(level=logging.INFO)

def ping(host):
    packet = IP(dst=host)/ICMP()
    logging.info(f"Enviando pacote ICMP para {host}")
    reply = sr1(packet, timeout=2)
    if reply:
        logging.info(f"Recebida resposta de {host}: {reply.summary()}")
        return reply.ttl
    else:
        logging.warning(f"Nenhuma resposta de {host}")
        return None

def monitor_latency(hosts, duration=60):
    start_time = time.time()
    while time.time() - start_time < duration:
        for host in hosts:
            try:
                latency = ping(host)
                logging.info(f"Host: {host}, Latency: {latency} ms")
            except Exception as e:
                logging.error(f"Erro ao pingar o host {host}: {e}")
        time.sleep(5)

if __name__ == "__main__":
    hosts_to_check = ["8.8.8.8", "1.1.1.1"]
    duration = 60  # Monitorar por 60 segundos
    monitor_latency(hosts_to_check, duration)
