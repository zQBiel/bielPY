produto = float(input('Digite o valor original do produto: '))
print('\033[32m-=-' *15)
# Escolha a forma de pagamento
print('\033[33m1 - À vista dinheiro/cheque: 10% de desconto')
print('2 - À vista no cartão: 5% de desconto')
print('3 - Em até 2x no cartão: preço normal')
print('4 - Em 3x ou mais no cartão: 20% de juros\033[m')
print('\033[32m-=-\033[m' *15)
met = input('Método de Pagamento: ').strip()
# Se metodo de pagamento for igual a 1
if met == '1':
    result = produto - (produto * (10/100))
    print(f'\033[34mO valor à vista no dinheiro/cheque é \033[31mR${result:.2f}')
# Se metodo de pagamento for igual a 2
elif met == '2':
    result = produto - (produto * (10/100))
    print(f'\033[34mO valor à vista no cartão é \033[31mR${result:.2f}')
# Se metodo de pagamento for igual a 3
elif met == '3':
    result = produto / 2
    print(f'\033[34mO valor de 2x no cartão em cada parcela será de \033[31mR${result:.2f}')
# Se metodo de pagamento for igual a 4
elif met == '4':
    result = (produto + (produto * (20/100)))
    # Escolha a quantidade de parcelas
    print('\033[33m3 - 3x no cartão')
    print('4 - 4x no cartão')
    print('6 - 6x no cartão')
    print('8 - 8x no cartão')
    print('10 - 10x no cartão')
    print('12 - 12x no cartão\033[m')
    parc = input('Em quantas vezes você deseja parcelar? ').strip()
    # Se parcela igual a 3
    if parc == '3':
        print(f'\033[34mO valor total é \033[31mR${result}\033[34m O valor de cada parcela será de \033[31mR${result / 3:.2f}')
    # Se parcela igual a 4
    elif parc == '4':
        print(f'\033[34mO valor total é \033[31mR${result}\033[34m O valor de cada parcela será de \033[31mR${result / 4:.2f}')
    # Se parcela igual a 6
    elif parc == '6':
        print(f'\033[34mO valor total é \033[31mR${result}\033[34m O valor de cada parcela será de \033[31mR${result / 6:.2f}')
    # Se parcela igual a 8
    elif parc == '8':
        print(f'\033[34mO valor total é \033[31mR${result}\033[34m O valor de cada parcela será de \033[31mR${result / 8:.2f}')
    # Se parcela igual a 10
    elif parc == '10':
        print(f'\033[34mO valor total é \033[31mR${result}\033[34m O valor de cada parcela será de \033[31mR${result / 10:.2f}')
    # Se parcela igual a 12
    elif parc == '12':
        print(f'\033[34mO valor total é \033[31mR${result}\033[34m O valor de cada parcela será de \033[31mR${result / 12:.2f}')
    else:
        print('\033[7mDIGITE UM NÚMERO VÁLIDO\033[m')
# Se nenhum desses números for digitado irá aparecer a mensagem seguinte
else:
    print('\033[7mDIGITE UM NÚMERO VÁLIDO\033[m')