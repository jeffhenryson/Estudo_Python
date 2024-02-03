# Exercício 9: Ordenação Personalizada
# Considere a lista palavras = ["banana", "pera", "maçã", "cereja"]. Ordene esta lista pelo 
# comprimento das palavras, do menor para o maior, e imprima a lista ordenada.

palavras = ["banana", "pera", "maçã", "cereja"]
palavras.sort(key=len)  # Ordena as palavras pelo comprimento
print(palavras)

