def check_age(age: int):
    try:
        if age < 0:
            raise ValueError("возраст не может быть отрицательным")
        result = 100 / age          # специально: если age == 0, будет ZeroDivisionError
    except ValueError as e:
        print(f"Ошибка: {e}")
    except ZeroDivisionError:
        print("Ошибка: возраст не может быть 0")
    else:
        print(f"Всё ок, результат: {result}")
    finally:
        print("Проверка завершена")

def classify_port(port: int):
    try:
        if not isinstance(port, int):
                return "error: порт должен быть числом"
        if port < 0:
            raise ValueError("Порт не может быть отрицательным")
            result = 100 / port
    except ValueError as e:
        print(f"Ошибка: {e}")
    if port <= 1023:
        return f"{port} -> well-known"
    elif port <= 49151:
        return f"{port} -> registered"
    elif port <= 65535:
        return f"{port} -> dynamic/private"
    else:
        return(f"{port} -> Not Found/Error")

port = int(input())
port_result = classify_port(port)
print(port_result)