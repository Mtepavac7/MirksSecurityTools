import socket
import re
from ipaddress import ip_address

# Setting up the target IP.
# Ensure IP address is properly formatted.
# If not, prompt user to re-enter IP address.
def get_target():
    while True:
        target = input("Please enter the IP address you want to scan >> ")
        try:
            target = ip_address(target)
            return target
        except ValueError:
            print("Please enter a valid IP address")

# Get ports to scan.
def get_ports():
    while True:
        ports_option = input("Please select a scanning option:\n[1] - Full Port Scan\n[2] - Common Ports\n[3] - Specific Port\n[q] - Quit\n>> ")
        if ports_option == "1":
            print("Scanning all ports")
            ports = range(1, 65536)
            return ports
        elif ports_option == "2":
            print("Scanning common ports")
            ports = [20, 21, 22, 23, 25, 69, 137, 139, 445, 53, 443, 80, 8080, 8443]
            return ports
        elif ports_option == "3":
            specific_port = input("Please enter the port you want to scan >> ")
            try:
                specific_port = int(specific_port)
                if 1 <= specific_port <= 65535:
                    print(f"Scanning specific port {specific_port}")
                    ports = [specific_port]
                    return ports
                else:
                    print("Please enter a valid port number (1-65535).")
            except ValueError:
                print("Please enter a valid port number.")
        elif ports_option == "q":
            exit()
        else:
            print("Please enter a valid option")

# Scan ports
def scan(target, ports):
    socket.setdefaulttimeout(1)
    try:
        for port in ports:
            conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = conn_skt.connect_ex((str(target), port))
            if result == 0:
                print(f"[+] TCP port {port} is open on host {target}")
            else:
                print(f"[-] TCP port {port} is closed on host {target}")
            conn_skt.close()
    except socket.error as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    target = get_target()
    ports = get_ports()
    scan(target, ports)
