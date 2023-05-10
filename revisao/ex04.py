#Faça um script que calcule o aumento de salário. Ele deve
#solicitar o valor do salário e a porcentagem de aumento.
#Exiba o valor do aumento e do novo salário.


salario =  float(input('Digite o salário: '))
aumento = float(input('Percentual de aumento: '))

newSal = salario * (aumento/100)

print(f'Seu salário atual:{salario}. Com {aumento} % de aumento:{newSal}')