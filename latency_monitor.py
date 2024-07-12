from scapy.all import sr1, IP, ICMP
import time
import logging

logging.basicConfig(level=logging.INFO)

def ping(host):
    packet = IP(dst=host)/ICMP()
    reply = sr1(packet, timeout=2)
    if reply:
        return reply.ttl
    else:
        return None

def monitor_latency(hosts, duration=60):
    start_time = time.time()
    while time.time() - start_time < duration:
        for host in hosts:
            latency = ping(host)
            logging.info(f"Host: {host}, Latency: {latency} ms")
        time.sleep(5)
