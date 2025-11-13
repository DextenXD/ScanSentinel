import subprocess
from pythonping import ping

def run_ping(args):
  try:
    if args.ip:
      ip = args.ip[0]
      ping(f"{ip}", verbose=True)
  except Exception as e:
    print(f"Error: {e}")

