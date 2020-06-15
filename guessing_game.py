from random import randint
from time import sleep
from termcolor import colored

print(colored('-=-', 'yellow') * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(colored('-=-', 'yellow')* 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar

print(colored('Processando...', 'red'))
sleep(2)
computador = randint(1, 5) # Faz o computador escolher o número de 1 até 5

if jogador == computador:
    print(colored('PARABÉNS!Você conseguiu me vencer!', 'blue'))
else:
    print('GANHEI! Eu pensei no número {} e você no {}!'.format(computador, jogador))
