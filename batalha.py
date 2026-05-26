import dialogos
import time


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
            statsInimigo = self.scaledInimigos(inimigo)
            self.printer_local(f"--- UM {statsInimigo["Nome"]} apareceu! Ele possui {statsInimigo["Vida"]} de vida e {statsInimigo["Dano"]} de ataque!")
            print(f"Esse é a sua primeira batalha, ela é divida em turnos! Cada turno que passar você ganhara 1 de energia")
            while True:
                self.playerStats["Energia"]+=1
                statsInimigo["Energia"]+=1
                self.printer_local(f"""Turno:{turno}\nVocê possui {self.playerStats["Vida"]} / {self.playerStats["VidaMax"]} de Vida e {self.playerStats["Energia"]} de energia\
                      \nO {statsInimigo['Nome']} possui {statsInimigo["Vida"]} de vida""")
                TipoAtk, Dano = self.IaInimigos(inimigo)
                self.printer_local(f"Seu inimigo irá usar um {TipoAtk} e dara {Dano}, como você reagirá?\n[1]Ataque leve\n[2]Ataque pesado (2 Energia) \n[3]Defesa")
                escolha, DanoPlr = self.ChecarAtaque(input(">"))
                match escolha:
                    case "Ataque leve":
                        pass
                    case "Ataque Pesado":
                        pass
                    case "Defesa":
                        pass

                
    def IaInimigos(self,Inimigo):
        if Inimigo == "EsqueletoTutorial":
            return "Ataque Fraco",1


    def ChecarAtaque(self,Escolha):
        while True:
            if int(Escolha.lower().strip()) not in [1,2,3]:
                self.printer_local("Digite 1,2 ou 3")
                Escolha = input(">")
            elif Escolha == 2 and not self.playerStats["Energia"] >= 2:
                self.printer_local("Você não possui 2 de energia")
                Escolha = input(">")
            else:
                break
        match Escolha:
            case 1:
                return "Ataque leve"
            case 2:
                return "Ataque Pesado"
            case 3:
                return "Defesa"


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
