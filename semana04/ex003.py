#Crie um programa que leia o nome, ano de nascimento e
#carteira de trabalho e cadastre-os com idade em um
#dicionario. se por acaso a CTPS for diferente de zero o
#dicionario recebera tambem o ano de contratação e
#salario. Calculo e acrescente além da didade, com
#quantos anos a pessoa vai se aposentar.


pessoa = {}

pessoa['Nome'] = str(input('Nome:'))
nasc= int(input("Ano de nascimento:"))
pessoa['idade'] = 2023 - nasc
pessoa['ctps'] = int(input("Carteira de trabalho: (digite 0 caso nao tenha):"))
if pessoa['ctps'] != 0:
  pessoa['contrato'] = int(input('ano de contratação:'))
  pessoa['salario'] = float(input('salario:'))
  pessoa['aposentadoria'] = pessoa['idade'] +((pessoa['contrato'] + 35) - 2023)

print('*'*30)
print(pessoa)