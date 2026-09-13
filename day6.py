suspicious_ips = ["45.33.32.156", "185.220.101.5", "104.244.72.115" ] 


with open("suspicious_ips.txt", "w") as f:
    for ip in suspicious_ips:
        f.write(f"{ip}\n")

with open("suspicious_ips.txt", "r") as f:
    for line in f:
        print(line.strip())

print("done reading and writing")