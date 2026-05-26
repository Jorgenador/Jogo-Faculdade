import dialogos
import time
import colorama

class Batalhas:

    def __init__(self):
        self.playerStats = {
            "Nome":"",
            "Sala":0,
            "VidaMax":100,
            "Vida":100,
            "Ataque":5,
            "Gold":0,
            "Energia":0
        }

    def printer_local(self,texto):
        for char in texto:
            print(char,end="",flush=True)
            time.sleep(0.01)
        print("")

    def iniciar_batalha(self):
        if self.playerStats["Sala"] == 0:
            self.printer_local(f"""Você possui {self.playerStats["Vida"]} de vida e {self.playerStats["Ataque"]} de Ataque.
Já que este esqueleto é bem fraco, vamos aprender os controles... 
[1] Para atacar
[2] Para ataque forte (Consome 2 de energia, você gera 1 por turno)
[3] Para defender! (Bloqueia completamente o dano de Ataques fracos e reduz pela metade o resto)
Vamos iniciar o primeiro turno!""")
            self.loop_batalha("EsqueletoTutorial")
        else:
            print("BLALBLALBLA")

    def loop_batalha(self,inimigo):
        turno = 0
        if inimigo == "EsqueletoTutorial":
            self.printer_local(f"Esse é a sua primeira batalha, ela é divida em turnos! Cada turno que passar você ganhara 1 de energia")
        statsInimigo = self.scaledInimigos(inimigo)
        self.printer_local(f"--- UM {statsInimigo["Nome"]} apareceu! Ele possui {statsInimigo["Vida"]} de vida e {statsInimigo["Dano"]} de ataque!")
        while True:
            self.playerStats["Energia"]+=1
            statsInimigo["Energia"]+=1
            self.printer_local(f"""Turno:{turno}\nVocê possui {self.playerStats["Vida"]} / {self.playerStats["VidaMax"]} de Vida e {self.playerStats["Energia"]} de energia\
                    \nO {statsInimigo['Nome']} possui {statsInimigo["Vida"]} de vida""")
            ETipoAtk, EDano = self.IaInimigos(inimigo)
            self.printer_local(f"Seu inimigo irá usar um {ETipoAtk} e dara {EDano}, como você reagirá?\n[1]Ataque leve\n[2]Ataque pesado (2 Energia) \n[3]Defesa")
            escolha, DanoPlr = self.ChecarAtaque(input(">"))
            print(escolha)
            match escolha:
                case "Ataque leve" | "Ataque pesado":
                    statsInimigo["Vida"] -= DanoPlr
                    self.playerStats["Vida"] -= EDano
                    self.printer_local(f"Você ataca o inimigo com um {escolha}, tirando {DanoPlr} de vida!\n>Ele reage com um {ETipoAtk} te causando {EDano} de dano...")
                case "Defesa":
                    if ETipoAtk == "Ataque Fraco":
                        self.printer_local("Você defendeu um ataque fraco completamente")
                    else:
                        DDano = EDano * 0.5
                        self.playerStats["Vida"] -= DDano
                        self.printer_local(f"Você defendeu um ataque, recebeu {DDano} de dano! 50% de defesa!")
            if statsInimigo["Vida"] <= 0 or self.playerStats["Vida"] <= 0:
                break
            turno+=1
        if statsInimigo["Vida"] <= 0:
            self.printer_local(f"Você ganhou!! Você possui {self.playerStats["Vida"]} de vida. Vamos para a escolha da sua proxima sala!")
        elif self.playerStats["Vida"] <= 0:
            self.printer_local("Você perdeu... acho que foi falta de habilidade...")

                
    def IaInimigos(self,Inimigo):
        if Inimigo == "EsqueletoTutorial":
            return "Ataque Fraco",1


    def ChecarAtaque(self,Escolha):
        while True:
            if int(Escolha.lower().strip()) not in [1,2,3]:
                self.printer_local("Digite 1,2 ou 3")
                Escolha = input(">")
            elif int(Escolha) == 2 and not self.playerStats["Energia"] >= 2:
                self.printer_local("Você não possui 2 de energia. Escolha outra ação!")
                Escolha = input(">")
            else:
                break
        match int(Escolha):
            case 1:
                return "Ataque leve",self.playerStats["Ataque"]
            case 2:
                self.playerStats["Energia"]-=2
                return "Ataque pesado",self.playerStats["Ataque"]*2
            case 3:
                return "Defesa",0


    def scaledInimigos(self,inimigo):
        sala = self.playerStats["Sala"]
        Inimigos = {
            "EsqueletoTutorial":{
                "Nome": "Esqueleto",
                "Vida":20 + (sala * 2),
                "Dano": 1 + (sala * .5),
                "Energia": 0,
            }
        }
        return Inimigos[inimigo]
