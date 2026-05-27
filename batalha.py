import time
import colorama
import random
import os
import loot
import sys

class Batalhas:

    def __init__(self):
        self.playerStats = {
            "Nome":"",
            "Sala":0,
            "VidaMax":100,
            "Vida":100,
            "Ataque":6,
            "Gold":0,
            "Energia":0
        }

    def printer_local(self,texto):
        for char in texto:
            print(char,end="",flush=True)
            time.sleep(0.0005)
        print("")

    def iniciar_batalha(self,Skip = False,dHandler=None,bHandler = None,Batalha = None):
        if bHandler != None: cbatalha = bHandler
        if dHandler != None: cdialogo = dHandler
        if self.playerStats["Sala"] == 0:
            if not Skip:
                self.printer_local(f"""Você possui {self.playerStats["Vida"]} de vida e {self.playerStats["Ataque"]} de Ataque.
Já que este esqueleto é bem fraco, vamos aprender os controles... 
[1] Para atacar
[2] Para ataque forte (Consome 2 de energia, você gera 1 por turno)
[3] Para defender! (Bloqueia completamente o dano de Ataques "Leves" e reduz pela metade o resto)
Você fica mais forte através de poções! A cada Batalha os inimigos podem deixar poções, Você pode comprar artefatos na loja e Poções na sala do tesouro!
Vamos iniciar o primeiro turno!""")
            self.loop_batalha("EsqueletoTutorial",dHandler = cdialogo,bHandler=cbatalha)
        else:
            inimigo = self.gerarInimigo(batalha=Batalha)
            self.loop_batalha(inimigo=inimigo,dHandler = cdialogo,bHandler=cbatalha)

    def loop_batalha(self,inimigo,dHandler = None,bHandler = None,stats = None):
        if bHandler != None: batalha = bHandler
        if dHandler != None: cdialogo = dHandler
        turno = 0
        self.playerStats["Energia"] = 0
        if inimigo == "EsqueletoTutorial":
                self.printer_local(f"Esse é a sua primeira batalha, ela é divida em turnos! Cada turno que passar você ganhara 1 de energia")
                statsInimigo = self.scaledInimigos(inimigo)
        else:
            statsInimigo = inimigo
        self.printer_local(f"Um {statsInimigo["Nome"]} apareceu! Ele possui "+colorama.Fore.LIGHTGREEN_EX+f"{statsInimigo["Vida"]} de Vida"+colorama.Fore.RESET+" e "+colorama.Fore.RED+f"{statsInimigo["Dano"]} de Ataque"+colorama.Fore.RED+"!"+colorama.Fore.RESET)
        while True:
            self.playerStats["Energia"]+=1
            statsInimigo["Energia"]+=1
            print("---"*20)
            self.printer_local(f"""Turno:{turno}\nVocê possui"""+colorama.Fore.LIGHTGREEN_EX+ f""" {round(self.playerStats["Vida"],2)} / {self.playerStats["VidaMax"]} de Vida"""+colorama.Fore.RESET+f""" e """+colorama.Fore.LIGHTBLUE_EX+f"""{self.playerStats["Energia"]} de Energia"""+colorama.Fore.RESET+"\nSeu ataque é de"+colorama.Fore.RED+f" {self.playerStats["Ataque"]}"+colorama.Fore.RESET+f"""\
                    \nO {statsInimigo['Nome']} possui"""+colorama.Fore.LIGHTGREEN_EX+f""" {statsInimigo["Vida"]} de vida"""+colorama.Fore.RESET+" e "+colorama.Fore.LIGHTBLUE_EX+f"{statsInimigo["Energia"]} de Energia."+colorama.Fore.RESET)
            ETipoAtk, EDano = self.IaInimigos(inimigo)
            self.printer_local(f"Seu inimigo irá usar um {ETipoAtk} e dara "+colorama.Fore.RED+f"{EDano} de dano"+colorama.Fore.RESET+", como você reagirá?\n"+"---"*20+"\n[1]Ataque leve\n[2]Ataque pesado "+colorama.Fore.LIGHTBLUE_EX+"(2 Energia)"+colorama.Fore.RESET+" \n[3]Defesa")
            escolha, DanoPlr = self.ChecarAtaque(input(">"))
            match escolha:
                case "Ataque leve" | "Ataque pesado":
                    statsInimigo["Vida"] -= DanoPlr
                    if statsInimigo["Vida"] > 0:
                        self.playerStats["Vida"] -= EDano
                        self.printer_local(f"Você ataca o inimigo com um {escolha},tirando "+colorama.Fore.RED+f" {DanoPlr} de vida!"+colorama.Fore.RESET+f"\nEle reage com um {ETipoAtk} te causando "+colorama.Fore.RED+f"{EDano} de dano..."+colorama.Fore.RESET)
                        if not inimigo == "EsqueletoTutorial" and inimigo["Nome"] == "Vampiro" and ETipoAtk in ["Mordida leve","Mordida Fatal"]:
                            cura = EDano / 2
                            statsInimigo["Vida"] += cura
                            self.printer_local(f"O ataque {ETipoAtk} cura o vampiro em "+colorama.Fore.LIGHTGREEN_EX+f"{cura} de Vida."+colorama.Fore.RESET)
                        elif not inimigo == "EsqueletoTutorial" and inimigo["Nome"] == "Eternus, o Imortal":
                            cura = (inimigo["Vida"]/50) + 5
                            statsInimigo["Vida"]+=cura
                            self.printer_local(f"Você obeserva as feridas dele se fechando, você não pode fazer nada. Ele se cura em "+colorama.Fore.LIGHTGREEN_EX+f"{cura} de Vida."+colorama.Fore.RESET)
                        time.sleep(1.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        self.printer_local(f"Você ataca o inimigo com um {escolha},tirando "+colorama.Fore.RED+f" {DanoPlr} de vida!"+colorama.Fore.RESET+f"\nEle não consegue reagir...")
                        break
                case "Defesa":
                    if ETipoAtk in ["Ataque leve","2x Ataque leve","Corte leve","Mordida leve","Soco Leve","Chuva de Socos leves"]:
                        self.printer_local("Você defendeu um ataque fraco completamente! Ignorando "+colorama.Fore.BLUE+f"{EDano} de dano."+colorama.Fore.RESET)
                    else:
                        DDano = EDano * 0.5
                        self.playerStats["Vida"] -= DDano
                        self.printer_local(f"Você defendeu um ataque pesado, recebeu apenas "+colorama.Fore.BLUE+f"{DDano} de dano! 50% de defesa!"+colorama.Fore.RESET)
                        if not inimigo == "EsqueletoTutorial" and inimigo["Nome"] == "Eternus, o Imortal":
                            cura = (inimigo["Vida"]/50) + 5
                            statsInimigo["Vida"]+=cura
                            self.printer_local(f"Você obeserva as feridas dele se fechando, você não pode fazer nada. Ele se cura em "+colorama.Fore.LIGHTGREEN_EX+f"{cura} de Vida."+colorama.Fore.RESET)
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
            if statsInimigo["Vida"] <= 0 or self.playerStats["Vida"] <= 0:
                break
            turno+=1
        if self.playerStats["Vida"] <= 0:
            self.printer_local("Você perdeu... acho que foi falta de habilidade...")
        else:
            self.printer_local(f"Você ganhou!! Você possui "+colorama.Fore.LIGHTGREEN_EX+f"{self.playerStats["Vida"]} de vida."+colorama.Fore.RESET)
            if inimigo != "EsqueletoTutorial" and inimigo["Nome"] == "Eternus, o Imortal":
                self.printer_local(f"Você derrotou o chefe deste lugar, você observa uma  Porta fantasmagorica e voadora voando pela sala...\nVocê com muito esforço alcança ela... você atravessa a porta e se ve em um trono, o seu trono, você retornou ao seu imperio.\nParabéns! Você venceu! Desculpa pela falta de conteudo e etc!")
                sys.exit()
            if inimigo != "EsqueletoTutorial":
                if inimigo["Nome"] in ["Cavalheiro-Zumbi","Lobisomem"]:
                    quantidade = random.randint(1,2)
                    pots = loot.GerarLoot(quantidade)
                    goldDrop = loot.GerarGold("Dificil")
                else:
                    quantidade = random.randint(1,1)
                    goldDrop = loot.GerarGold("Facil")
                    pots = loot.GerarLoot(quantidade)
                self.printer_local(colorama.Fore.LIGHTYELLOW_EX+f"Você dropou {goldDrop} de Gold!!!")
                self.AdicionarOuro(goldDrop)
                self.printer_local(colorama.Fore.LIGHTYELLOW_EX+f"Você dropou {len(pots)} poções!"+colorama.Fore.RESET)
                for i in pots:
                    self.UsarPot(i)
            else:
                goldDrop = loot.GerarGold("EsqueletoTutorial")
                self.printer_local(colorama.Fore.LIGHTYELLOW_EX+f"Você dropou {goldDrop} de Gold!!!"+colorama.Fore.RESET)
                self.AdicionarOuro(goldDrop)
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            cdialogo.ProximaSala(bHandler=batalha,dHandler=cdialogo)

    def AdicionarOuro(self,quantia):
        self.playerStats["Gold"]+=quantia

    def UsarPot(self,pot):
        stat = pot["Stats"]
        self.playerStats[stat]+= pot["Aumento"]
        self.printer_local(f"A {pot["Nome"]} de {stat} aumentou seu(a) {stat} em {pot["Aumento"]}")
        if stat == "VidaMax":
            self.playerStats["Vida"]+=pot["Aumento"]

    def IaInimigos(self,Inimigo):
        if Inimigo == "EsqueletoTutorial":
            return "Ataque leve",1
        Inimigo["Energia"]+1
        chanceATK = random.randrange(100)
        match Inimigo["Nome"]:
            case "Zumbi":
                if Inimigo["Energia"] >= 2:
                    if chanceATK >=50:
                        Inimigo["Energia"]-=2
                        return "Ataque pesado", (Inimigo["Dano"] * 2)
                return "Ataque leve", Inimigo["Dano"]
            case "Esqueleto":
                if Inimigo["Energia"] >= 2:
                    if chanceATK >=50:
                        Inimigo["Energia"]-=2
                        return "2x Ataque leve", (Inimigo["Dano"] * 2)
                return "Ataque leve", Inimigo["Dano"]
            case "Vampiro":
                if Inimigo["Energia"] >= 3 and chanceATK>= 25:
                        Inimigo["Energia"]-=3
                        return "Mordida Fatal",Inimigo["Dano"]*2
                elif Inimigo["Energia"] >=1 and chanceATK >=25:
                        Inimigo["Energia"]-=1
                        return "Mordida leve",Inimigo["Dano"]*1.5
                return "Ataque leve",Inimigo["Dano"]
            case "Cavalheiro-Zumbi":
                if Inimigo["Energia"] >= 3:
                    Inimigo["Energia"]-=3
                    return "Corte Profundo", Inimigo["Dano"]*3
                elif Inimigo["Energia"]>= 1 and chanceATK>=70:
                    Inimigo["Energia"]-=1
                    return "Corte leve",Inimigo["Dano"]*2
                return "Ataque leve",Inimigo["Dano"]
            case "Lobisomem":
                if Inimigo["Energia"]>=3 and chanceATK >= 40:
                    Inimigo["Energia"]-=2
                    return "2x Mordida Pesada",(Inimigo["Dano"]*2) + (Inimigo["Vida"]/10)
                return "Ataque leve",Inimigo["Dano"] + (Inimigo["Vida"]/10)
            case "Eternus, o Imortal":
                Inimigo["Energia"]+=1
                if Inimigo["Energia"] >= 9 and chanceATK>70:
                    Inimigo["Energia"]-=5
                    return "Aniquilacao",Inimigo["Dano"]*4
                elif chanceATK >= 60:
                    return "Chuva de Socos leves",Inimigo["Dano"]*2
                elif chanceATK>=50:
                    return "Soco Leve", Inimigo["Dano"]
                elif Inimigo["Energia"] >= 4 and chanceATK>=30:
                    Inimigo["Energia"]-=5
                    return "Soco Poderoso", Inimigo["Dano"]*1.5
                return "Eternus te observa...",0
    
                

            
        


    def ChecarAtaque(self,Escolha):
        while True:
            try:
                if int(Escolha.lower().strip()) not in [1,2,3]:
                    self.printer_local("Digite 1,2 ou 3")
                    Escolha = input(">")
                elif int(Escolha) == 2 and not self.playerStats["Energia"] >= 2:
                    self.printer_local("Você não possui "+colorama.Fore.LIGHTBLUE_EX+"2 de energia"+colorama.Fore.RESET+". Escolha outra ação!")
                    Escolha = input(">")
                else:
                    break
            except ValueError:
                self.printer_local("Use os numeros 1,2 ou 3!")
                Escolha = input(">")
        match int(Escolha):
            case 1:
                return "Ataque leve",self.playerStats["Ataque"]
            case 2:
                self.playerStats["Energia"]-=2
                return "Ataque pesado",self.playerStats["Ataque"]*2
            case 3:
                return "Defesa",0

    def gerarInimigo(self,batalha):
        if batalha == "Batalha Dificil":
            inimigo_d = random.choice(["Cavalheiro","Lobisomem"])
            return self.scaledInimigos(inimigo=inimigo_d,dificuldade="Dificil")
        elif batalha == "Batalha Facil":
            inimigo_f = random.choice(["Zumbi","Esqueleto","Vampiro"])
            return self.scaledInimigos(inimigo=inimigo_f,dificuldade="Facil")
        elif batalha == "SALA DE BOSS":
            inimigo_f = "O Eterno imortal"
            return self.scaledInimigos(inimigo=inimigo_f,dificuldade="Boss")
        

    def scaledInimigos(self,inimigo,dificuldade = None):
        sala = self.playerStats["Sala"]
        Inimigos = {
            "EsqueletoTutorial":{
                "Nome": "Esqueleto Fraco",
                "Vida":15,
                "Dano": 1,
                "Energia": 0,
            },
            "Facil":{
                "Esqueleto":{
                    "Nome": "Esqueleto",
                    "Vida":15 + (sala*2),
                    "Dano": 3 + (sala),
                    "Energia": 0,
                },
                "Zumbi":{
                    "Nome": "Zumbi",
                    "Vida":20 + (sala * 3),
                    "Dano": 2 + (sala/2),
                    "Energia": 0,
                },
                "Vampiro":{
                    "Nome":"Vampiro",
                    "Vida":20 + (sala * 5),
                    "Dano": 2 + (sala * 1.5),
                    "Energia":0
                }
            },
            "Dificil":{
                "Cavalheiro":{
                    "Nome": "Cavalheiro-Zumbi",
                    "Vida":35 + (sala*5),
                    "Dano": 4 + (sala*2),
                    "Energia": 1,
                },
                "Lobisomem":{
                    "Nome":"Lobisomem",
                    "Vida":40 + (sala*7),
                    "Dano": 5 + (sala*1),
                    "Energia": 0
                }
            },
            "Boss":{
                "O Eterno imortal":{
                    "Nome":"Eternus, o Imortal",
                    "Vida":700,
                    "Dano":40,
                    "Energia": 0
                }
            }
        }
        if dificuldade != None: return Inimigos[dificuldade][inimigo]
        else: return Inimigos[inimigo]
