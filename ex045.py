import random
ppt = str(input('Pedra, Papel ou Tesoura? ')).strip().upper()
pal = ['PEDRA', 'PAPEL', 'TESOURA']
robo = random.choice(pal)
if ppt == robo:
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. EMPATE!!!')

elif ppt == 'PEDRA' and robo == 'TESOURA':
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. VOCÊ GANHOU!!!')

elif ppt == 'PAPEL' and robo == 'PEDRA':
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. VOCÊ GANHOU!!!')

elif ppt == 'TESOURA' and robo == 'PAPEL':
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. VOCÊ GANHOU!!!')

elif ppt == 'PEDRA' and robo == 'PAPEL':
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. VOCÊ PERDEU!!!')

elif ppt == 'PAPEL' and robo == 'TESOURA':
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. VOCÊ PERDEU!!!')

elif ppt == 'TESOURA' and robo == 'PEDRA':
    print(f'Você escolheu {ppt} e o computador escolheu {robo}. VOCÊ PERDEU!!!')
