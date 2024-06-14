import socket
import json

def scan_ports(ip_address, start_port, end_port):
    results = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip_address, port))
            s.close()

            if result == 0:
                results.append({"port": port, "status": "open"})
            else:
                results.append({"port": port, "status": "closed"})

        except Exception as e:
            results.append({"port": port, "status": "filtered"})

    return results

def main():
    ip_address = input("Enter IP Address: ")
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    results = scan_ports(ip_address, start_port, end_port)
    print(json.dumps({"results": results}, indent=2))

if __name__ == '__main__':
    main()