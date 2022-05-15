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

# variável que contém a quantidade de dinheiro que foi depositado 
# feito pelo Gustavo
nDeposito = 0

# variável que contém a quantidade de vezes que foi retirado os depósitos feitos 
# feito pelo Gustavo
nRetirada = 0

# variável que contém a quantidade de vezes que foi abastecido
# feito pelo Gustavo
nAbestecimento = 0

# variável que contém o que vai ser feito no caixa
# feito pelo Gustavo
nFuncao = int(input("Digite 1 para  sacar \nDigite 2 para depositar \nDigite 3 para fazer login como administrador: \n"))

# teste para saber o que vai ser feito no caixa
# feito pelo Gustavo
if nFuncao == 1:

    # bloco de código que oferece q meno quantidade de notas possível
    # feito em conjunto pelo grupo
    nSaque = int(input("Informe o valor que você quer sacar: "))
    while nSaque >= 200:
        nSaqueDuzentos += 1
        nSaque = nSaque - 200
    while nSaque >= 100:
        nSaqueCem += 1
        nSaque = nSaque - 100
    while nSaque >= 50:
        nSaqueCinquenta += 1
        nSaque = nSaque - 50
    while nSaque >= 20:
        nSaqueVinte += 1
        nSaque = nSaque - 20
    while nSaque >= 10:
        nSaqueDez += 1
        nSaque = nSaque - 10
    while nSaque >= 5:
        nSaqueCinco += 1
        nSaque = nSaque - 5
    while nSaque >= 2:
        nSaqueDois += 1
        nSaque = nSaque - 2
    
    print('\nNotas de duzentos a receber:', nSaqueDuzentos, 
    '\nNotas de cem a receber:', nSaqueCem, 
    '\nNotas de cinquenta a receber:', nSaqueCinquenta, 
    '\nNotas de vinte a receber:', nSaqueVinte, 
    '\nNotas de dez a receber: ', nSaqueDez, 
    '\nNotas de cinco a receber:', nSaqueCinco, 
    '\nNotas de dois a receber', nSaqueDois )

elif nFuncao == 2:
    nDeposito = int(input("Informe a quantidade que você quer depositar: "))
elif nFuncao == 3:
    sLogin = input("Informe o o login: ")
    sSenha = input("Informe a senha: ")
else:
    print("Escolha uma função:")