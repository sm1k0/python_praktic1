import math
def math_opperation():
    global add, subtract, multiply, divide, power, square_root, factorial, sin, cos, tan, get_number_input, get_operation_input
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            print("Ошибка: Деление на ноль недопустимо!")
            return None
    def power(a, b):
        return a ** b
    def square_root(a):
        if a >= 0:
            return math.sqrt(a)
        else:
            print("Ошибка: Квадратный корень из отрицательного числа недопустим!")
            return None
    def factorial(a):
        if a >= 0:
            return math.factorial(a)
        else:
            print("Ошибка: Факториал отрицательного числа не определен!")
            return None
    def sin(a):
        return math.sin(math.radians(a))
    def cos(a):
        return math.cos(math.radians(a))
    def tan(a):
        return math.tan(math.radians(a))
    def get_number_input(prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print("Ошибка: Введите число!")
    def get_operation_input():
        valid_operations = ['+', '-', '*', '/', '^', 'sqrt', 'fact', 'sin', 'cos', 'tan']
        while True:
            operation = input("Выберите операцию (+, -, *, /, ^, sqrt, fact, sin, cos, tan): ")
            if operation in valid_operations:
                return operation
            else:
                print("Ошибка: Неверная операция!")
math_opperation()
while True:
    print("Доступные операции: +, -, *, /, ^, sqrt, fact, sin, cos, tan")
    operation = get_operation_input()
    if operation in ['+', '-', '*', '/', '^']:
        a = get_number_input("Введите первое число: ")
        b = get_number_input("Введите второе число: ")
        if operation == '+':
            result = add(a, b)
        elif operation == '-':
            result = subtract(a, b)
        elif operation == '*':
            result = multiply(a, b)
        elif operation == '/':
            result = divide(a, b)
        elif operation == '^':
            result = power(a, b)
        if result is not None:
            print("Ответ: ", result)
    elif operation in ['sqrt', 'fact', 'sin', 'cos', 'tan']:
        a = get_number_input("Введите число: ")
        if operation == 'sqrt':
            result = square_root(a)
        elif operation == 'fact':
            result = factorial(int(a))
        elif operation == 'sin':
            result = sin(a)
        elif operation == 'cos':
            result = cos(a)
        elif operation == 'tan':
            result = tan(a)
        if result is not None:
            print("Ответ: ", result)
    choice = input("Хотите продолжить вычисления? (y/n): ")
    if choice.lower() != 'y':
        break