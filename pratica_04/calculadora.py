
# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.
# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

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