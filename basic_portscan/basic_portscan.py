import pyfiglet
import sys
import socket
import subprocess
from flags import args, parser

if len(sys.argv) > 1 and sys.argv[1] == '-h':
    parser.print_help()
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


if len(sys.argv) > 1:
    ip = socket.gethostbyname(sys.argv[1])
else:
    print(66 * "*" + "\nTYPE THE IP!! Exiting..\n" + 66 * "*")
    sys.exit()  # If the first arg is not defined

print(66 * "*")
print("SCANNING HOST: " + str(ip))  # Showing the Scan process
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

if args.min_port < args.max_port:  # If the low port is < max port
    scanport(args.min_port, args.max_port)
    print("\nFinished!!")

print("\nExiting...")
