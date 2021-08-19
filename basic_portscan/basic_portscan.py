import pyfiglet
import sys
import socket

ascii_banner = pyfiglet.figlet_format("PORTSCAN")
print(ascii_banner)  # Printing the banner

ip = socket.gethostbyname(sys.argv[1]) if len(sys.argv) > 1 else print(66 * "*" + "\nTYPE THE IP!! Exiting..\n" + 66 * "*") and sys.exit()

if ip is not None:
    print(66 * "*")
    print("SCANNING HOST: " + str(ip))
    print(66 * "*")
    try:
        for ports in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            if s.connect_ex((ip, ports)) == 0:
                print(socket.getservbyport(ports).upper() + f" - Port {ports} open")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting!!")
        sys.exit()
    except socket.gaierror:
        print("No host defined!")
        sys.exit()
    except socket.timeout:
        print("Timeout Error")
        sys.exit()
    except socket.error:
        print("No server response!")
        sys.exit()
