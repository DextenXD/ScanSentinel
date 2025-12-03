import argparse
from .ping import runPing
# from .scanner import Scanner

def run_scan(args):
  return print(f"🔍 Scanning {args.ip} for open ports...")
def run_monitor(args):
  return print(f"📊 Monitoring {args.ip} on {args.ports}")
def run_export(args):
  if args.database:
   return print(f"exporting to database: {args.database}")
  elif args.json:
     return print(f"Exporting to {args.json}")
  else: 
    return print("⚠️ No export target provided! Use --database or --json")
def run_version(args):
    return print("Version: 0.1.0")
def run_config(args):
  return print("config configured")
def run_report(args):
  return print("reporting")

def main():
  parser = argparse.ArgumentParser(prog="scansentinel", description="Network scanning tool")
  subparser = parser.add_subparsers(dest="command", required=True)

  # ===== subcommand: scan =====
  scan_parser = subparser.add_parser("scan", help="Scan a target IP for open ports")
  scan_parser.add_argument("--ip", help="Target IP address to scan")
  scan_parser.add_argument("-r", "-range", help="Target IP range (192.168.1.1-254)")
  scan_parser.set_defaults(func=run_scan)

  # ===== subcommand: monitor =====
  scan_parser = subparser.add_parser("monitor", help="Monitors on target IP")
  scan_parser.add_argument("--ip", required=True, help="Target IP address to scan")
  scan_parser.add_argument("--ports", nargs="+", help="Targeted ports to scan")
  scan_parser.set_defaults(func=run_monitor)

  # ===== subcommand: Vesion =====
  scan_parser = subparser.add_parser("version", help="Returns application version")
  scan_parser.add_argument("--v", "-version", nargs="*", required=False, help="Returns application version")
  scan_parser.set_defaults(func=run_version)

  # ===== subcommand: config =====
  scan_parser = subparser.add_parser("config", help="Congigure your aplication")
  scan_parser.add_argument("--c", "-config", nargs="+", required=True, help="Congigure your aplication")
  scan_parser.set_defaults(func=run_config)

  # ===== subcommand: report =====
  scan_parser = subparser.add_parser("report", help="returns a report of you latest scan")
  scan_parser.add_argument("--r", "-report", nargs="+", required=True, help="enter wich scan you want to use")
  scan_parser.set_defaults(func=run_report)

  # ===== subcommand: ping =====
  scan_parser = subparser.add_parser("ping", help="pings your ip or http")
  scan_parser.add_argument("--ip", nargs="*", required=True, help="Specify the IP")
  scan_parser.add_argument("--c", "-count", dest="count", nargs="*", required=False, help="Define how many times you want to ping")
  scan_parser.add_argument("--t", "-timeout", dest="timeout", nargs="*", required=False, help="Specify the timeout for pinging")
  scan_parser.set_defaults(func=runPing)

  # ===== subcommand: export as =====
  scan_parser = subparser.add_parser("export", help="Export data to your database or save as json")
  scan_parser.add_argument("-d" ,"--database", nargs="?", help="Export database (provide DB URL or name)", metavar="DB")
  scan_parser.add_argument("-j", "--json", nargs="?", const="export.json",
                           help="Save as json (optinal filename, default: export.json)", metavar="FILE")
  scan_parser.set_defaults(func=run_export)



  args = parser.parse_args()

  args.func(args)