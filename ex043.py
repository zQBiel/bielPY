peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = peso / (alt**2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Abaixo de 18.5: Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.1f}. Entre 18.5 e 25: Peso ideal')
elif imc >= 25 and imc <= 30:
    print(f'Seu IMC é {imc:.1f}. De 25 até 30: Sobrepeso')
elif imc >= 30 and imc <= 40:
    print(f'Seu IMC é {imc:.1f}. De 30 até 40: Obesidade')
elif imc > 40:
    print(f'Seu IMC é {imc:.1f}. Acima de 40: Obesidade mórbida')

