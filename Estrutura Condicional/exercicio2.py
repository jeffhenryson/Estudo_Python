# Modifique o programa de número positivo/negativo/zero para também verificar se o número é par ou ímpar.


numero = float(input("Digite um número: "))

if numero > 0 and numero % 2 == 0:
    print("O número é positivo e par.")
elif  numero > 0 and numero % 2 != 0:
    print("O número é positivo e impar.")
elif  numero < 0 and numero % 2 == 0:
    print("O número é negativo e par.")
elif  numero < 0 and numero % 2 != 0:
    print("O número é negativo e impar.")
elif numero == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")
