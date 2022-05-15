# variaveis que contém as quantidades de cada cedulas
# feito em conjunto com todo o grupo
nQuantidadeCedulas = 7000
nDuzentos = 1000
nCem = 1000
nCinquenta = 1000
nVinte = 1000
nDez = 1000
nCinco = 1000
nDois = 1000

# variavel que contém a quantide de notas que a pessoa vai receber
# feito em cunjunto com todo grupo
nSaqueDuzentos = 0
nSaqueCem = 0
nSaqueCinquenta = 0
nSaqueVinte = 0
nSaqueDez = 0
nSaqueCinco = 0
nSaqueDois = 0

# variável que contém a quantidade de depósitos feitos
# feito pelo Gustavo
nDeposito = 0

# variável que contém a quantidade total de dinheiro depositado
# feito pelo Gustavo
nTotalDeposito  = 0

# vairável que contém a senha de administrador padrão
#feito pelo Gustavo
sLoginPadrao = 'Admin'
sSenhaPadrao = '0000'

# variável que contém a quantidade de vezes que foram retirados os depósitos feitos 
# feito pelo Gustavo
nRetirada = 0

# variável que contém a quantidade de vezes que foi abastecido
# feito pelo Gustavo
nAbestecimento = 0

# variável que contém o que vai ser feito no caixa
# feito pelo Gustavo
nFuncao = int(input("Digite 0 para sair \nDigite 1 para  sacar \nDigite 2 para depositar \nDigite 3 para fazer login como administrador \n"))

# laço de repetição para saber quantas vezes vai ser sacado dinheiro
# feito pelo gustavo
while nFuncao != 0:

    # teste para saber o que vai ser feito no caixa
    # feito pelo Gustavo
    if nFuncao == 1:

        # bloco de código que oferece q meno quantidade de notas possível
        # feito em conjunto pelo grupo
        nSaque = int(input("\nInforme o valor que você quer sacar: "))
        while nSaque >= 200:
            nSaqueDuzentos += 1
            nSaque = nSaque - 200
            nQuantidadeCedulas = nQuantidadeCedulas - 200
            nDuzentos = nDuzentos - 200

        while nSaque >= 100:
            nSaqueCem += 1
            nSaque = nSaque - 100
            nQuantidadeCedulas = nQuantidadeCedulas - 100
            nCem = nCem - 100

        while nSaque >= 50:
            nSaqueCinquenta += 1
            nSaque = nSaque - 50
            nQuantidadeCedulas = nQuantidadeCedulas - 50
            nCinquenta = nCinquenta - 50

        while nSaque >= 20:
            nSaqueVinte += 1
            nSaque = nSaque - 20
            nQuantidadeCedulas = nQuantidadeCedulas - 20
            nVinte =nVinte - 20

        while nSaque >= 10:
            nSaqueDez += 1
            nSaque = nSaque - 10
            nQuantidadeCedulas = nQuantidadeCedulas - 10
            nDez = nDez - 10

        while nSaque >= 5:
            nSaqueCinco += 1
            nSaque = nSaque - 5
            nQuantidadeCedulas = nQuantidadeCedulas - 5
            nCinco = nCinco - 5

        while nSaque >= 2:
            nSaqueDois += 1
            nSaque = nSaque - 2
            nQuantidadeCedulas = nQuantidadeCedulas - 2
            nDois = nDois - 2

        if nSaque == 1:
            print("Não conseguiremos entregar o valor pedido, por isso receberá o valor aproximado")
        
        print('\nNotas de duzentos a receber:', nSaqueDuzentos, 
        '\nNotas de cem a receber:', nSaqueCem, 
        '\nNotas de cinquenta a receber:', nSaqueCinquenta, 
        '\nNotas de vinte a receber:', nSaqueVinte, 
        '\nNotas de dez a receber: ', nSaqueDez, 
        '\nNotas de cinco a receber:', nSaqueCinco, 
        '\nNotas de dois a receber', nSaqueDois, "\n")

    elif nFuncao == 2:
        nDeposito = int(input("Informe a quantidade que você quer depositar: "))
    elif nFuncao == 3:
        sLogin = input("Informe o o login: ")
        sSenha = input("Informe a senha: ")

        if sLogin == sLoginPadrao and sSenha == sSenhaPadrao:
            nFunc2 = int(input(" Digite \0 para sair nDigite 1 para  receber as informações gerias \nDigite 2 para repor cédulas \nDigite para retirar envelopes de depósito \n"))
            while nFunc2 != 0:
                if nFunc2 == 1:
                    print("Infos gerais\n")
                    print("Ainda tem", nQuantidadeCedulas, "notas no caixa, sendo elas:")
                    print(nDuzentos, "notas de duznetos reais;")
                    print(nCem, "notas de cem reais")
                    print(nCinquenta, "notas de Cinquenta reais")
                    print(nVinte, "notas de vinte reais")
                    print(nDez, "notas de dez reais")
                    print(nCinco, "notas de cinco reais")
                    print(nDois, "notas de dois reais")
                    print("\n Foram retidados", (7000 - nQuantidadeCedulas), "notas sendo a seguinte quantidade de notas para cada valor")
                    print((1000 - nDuzentos), "notas de duznetos reais;")
                    print((1000 - nCem), "notas de cem reais")
                    print((1000 - nCinquenta), "notas de Cinquenta reais")
                    print((1000 - nVinte), "notas de vinte reais")
                    print((1000 - nDez), "notas de dez reais")
                    print((1000 - nCinco), "notas de cinco reais")
                    print((1000 - nDois), "notas de dois reais")
                    print("Totalizando", ((1000 - nDuzentos) * 200) + ((1000 - nCem) * 100) + (1000 - nCinquenta) + ((1000 - nVinte) * 20) + ((1000 - nDez) * 10) + ((1000 - nCinco) * 5) + ((1000 - nDois) * 2))
                    print("\nForam relizados", nDeposito, "depoistosm totalizando", nTotalDeposito)
                    print("\nForam realizados", nAbestecimento, "reabastecimentos")
                    print("\nFOram realizados", nRetirada, "retiradas de depósitos")
                elif nFunc2 == 2:
                    print("Repondo cédulas")
                    print("Informe quanto de cada cédula foi reposto")
                    nAux200 = int(input("200: "))
                    nAux100 = int(input("100: "))
                    nAux50 = int(input("50: "))
                    nAux20 = int(input("20: "))
                    nAux10 = int(input("10: "))
                    nAux5 = int(input("5: "))
                    nAux2 = int(input("2: "))

                    if (nAux200 + nDuzentos) > 1000 and (nAux100 + nCem) > 1000 and (nAux50 + nCinquenta) > 1000 and (nAux20 + nVinte) > 1000 and (nAux10 + nDez) > 1000 and (nAux5 + nCinco) > 1000 and (nAux2 + nDois) > 1000:
                        print("Não é possível repor essa quantidade de cédulas")
                    else:
                        nDuzentos += nAux200
                        nCem += nAux100
                        nCinquenta += nAux50
                        nVinte += nAux20
                        nDez += nAux10
                        nCinco += nAux5
                        nDois += nAux2

                        nQuantidadeCedulas = (nDuzentos + nCem + nCinquenta + nVinte + nDez + nCinco + nDois)
                elif nFunc2 == 3:
                    print("Retirando os depósitos feitos")
    else:
        print("Escolha uma função:")
    nFuncao = int(input("Digite 0 para sair \nDigite 1 para  sacar \nDigite 2 para depositar \nDigite 3 para fazer login como administrador: \n"))