blocked_ips = ["192.168.1.5", "10.0.0.7", "172.16.0.9"]

# 1. Добавь в список новый IP "192.168.1.100" — через .append(...)
blocked_ips.append("192.168.1.100")
print(blocked_ips)

# 2. Удали из списка "10.0.0.7" — через .remove(...)
blocked_ips.remove("10.0.0.7")
print(blocked_ips)

# 3. Отсортируй список по алфавиту — через .sort()
blocked_ips.sort()

# 4. Выведи финальный список через print(blocked_ips)
print(blocked_ips)

