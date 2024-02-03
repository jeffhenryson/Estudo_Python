# Exercício 12: Clonando Listas
# Dada a lista original = [10, 22, 44, 23, 4], crie uma cópia dela chamada copia de 
# modo que modificar copia não afete original. Demonstre isso modificando copia e imprimindo
# ambas as listas.

original = [10, 22, 44, 23, 4]
copia = original.copy()  # Ou copia = original[:]

copia[0] = 99  # Modifica a cópia

print(original)  # Imprime a lista original não modificada
print(copia)  # Imprime a cópia modificada
