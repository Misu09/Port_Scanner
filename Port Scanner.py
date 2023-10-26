import socket

def scan_ports(hostname, port_range):
    open_ports = []
    count = 1
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((hostname, port))
        if result == 0:
            open_ports.append(port)
        
        sock.close()
    
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target hostname or IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    ports = range(start_port, end_port + 1)
    open_ports = scan_ports(target_host, ports)
    
    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")