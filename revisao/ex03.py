#Escreva um script que leia a quantidade de dias,horas,
#minutos e segundos para o usuário. Calcule o total em
#segundos.

dias = int(input('Digite quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

total = dias * 24 * 3600 + horas * 3600 + minutos*60 + segundos

print(f'total em segundos: {total}')