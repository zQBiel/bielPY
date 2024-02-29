nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi {media:.1f} pontos. REPROVADO(A)')
elif media > 5 and media < 6.9:
    print(f'Sua média foi {media:.1f} pontos. RECUPERAÇÃO')
elif media >= 7:
    print(f'Sua média foi {media:.1f} pontos. APROVADO(A)')