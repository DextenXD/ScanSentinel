from pythonping import ping

class HostDiscovery:
  def __init__(self, timeout=1):
    self.timeout = timeout

  def ping_host(self, ip):
    """Stuurt 1 ping request. Return True als host online is."""
    try:
      response = ping(ip, count=1, timeout=self.timeout)
      return response.success()
    except Exception as e:
      print(f"⚠️ ERROR {e}")
      return False
  
  def discover(self, ip_list):
    """Neemt een lijst IP's en returnt alleen de actives IP's."""
    alive_hosts=[]
    print(f"🔎 Checking for {len(ip_list)} hosts for activity...")

    for ip in ip_list:
      if self.ping_host(ip):
        alive_hosts.append(ip)
        print(f"[+] Host up: {ip}")
    
    return alive_hosts
    