port_services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP"
}

open_ports = [22, 443, 8080, 80, 3389]

for port in open_ports:
    if port in port_services:
        print(f"{port} -> {port_services[port]}")
    else:
        print(f"{port} -> неизвестный сервис")