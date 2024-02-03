# Exercício 1: Adivinhe o Número
# Vamos fazer um jogo simples de adivinhação de número. O programa escolherá um número aleatório entre 1 e 10, e o usuário terá que adivinhar qual é. 
# Usaremos um loop while para permitir várias tentativas até que o usuário acerte o número.

import random


numberTarget = random.randint(1, 10)

numberChosen = int(input("Escolha um numero de 1 a 10: "))

win = False  

while win == False :

    if numberChosen != numberTarget : 
        numberChosen = int(input("Escolha outro número: "))
        win = False
    elif numberChosen == numberTarget : 
        print("Você acertou!! O número escolhido foi ", numberTarget)
        win = True
    else :
        print("error")
