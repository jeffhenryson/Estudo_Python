# Exercício 4: Substituição de Elementos
# Considere a lista temperaturas = [22, 20, 19, 23, 24]. O sensor de temperatura registrou
# erroneamente 19 no terceiro dia; o valor correto era 21. Substitua o valor incorreto pelo
# correto e imprima a lista modificada.

temperatura = [22,20,19,23,24]

temperatura.remove(19)
temperatura.insert(2,21)

print(temperatura)