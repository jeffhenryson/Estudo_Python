# Exercício 5: Contando Letras
# Crie uma função contar_letras que receba uma string e retorne o número de letras na string.
# Dica: use a função integrada str.isalpha() para verificar se um caractere é uma letra.
    
def contar_letras(palavra):
    contador = 0
    for letra in palavra:  # Itera diretamente sobre cada caractere na string
        if letra.isalpha():  # Verifica se o caractere é uma letra
            contador += 1
    return contador  # Retorna o contador após iterar por toda a string
