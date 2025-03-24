import socket

def scan_tcp_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"TCP Port {port} is open")  # Only print open ports
        s.close()
    except Exception as e:
        pass  # Ignore errors

def scan_udp_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        s.settimeout(1)
        s.sendto(b'', (target, port))  # Send an empty packet
        try:
            data, _ = s.recvfrom(1024)  # Try receiving a response
            print(f"UDP Port {port} is open or responding")
        except socket.timeout:
            pass  # Ignore closed/filtered ports
        s.close()
    except Exception as e:
        pass  # Ignore errors

target_ip = input("Enter target IP: ")
print(f"\nScanning {target_ip}...\n")

for port in range(1, 1025):  # Scans ports 1-1024
    scan_tcp_port(target_ip, port)
    scan_udp_port(target_ip, port)
