#Escreva um programa que solicite ao usuário uma lista de números e exiba o
#segundo maior número da lista, utilizando um loop.

lista = []
n = int(input("Digite a quantidade de números que deseja informar: "))
for i in range(n):
    lista.append(int(input("Digite um número: ")))
  
maior = lista[0]
segundo_maior = lista[0]

for i in lista:
    if i > maior:
        segundo_maior = maior
        maior = i
    elif i > segundo_maior and i != maior:
        segundo_maior = i
        
print("O segundo maior número é:", segundo_maior)
