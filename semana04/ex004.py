#Crie um programa que gerencia o aproveitamento de um
#jogador de futebol. o programa vai ler o nome do
#jogador e quantas partidas ele jogou. Depois vai ler a
#quantidade de gols feitos em cada partida. No final, tudo
#isso será guardado em um dicionário incluindo o total de
#gols realizados durante o campeonato

jogador = {}
partidas = list()
##pega nome e qntd de jogos
jogador['Nome'] = str(input("Nome: "))
QtdJogos = int(input("Qtd de jogos: "))

#pela qtd de jogos, roda um for pegando os gols
for i in range(QtdJogos):
  partidas.append(int(input(f'Quantidade de gols na partida {i+1}:')))

total = sum(partidas)
#transfere lista partidas com os gols para o dict jogador
jogador['gols'] = partidas[:]
jogador['total'] = total
print('*'*30)

#mostra partida -> gols
for i, j in enumerate(jogador['gols']):
  print(f"partida {i+1} - {j} gols")

#total de gols com o nome
print(f"total de gols do jogador {jogador['Nome']}: {total}")

print('*'*30)