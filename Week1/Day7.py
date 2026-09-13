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
            raise TypeError("порт должен быть числом")
        if port < 0:
            raise ValueError("порт не может быть отрицательным")
    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}")
    else:
        if port <= 1023:
            print(f"{port} -> well-known")
        elif port <= 49151:
            print(f"{port} -> registered")
        else:
            print(f"{port} -> dynamic/private")
    finally:
        print("проверка порта завершена")


    
port_input = input("Введи номер порта: ")

try:
    port = int(port_input)
    classify_port(port)
except ValueError as e:
    if "invalid literal" in str(e):
        print("Ошибка: нужно ввести число, а не текст")
    else:
        print(f"Ошибка: {e}")



