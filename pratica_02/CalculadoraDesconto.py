Nomeproduto = input("Digite nome do produto: ")
PrecoOriginal = float(input("Digite o preço do produto: "))
PorcentagemDesconto = float(input("Digite porcentagem do Desconto: "))

CalculoDesconto = ((PrecoOriginal / 100) * PorcentagemDesconto)
PrecoFinal = PrecoOriginal - CalculoDesconto

print(f"Nome do produto: {Nomeproduto}\n"+
      f"Preço original: {PrecoOriginal}\n"+
      f"Porcentagem de desconto: {PorcentagemDesconto}%\n"+
      f"Preço Final: {PrecoFinal:.2f}")