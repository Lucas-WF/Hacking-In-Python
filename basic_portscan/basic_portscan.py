import pyfiglet
import sys
import socket
import subprocess
from datetime import datetime
from flags import args, parser

if len(sys.argv) > 1 and sys.argv[1] == '-h' or len(sys.argv) > 1 and sys.argv[1] == "--help":  # If the args is a flag 
    parser.print_help()  # Printing the flags help
    sys.exit()
elif len(sys.argv) > 1:  # If the args is the IP
    ip = socket.gethostbyname(sys.argv[1])
else:  # If no args
    parser.print_help()  # Printing the flags help
    sys.exit()

subprocess.call("clear", shell=True)

if sys.platform.startswith("linux"):
    red_color = "\033[1;31m"
    reset_color = "\033[0;0m"
    ascii_banner = pyfiglet.figlet_format("PY PORTSCAN")
    print(red_color + ascii_banner + reset_color)  # Printing the banner with colors (for Linux)
else:
    ascii_banner = pyfiglet.figlet_format("PY PORTSCAN")
    print(ascii_banner)  # Printing the banner without colors

ft = datetime.now()
print(66 * "*")
print(f"SCANNING HOST: {ip}")  # Showing the Scan process
print(f"Started in {ft}")
print(66 * "*")


def scanport(low_port=1, high_port=1000):
    try:  # To cover errors or not
        for ports in range(low_port, high_port):  # For all ports
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket
            socket.setdefaulttimeout(1)  # Setting a timeout
            if s.connect_ex((ip, ports)) == 0:  # If the ports are open
                print(socket.getservbyport(ports).upper() + f" - Port {ports} open")
            s.close()

    except KeyboardInterrupt:
        print("\n\nExiting!!")
        sys.exit()
    except socket.gaierror:
        print("No host defined!")
        sys.exit()
    except socket.timeout:  # Never occurs because we defined a timeout. But if you want do del the timeout
        print("Timeout Error")
        sys.exit()
    except socket.error:
        print("No server response!")
        sys.exit()

if args.min_port <= args.max_port:  # If the low port is < max port
    scanport(args.min_port, args.max_port)

et = datetime.now()
print(f"\nFinished in {et}")

print("\nExiting...")
