import moeda
num = float(input("Preço do produto: R$"))
print(f"Produto com 20% de aumento {moeda.aumentar(num, True)}")
print(f"Protudo com 15% de desconto {moeda.diminuir(num, True)}")
print(f"O dobro do preço é {moeda.dobro(num, True)}")
print(f"A metade do preço é {moeda.metade(num, True)}")
