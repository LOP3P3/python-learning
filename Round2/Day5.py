ping_result = {"google.com":40, "pinterest.com":22, "aaac":1337, "namemc.com":67}

def rate_ping(x):
    if x <= 50:
        return "Пинг отличный!"
    elif x <= 200:
        return "Нормально"
    else:
        return "БЕДА СЛИШКОМ БОЛЬШОЙ"
    
for name, ping in ping_result.items():
    print("~=0=~" * 5)
    print(f"Сайт: {name}\nПинг: {ping} |", rate_ping(ping))
print("~=0=~" * 5)
