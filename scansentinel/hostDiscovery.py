from .ping import pingOnce
from pythonping import ping

def pingOnce(ip):
    try:
        resp = ping(ip, count=1, timeout=1)
        return resp.success
    except Exception:
        return False
    
def discover_hosts(ip_range):
  start, end = ip_range.split("-")

  # split first 3 octects
  base = ".".join(start.split(".")[:3])

  # takes start/end of host numbers
  startNum = int(start.split(".")[:3])
  endNum = int(end)

  alive = []

  # Nice loop die eerste stukje van ip pakt en dan checkt loopt van 1 tm 254
  for i in range(startNum, endNum + 1):
    ip = f"{base}.{i}"
    if pingOnce(ip):
      alive.append(ip)

  return alive  