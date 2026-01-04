import ipaddress

def parse_targets(target_str):
  """
  Zet een input string (IP, range of CIDR) om naar een lijst van IP strings.
  Ondersteunt:
  - 192.168.1.1  (single)
  - 192.168.1.0/24  (CIDR)
  - 192.168.1.1-192.168.1.5  (range)
  """
  ips = []

  if "-" in target_str:
    try:
      start_ip, end_ip = target_str.split("-")
      start = ipaddress.IPv4Address(start_ip.strip())
      end = ipaddress.IPv4Address(end_ip.strip())

      for ip_int in range(int(start), int(end) +1):
        ips.append(str(ipaddress.IPv4Address(ip_int)))
    except ValueError:
      print(f"⚠️Fout bij parsen range: {target_str}")
  else:
    try:
      net = ipaddress.ip_network(target_str, strict=False)
      for ip in net:
        ips.append(str(ip))
    except ValueError:
      ips.append(target_str)
  return ips

def validate_ip(ip):
  """Simpele check of een string geldig is."""
  try:
    ipaddress.IPv4Address(ip)
    return True
  except:
    return False