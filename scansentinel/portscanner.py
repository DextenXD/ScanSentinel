import socket
import concurrent.futures

class PortScanner:
  def __init__(self, threads=50, timeout=1):
    self.threads = threads
    self.timeout = timeout

  def check_port(self, ip, port):
    """Probeert verbinding te maken met een poort"""
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(self.timeout)
        result = s.connect_ex((ip, port))
        if result == 0:
          return port
    except:
      pass
    return None
  
  def scan_host(self, ip, ports):
    """Scant een lijst poorten voor een IP met multithreading."""
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
      future_to_port = {executor.submit(self.check_port, ip, port): port for port in ports}

      for future in concurrent.futures.as_completed(future_to_port):
        port = future_to_port[future]
        if future.result():
          open_ports.append(port)

    return sorted(open_ports)