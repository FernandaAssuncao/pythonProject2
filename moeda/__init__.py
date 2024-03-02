def aumentar(n, formato=False):
    aumento = n + (n * 20 / 100)
    return aumento if formato is False else moeda(aumento)


def diminuir(n, formato=False):
    diminui = n - (n * 15 / 100)
    return diminui if formato is False else moeda(diminui)


def dobro(n, formato=False):
    dobroo = n * 2
    return dobroo if formato is False else moeda(dobroo)


def metade(n, formato=False):
    met = n / 2
    return met if formato is False else moeda(met)


def moeda(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num):
    print("=" * 30)
    print("RESUMO DO VALOR".center(30))
    print("=" * 30)
    print(f"Preço analisado: \t{moeda(num)}")
    print(f"Dobro do preço: \t{dobro(num, True)}")
    print(f"Metade do preço: \t{metade(num, True)}")
    print(f"20% de aumento: \t{aumentar(num, True)}")
    print(f"15% de desconto: \t{diminuir(num, True)}")
    print("=" * 30)
