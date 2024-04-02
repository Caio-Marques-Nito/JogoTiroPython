import functs
import time
import random

class personagem():
    nome = ""
    vida = 3
    bulet = 0
    desvio = False
    tiro = False
    recarga = False
    dano = 1
    escolha = True
    Nbullets = 2

    def __init__(self,nome,vida,dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano
    
    def desativar(self):
        self.desvio = False
        self.tiro = False
        self.recarga = False
    
    def ação(self,letra):
        if letra == "R":
            self.bulet+=self.Nbullets
            self.recarga = True
            self.escolha = False
        elif letra == "D":
            self.desvio = True
            self.escolha =False
        elif letra == "A":
            if self.bulet > 0:
                self.tiro = True
                self.bulet-=1
                self.escolha = False
            else:
                functs.limpar_tela()
                print("Você não tem balas para atirar")
                time.sleep(2)
        else:
            functs.limpar_tela()
            print("Isso não está nas opções")
            time.sleep(2)

    def acerto(self,PP,PB):
        if PP.tiro == True:
            aleatorio = random.randint(0,100)
            if aleatorio <= 80:
                PB.vida-=PP.dano
                print(PP.nome+" atirou")
            else:
                print(PP.nome+" errou o tiro")
                PP.tiro = False
    
    def desvio_carga(self,PP,PB):
        if PP.desvio== True:
            print(PP.nome+" desviou")
            if PB.tiro == True:
                PP.vida+=PB.dano
        elif PP.recarga == True:
            print(PP.nome+" carregou "+str(self.Nbullets)+" balas")



    
    


