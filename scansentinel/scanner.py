from .util import parse_targets
from .hostDiscovery import HostDiscovery
from .portscanner import PortScanner
from .reporter import Reporter

class ScannerController:
  def __init__(self):
    self.discovery = HostDiscovery()
    self.scanner = PortScanner()
    self.result = {}

  def run_scan(self, target_input, ports=None, export_file=None):
    ip_list = parse_targets(target_input)
    alive_hosts = self.discovery.discover(ip_list)

    if not alive_hosts:
      print("⚠️ Geen active Hosts gevonden.")
      return
    
    if not ports:
      ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]
    else:
      ports = [int(p) for p in ports]

    print(f"\n🚀 Start port scan op {len(alive_hosts)} hosts...")

    for ip in alive_hosts:
      print(f"  -> Scanning {ip}...")
      open_ports = self.scanner.scan_host(ip, ports)

      if open_ports:
        print(f" 🔓 Open poorten op {ip}: {open_ports}")
        self.result[ip] = open_ports
      else:
        print(f" 🔒 Geen open porten gevonden op {ip}")
      
      if export_file:
        Reporter.export_json(self.result, export_file)