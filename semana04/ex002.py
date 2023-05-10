#Crie um programa que leia nome, sexo, peso e altura de
#várias pessoas. guarde os dados de cada pessoa num
#dicionário individual e acrescente o IMC da pessoa.
#Organize todos os dicionários em uma lista. No final
#mostre
#a. Quantas pessoas foram cadastradas
#b. Qual é o peso médio das pessoas
#c. Qual é a altura média das pessoas
#d. Qual é IMC médio das pessoas

#dictionario pessoas
pessoa = {}
pessoas=[]
#conta quantidade de pessoa cadastrada
contP = 0
pesoM = 0
alturaM = 0
imcM = 0
validador = 's'

while validador != 'N':
  pessoa['nome'] = str(input("Nome: "))
  pessoa['sexo'] = str(input('Sexo: ')).upper()
  pessoa['peso'] = float(input("Peso: "))
  pessoa['altura'] = float(input("Altura: "))
  pessoa['IMC'] = pessoa['peso'] / pessoa['altura']**2
  contP += 1
  pesoM += pessoa['peso'] / contP
  alturaM = pessoa['altura'] / contP
  imcM = pessoa['IMC'] / contP
  
  #passa para uma lista separadamente
  pessoas.append(pessoa.copy())
  #valida se conitinua cadastrando ou nao
  validador = str(input("Deseja continuar? S/N")).upper()

print('='*10)

for i, j  in enumerate(pessoas):
  print(f'{i+1} - {j}')


print(f'Foi cadastrado {contP} pessoas, tendo Peso médio de {pesoM}, altura media de {alturaM} e imc medio de {imcM}')
