while True:
    try:
        quantidade_alunos = int(input("Quantidade de Alunos: "))
        acumulador = 0

        for i in range(quantidade_alunos):
            print(f'\nAluno {i+1}\n')
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            n3 = float(input("Nota 3: "))
            
            media_aluno = (n1+n2+n3)/3
            acumulador += media_aluno

        media_turma = acumulador/quantidade_alunos
        print(f'\nA media da turma é: {media_turma}')
        
        break
    except ValueError: print("Por favor digite números válidos!")