#Faça um programa que leia o nome RA e média final de
#uma aluno. Armazene todas as informações num
#dicionário. No final programa deve imprimir as
#informações do dicionário e situação do aluno
#(reprovado, exame ou aprovado). Utilize as regras da
#UNIFESP para definir a situação do aluno.

aluno = {}

aluno['nome']=str(input("Nome: "))
aluno['RA']=int(input('RA: '))
aluno['media']=float(input('media: '))

if aluno['media'] < 3:
  aluno['situação'] = "reprovado"
  print('Aluno reprovado diretamente')
elif aluno['media'] > 3 and aluno['media'] < 6:
  aluno['situação'] = 'exame'
  print('Aluno deverá fazer exame')
else:
  aluno['situação'] = "aprovado"
  print("Aluno aprovado diretamente")
  