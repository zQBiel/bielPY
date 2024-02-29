cor = {'amarelo':'\033[33m',
       'clean':'\033[m',
       'branco':'\033[7:97m',
       'azul':'\033[36m'}
print(f'{cor['amarelo']}-=-{cor['clean']}' * 10)
print('Analisador de Triângulos')
print(f'{cor['amarelo']}-=-{cor['clean']}' * 10)
# Analisando as Retas
r1 = float(input(f'{cor['branco']}Primeira reta:{cor['clean']} '))
r2 = float(input(f'{cor['branco']}Segunda reta:{cor['clean']} '))
r3 = float(input(f'{cor['branco']}Terceira reta:{cor['clean']} '))
# O valor de duas retas deve ser maior do que a terceira
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'{cor['amarelo']}As retas podem formar um triângulo!')
    # Senão se r1 igual a r2 e r3
    if r1 == r2 == r3:
        print(f'{cor['azul']}Equilátero: {cor['amarelo']}todos os lados iguais')
    # Senão se r1 igual a r2 ou r1 igual a r3 ou r2 igual a r3
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f'{cor['azul']}Isósceles: {cor['amarelo']}dois lados iguais')
    # Senão se r1 diferente de r2 e diferente de r3
    elif r1 != r2 != r3:
        print(f'{cor['azul']}Escaleno: {cor['amarelo']}todos os lados diferentes')
else:
    print(f'{cor['amarelo']}As retas não podem formar um triângulo!')

