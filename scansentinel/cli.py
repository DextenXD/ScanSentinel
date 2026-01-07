import argparse
from .scanner import ScannerController

controller = ScannerController()

def run_scan(args):
    controller.run_scan(target_input=args.ip, export_file=args.json)


def run_monitor(args):
    if not args.ports:
        print("⚠️ Voor monitor moet je poorten opgeven")
        return
    controller.run_scan(target_input=args.ip, ports=args.ports)

def run_version(args):
    print("ScanSentinel Version: 0.1.0")



def main():
    parser = argparse.ArgumentParser(prog="scansentinel", description="Network scanning tool")
    subparser = parser.add_subparsers(dest="command", required=True)

    # ===== subcommand: scan =====
    scan_parser = subparser.add_parser("scan", help="Scan a target IP or Range")
    scan_parser.add_argument("--ip", required=True, help="Target IP, Range (1.1-1.5) or CIDR (1.0/24)")
    scan_parser.add_argument("--json", help="Export result to JSON file")
    scan_parser.set_defaults(func=run_scan)

    # ===== subcommand: monitor =====
    mon_parser = subparser.add_parser("monitor", help="Scan specific ports on target")
    mon_parser.add_argument("--ip", required=True, help="Target IP")
    mon_parser.add_argument("--ports", nargs="+", required=True, help="Ports to scan (space separated)")
    mon_parser.set_defaults(func=run_monitor)

    # ===== subcommand: version =====
    ver_parser = subparser.add_parser("version", help="Returns application version")
    ver_parser.set_defaults(func=run_version)

    args = parser.parse_args()
    args.func(args)