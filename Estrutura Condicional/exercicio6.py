# Exercício 2: Imprimindo Números Pares
# Use um loop for para imprimir todos os números pares de 0 até um número fornecido pelo usuário. 
# Aqui, você pratica o uso de for junto com uma condição if para filtrar números pares.


number = int(input("Me diga um número: "))

for number in range(0, (number+1)): 
    if number % 2 == 0:
        print(number)

