ports = [22, 80, 443, 8080, 31337, 64436, 23123, 222222222]

for port in ports:
    if port <= 1023:
        print(f"{port} -> well-known")
    elif port <= 49151:
        print(f"{port} -> registered")
    elif port <= 65535:
        print(f"{port} -> dynamic/private")
    else:
        print(f"{port} -> error")