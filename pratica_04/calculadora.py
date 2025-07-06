
while True:
    try:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        op = input("Operação (+-*/): ")
        
        if op == '+': print(n1 + n2)
        elif op == '-': print(n1 - n2)
        elif op == '*': print(n1 * n2)
        elif op == '/': print(n1 / n2)
        else: continue
        
        break
    except ValueError: print("Por favor digite números válidos!")
    except ZeroDivisionError: print("Por favor não divida por zero!")