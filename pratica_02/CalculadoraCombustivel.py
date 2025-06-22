distancia = (float(input("Digite a distancia percorrida: ")))
combustivel = (float(input("Digite o combustivel gasto: ")))
consumo = (distancia/combustivel)

print(f"Distância percorrida: {distancia} km\nCombustível gasto: {combustivel} litros")
print(f"consumo médio: {consumo:.2f} (km/l)")