# if condição:
#     # Executa este bloco se a condição for verdadeira
# elif outra_condição:
#     # Executa este bloco se a primeira condição for falsa e esta for verdadeira
# else:
#     # Executa este bloco se todas as condições acima forem falsas

numero = int(input("Me diga um número : "))

if numero > 0 : 
    print ( "esse numero é positivo!")
elif numero == 0 : 
    print ("O seu número é: 0")
elif numero < 0 : 
    print ("Esse número é negativo")
else :
    print ("error")