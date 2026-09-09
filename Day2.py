ports = [22, 80, 443, 8080, 31337, 64436, 23123, 222222222]

for p in ports:
    if p <= 1023:
        print(f"{p} -> well-known")
    elif p <= 49151:
        print(f"{p} -> registered")
    elif p <= 65535:
        print(f"{p} -> dynamic/private")
    else:
        print(f"{p} -> error")