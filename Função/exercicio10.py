# Exercício 10: Função de Máximo em Lista
# Crie uma função chamada maximo_lista que receba uma lista de números 
# como argumento e retorne o maior número da lista. Não utilize a função 
# max() do Python para este exercício.

def maximo_lista(lista_numeros):
    if not lista_numeros:
        return None
    maximo = lista_numeros[0]
    for numero in lista_numeros[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

lista_de_numeros = [3, 5, 1, 2, 7, 0, -1, 7]
print(maximo_lista(lista_de_numeros))
