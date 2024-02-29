from datetime import date
print(f'-=-' *12)
print('Confederação Nacional de Natação')
print(f'-=-' *12)
ano = int(input('Qual é o ano do seu nascimento, atleta? '))
# Idade recebe ANO ATUAL - ANO DE NASCIMENTO
idade = date.today().year - ano
# Se a idade for menor ou igual a 9
if idade <= 9:
    print(f'Você tem {idade} ano(s). Até 9 anos: MIRIM')
# Se a idade for maior que 9 e menor ou igual a 14
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos. Até 14 anos: INFANTIL')
# Se a idade for maior que 14 e menor ou igual a 19
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos. Até 19 anos: JÚNIOR')
# Se a idade for maior que 19 e menor ou igual a 20
elif idade > 19 and idade <= 20:
    print(f'Você tem {idade} anos. Até 20 anos: SÊNIOR')
# Se a idade for maior que 20
elif idade > 20:
    print(f'Você tem {idade} anos. Acima de 20 anos: MASTER')
