#Escreva um script chamado “belamatematica” que, quando executado, faz as
#operações matemáticas necessárias e exibe o seguinte na tela:

c=1

for i in range(1,10):
  print(f'{c} * 8 + {i} = {c*8+i}')
  c = c * 10 + i + 1