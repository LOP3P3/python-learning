try:
    num1 = int(input("Введи 1st число: "))
    num2 = int(input("Введи 2nd число: "))
    print(num1 / num2)
except ValueError:
    print("ЭТО НЕ ЧИСЛО!")
except ZeroDivisionError:
    print("НА 0 / НЕЛЬЗЯ!!!")


def classify_port(port: int):
        if not isinstance(port, int):
            return "error: порт должен быть числом"
        if port <= 1023:
            return f"{port} -> well-known"
        elif port <= 49151:
            return f"{port} -> registered"
        elif port <= 65535:
            return f"{port} -> dynamic/private"
        else:
            return f"{port} -> error"
        
port_input = input("Введи номер порта: ")

try:
    port = int(port_input)
    print(classify_port(port))
except ValueError:
    print("Ошибка: нужно ввести число, а не текст")