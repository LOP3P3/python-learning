def greet(name):
    print(f"Hello, {name}!")

def math(a , b):
    print(a + b)
    print(a - b)
    print(a * b)

def square(x):
    return x * x 

result = square(67)
print(result)

math(45, 222)
greet("Six Seven")
greet("Test")



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


resultClassify_port = classify_port(5112)
print(resultClassify_port)