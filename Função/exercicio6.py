# Exercício 6: Função maximo
# Escreva uma função chamada maximo que receba dois números como argumentos e retorne o maior deles.
# Se os números forem iguais, pode retornar qualquer um dos dois.

# Dica: Use uma estrutura condicional dentro da função para comparar os dois números.

def maximo(x,z) : 

    if x > z : 
        return print(x),
    elif x < z:
        return print(z),
    elif z == x:
        return print("Os dois são iguais", x," e ",z),

maximo(7,9)