def limpar_tela():
    print('\033[H\033[J')

def introdução():
    print("Olá jovens pistoleiros, esse jogo vai funcionar da seguinte forma")
    input()
    limpar_tela()
    print("Cada jogador terá 3 escolhas sendo elas recarregar arma, desviar e atirar")
    input()
    limpar_tela()
    print("Cada jogador deve ter pelo menos uma munição para atirar no outro. cada jogador tem o total de 3 vidas")
    input()
    limpar_tela()


def vencedor(V1,V2):
    if V1 <= 0 and V2 <= 0:
        print("Os dois deram tudo de si porém ambos morrem ali")
        return True
    elif V1 <= 0:
        print("Jonas ganha o duelo")
        return True
    elif V2 <= 0:
        print("Fernanda ganha o duelo")
        return True




    
