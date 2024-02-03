# Exercício 3: Menu Simples
# Crie um menu simples que repete até que o usuário escolha sair. Use um loop while com condições if para lidar com a escolha do usuário.

closeAplication = False

def soma(a,b) : 
    return a + b;

def sub(a,b):
    return a - b;

def div(a, b):
    return a / b;

def mult(a,b) : 
    return a * b;


while closeAplication == False : 

    print("1.Soma ")
    print("2.Subtração ")
    print("3.Divisão ") 
    print("4.multiplicação ")
    print("5.Sair ")
    userOption = int(input("Escolha o que você quer fazer: "))

    if userOption == 1 : 
        firstNumber = int(input("Escolha o primeiro número: "))
        secondNumber = int(input("Escolha o segundo número: "))
        finalSoma = soma(firstNumber,secondNumber)
        print("A soma dos valores é: ", finalSoma)
    elif userOption == 2 :
        firstNumber = int(input("Escolha o primeiro número: "))
        secondNumber = int(input("Escolha o segundo número: "))
        finalSub = sub(firstNumber,secondNumber)
        print("A soma dos valores é: ", finalSub)
    elif userOption == 3 :
        firstNumber = int(input("Escolha o primeiro número: "))
        secondNumber = int(input("Escolha o segundo número: "))
        finalDiv = div(firstNumber,secondNumber)
        print("A divisão dos valores é: ", finalDiv)
    elif userOption == 4 :
        firstNumber = int(input("Escolha o primeiro número: "))
        secondNumber = int(input("Escolha o segundo número: "))
        finalMult = mult(firstNumber,secondNumber)
        print("A multiplicação dos valores é: ", finalMult)
    elif userOption == 5 :
        print("Saindo....")
        closeAplication = True
    else : 
        print("Opção inválida. Tente novamente outro número:")
