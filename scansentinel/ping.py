import subprocess
from pythonping import ping


def count(args):
    if args.count:
        return int(args.count[0])  
    return None


def timeout(args):
    if args.timeout:
        return int(args.timeout[0])  
    return None


def runPing(args):
    try:
        if args.ip:
            ip = args.ip[0]

            
            ping_args = {}
            if args.count:
                ping_args["count"] = count(args)  
            if args.timeout:
                ping_args["timeout"] = timeout(args)  

            ping(ip, verbose=True, **ping_args) 

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
