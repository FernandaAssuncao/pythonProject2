def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f"\033[1:31mERRO, {entrada} não é um preço valido!!!\033[m")
        else:
            valido = True
            return float(entrada)