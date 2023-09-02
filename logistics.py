def dimensoesObjeto():
    print("---------- Menu 1 de 3 // Dimensão do Objeto ----------")
    while True:
        try:
            comprimento = int(input("Digite o comprimento do objeto (em cm): "))
            largura = int(input("Digite a largura do objeto (em cm): "))
            altura = int(input("Digite a altura do objeto (em cm): "))
            volume = comprimento * largura * altura
            print("O volume do objeto é : {:.1f}cm³".format(volume))
            if volume < 1000:
                return 10
            if (volume >= 1000) and (volume <= 10000):
                return 20
            if (volume >= 10000) and (volume <= 30000):
                return 30
            if (volume >= 30000) and (volume <= 100000):
                return 50
            else:
                print("Não aceitamos objetos com dimensões muito grandes!")
        except ValueError: #caso o usuário não digite um valor número inteiro
            print("Você digitou alguma dimensão do objeto com um valor não numérico!\nPor favor entre com as dimensões desejadas novamente.")
#Fim do menu de dimensões do objeto

#Início do menu de pesos do objeto
def pesoObjeto():
    print("---------- Menu 2 de 3 // Peso do Objeto ----------")
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            print("O peso do seu objeto é: {}kg".format(peso))
            if peso <= 0.1:
                return 1.00
            elif (peso > 0.1) and (peso < 1):
                return 1.50
            elif (peso >= 1) and (peso < 10):
                return 2
            elif (peso >= 10) and (peso < 30):
                return 3
            else:
                print("Não aceitamos objetos tão pesados.")
        except ValueError:
            print("Você digitou o peso do objeto com um valor não numérico!")
#Fim do menu de pesos do objeto

#Início do menu de rotas do objeto
def rotaObjeto():
    print("---------- Menu 3 de 3 // Rota do Objeto ----------")
    while True:
            rota = input("Selecione a rota:\n" +
                        "RS - De Rio de Janeiro até São Paulo\n" +
                        "SR - De São Paulo até Rio de Janeiro\n" +
                        "BS - De Brasília até São Paulo\n" +
                        "SB - De São Paulo até Brasília\n" +
                        "BR - De Brasília até Rio de Janeiro\n" +
                        "RB - Rio de Janeiro até Brasília\n" 
                        ">> ")
            rota = rota.upper()
            if rota == "RS":
                return 1
            if rota == "SR":
                return 1
            if rota == "BS":
                return 1.2
            if rota == "SB":
                return 1.2
            if rota == "BR":
                return 1.5
            if rota == "RB":
                return 1.5
            else:
                print("Você digitou uma rota que não existe!")
#Início do menu de rotas do objeto

#Início do main
print("---------- Bem-vindo a Companhia de Logística Paulo Eduardo! ---------- ")
volume = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = volume * peso * rota
print("Total a pagar (R$): {:.2f} (Volume: {} * Peso: {} * Rota: {})".format(total, volume, peso, rota))
#Fim do main
