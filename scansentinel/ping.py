import subprocess
from pythonping import ping


def count(args):
    if args.count:
        return int(args.count[0])  # converts the list to a int
    return None


def timeout(args):
    if args.timeout:
        return int(args.timeout[0])  # converts the list to a int
    return None


def runPing(args):
    try:
        if args.ip:
            ip = args.ip[0]

            # stores args (if there are any)
            ping_args = {}
            if args.count:
                ping_args["count"] = count(args)  # adds count to the dictonary
            if args.timeout:
                ping_args["timeout"] = timeout(args)  # adds timeout to the dictonary

            ping(ip, verbose=True, **ping_args)  # unpacks the arguments

    except KeyboardInterrupt:
        print(f"Exiting the program")
    except RuntimeError as e:
        print(f"Please provide a correct IP address {e}")
    except Exception as e:
        print(f"unexpected error: {e}")


def pingOnce(ip):
    try:
        resp = ping(ip, count=1, timeout=1)
        return resp.success
    except Exception:
        return False
