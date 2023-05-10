#Em química, o pH de uma solução aquosa é uma medida da sua acidez.Os
#Valores de pH variam entre 0 e 14. Soluções ácidas tem pH maior que 7.
#Soluções básicas tem pH menor que 7. Soluções neutras tem pH igual a 7.
#Escreva duas funções que recebem um número correspondente ao pH de uma
#solução aquosa e exibem na tela o tipo de solução (algo como “A solução é
#ácida”).

pH = int(input("Informe um valor de pH: "))
if pH > 0 and pH < 7:
  print(f'o pH informado {pH} é acido.')
elif pH > 7 and pH < 14:
  print(f'o pH informado {pH} é basico.')
else:
  print(f'o pH informado {pH} é neutro.')