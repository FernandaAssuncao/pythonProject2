import moeda
num = float(input("Preço do produto: R$"))
print(f"Produto com 20% de aumento {moeda.aumentar(num)}")
print(f"Protudo com 15% de desconto {moeda.diminuir(num)}")
print(f"O dobro do preço é {moeda.dobro(num)}")
print(f"A metade do preço é {moeda.metade(num)}")
