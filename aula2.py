nQuantidadeCedulas = 7000
nDuzentos = 1000
nCem = 1000
nCinquenta = 1000
nVinte = 1000
nDez = 1000
nCinco = 1000
nDois = 1000

nSaqueDuzentos = 0
nSaqueCem = 0
nSaqueCinquenta = 0
nSaqueVinte = 0
nSaqueDez = 0
nSaqueCinco = 0
nSaqueDois = 0

nSaque = int(input("Informe o valor que você quer sacar: "))

while nSaque > 200:
    nSaqueDuzentos += 1
    nSaque = nSaque - 200
if nSaque < 100:
    nSaqueCem += 1
    nSaque = nSaque - 100
if nSaque > 50:
    nSaqueCinquenta += 1
    nSaque = nSaque - 50
if nSaque > 20:
    nSaqueVinte += 1
    nSaque = nSaque - 20
if nSaque > 10:
    nSaqueDez += 1
    nSaque = nSaque - 10
if nSaque > 5:
    nSaqueCinco += 1
    nSaque = nSaque - 5
if nSaque > 2:
    nSaqueDois += 1
    nSaque = nSaque - 2

print('Notas de duzentos a receber:', nSaqueDuzentos, 'Notas de cem a receber:', nSaqueCem, 'Notas de cinquenta a receber:', nSaqueCinquenta, 'Notas de vinte a receber:', nSaqueVinte, 'Notas de dez a receber: ', nSaqueDez, 'Notas de cinco a receber:', nSaqueCinco, 'Notas de dois a receber', nSaqueDois )