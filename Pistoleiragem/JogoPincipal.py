import functs
import time
import random
import personagens

functs.limpar_tela()

P1 = personagens.personagem("Fernanda",3,1)
P2 = personagens.personagem("Jonas",3,1)

vez = "Fernanda"
rodada = 1
distancia = "perto"

#Mensagem de inicio do jogo
functs.introdução()
while(True):
    if vez == "Fernanda":
        functs.limpar_tela()
        sair = functs.vencedor(P1.vida,P2.vida)
        if sair:
            break
        print("\tRodada "+str(rodada))
        rodada+=1

        P1.desativar()
        P2.desativar()

        time.sleep(1.5)

    if vez == "Fernanda":
        P1.escolha = True
        while(P1.escolha):
            functs.limpar_tela()
            print("Vez de Fernanda\n\nVocê tem: vida "+str(P1.vida)+" Munição "+str(P1.bulet))
            acao = input("Escolha entre Recarregar, Atirar ou Desviar(R,A,D) ")

            P1.ação(acao)
        vez = "Jonas"
    else :
        P2.escolha = True
        while(P2.escolha):
            functs.limpar_tela()
            print("Vez de Jonas\n\nVocê tem vida: "+str(P2.vida)+" Munição "+str(P2.bulet))
            acao = input("Escolha entre Recarregar, Atirar ou Desviar(R,A,D) ")

            P2.ação(acao)
        vez = "Fernanda"

        functs.limpar_tela()

        P1.acerto(P1,P2)
        P2.acerto(P2,P1)

        P1.desvio_carga(P1,P2)
        P2.desvio_carga(P2,P1)

        time.sleep(3)
time.sleep(3)
        

