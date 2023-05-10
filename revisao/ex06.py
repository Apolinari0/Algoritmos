#Em um script, o usuário deve responder à pergunta “Continuar (s/n)?”. Se o
#usuário digitar ‘s’ ou ‘S’, o script deve retornar a mensagem “OK,
#continuando...”. Se o usuário digitar ‘n’ ou ‘N’, o script deve retornar a
#mensagem “OK, parando...”. Por fim, se o usuário digitar qualquer outra coisa,
#o script deve retornar uma mensagem de erro.

s = input("Continuar (s/n)?\n")
while True:
    if s.lower() == 's':
        s = input("Continuar (s/n)?\n")
    elif s.lower() == 'n':
        print("OK, parando...\n")
        break
    else:
        print ("Erro...\n")
        s = input("Continuar (s/n)?\n")

  