from datetime import date
cor = {'limpa':'\033[m'}
ano = int(input('\033[33mQual é o seu ano de nascimento?\033[m '))
# Idade recebe ANO ATUAL - ANO DE NASCIMENTO
idade = date.today().year - ano
# Se idade for menor do que 18 anos
if idade < 18:
    tempo = 18 - idade
    print(f'\033[36mVocê ainda tem \033[37m{idade} ano(s) \033[36me vai se alistar em \033[37m{tempo} ano(s)')
# Se idade for igual a 18 anos
elif idade == 18:
    print(f'\033[36mEstá na hora de se alistar. Você já tem \033[37m{idade} anos')
# Se a idade for maior do que 18 anos
elif idade > 18:
    tempo = idade - 18
    print(f'\033[36mJá passou \033[37m{tempo} ano(s) \033[36mdo tempo de se alistar. Você tem \033[37m{idade} anos.')