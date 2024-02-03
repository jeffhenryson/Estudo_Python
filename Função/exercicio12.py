# Exercício 12: Função para Verificar Palíndromos
# Escreva uma função e_palindromo que verifique se uma string é um palíndromo 
# (uma palavra que é lida igualmente de trás para frente), retornando True se for
# um palíndromo e False caso contrário. Ignore diferenças de maiúsculas e minúsculas e espaços.

def e_palindromo(str) : 
    if str == str[::-1] :
        return "é palíndromo"
    else:
        return ("Não é palíndromo: ", str ,str[::-1])
    
print(e_palindromo("amar"))

