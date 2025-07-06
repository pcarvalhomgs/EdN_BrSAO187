def verificar_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
    
while True:
        frase = input("Digite uma palavra ou frase (0 para Sair): ")

        if frase == '0':
             break
        
        resultado = verificar_palindromo(frase)
        print(f"É palíndromo? {resultado}")
        
