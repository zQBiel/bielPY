num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print(f'O número {num1} é maior do que {num2}')
elif num2 > num1:
    print(f'O número {num2} é maior do que {num1}')
elif num1 == num2:
    print(f'Os dois números são iguais')