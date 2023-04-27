from currency_converter import CurrencyConverter

c = CurrencyConverter()

while True:
    valor = float(input('Digite um valor: '))
    print('Opções de moedas')
    print('1 - USD')
    print('2 - BRL')
    print('3 - OUTRA')
    moeda_inicial = int(input('Escolha uma moeda inicial: '))
    if moeda_inicial == 1:
        moeda_inicial = 'USD'
    elif moeda_inicial == 2:
        moeda_inicial = 'BRL'
    elif moeda_inicial == 3:
        moeda_inicial = input(
            'Digite o código da moeda em 3 digitos: ').upper()

    print('1 - USD')
    print('2 - BRL')
    print('3 - OUTRA')
    moeda_cambio = int(input('Escolha uma moeda de câmbio: '))
    if moeda_cambio == 1:
        moeda_cambio = 'USD'
    elif moeda_cambio == 2:
        moeda_cambio = 'BRL'
    elif moeda_cambio == 3:
        moeda_cambio = input('Digite o código da moeda em 3 digitos: ').upper()

    valor_convertido = c.convert(valor, moeda_inicial, moeda_cambio)
    print(f'{valor:.2f} {moeda_inicial} = {valor_convertido:.2f} {moeda_cambio} ')
