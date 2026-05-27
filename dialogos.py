import time
import Salas
from colorama import Fore 
import os
import random
import loot

roomHandle = Salas.Salas()



class CDialogos:

    def __init__(self):
        self.dialogosProntos = {
            "Inicio":"Olá Aventureir@, qual seria o seu nome?",
            "firstRoom": "Está pronto para entrar na sua primeira batalha? Ela será facil!",
            "Salas": "Use 1,2 ou 3 para escolher a sala!"
        }


    def Printer(self,dialogo,preText = True,Resposta = "",bHandler = None,dHandler = None):
        if bHandler != None: batalha = bHandler
        if dHandler != None: cdialogo = dHandler
        if preText:
            texto = self.dialogosProntos[dialogo]
        else:
            texto = dialogo
        for c in texto:
            print(c,end = "",flush= True)
            time.sleep(0.0025)
        print("")
        if Resposta != "":
            match Resposta:
                case "Inicio":
                    self.Respostas("Inicio",batalha,cdialogo)
                case "Batalha1":
                    self.Respostas("Batalha1",batalha,cdialogo)
                case "Salas":
                    return self.Respostas("Salas",batalha,cdialogo)
                    
    def ProximaSala(self,bHandler = None, dHandler = None,Salas = None):
        if bHandler != None: batalha = bHandler
        if dHandler != None: cdialogo = dHandler
        if Salas == None: salas = roomHandle.GerarSalas() 
        else: salas = Salas
        choose_room = self.Printer(f"Você está indo para sala: {batalha.playerStats["Sala"]+1}\nVocê possui 3 opções de salas para seguir:\n[1] A sua direita existe uma {salas[0]}\n[2] A sua frente existe uma {salas[1]}\n[3] A sua esquerda existe uma {salas[2]}\n[4]Vizualiar Stats\nUse 1,2,3 ou 4!!",preText=False,Resposta="Salas",bHandler=batalha,dHandler=cdialogo)
        if choose_room !=3: choose_room = salas[choose_room]
        if choose_room !=3: bHandler.playerStats["Sala"]+=1
        match choose_room:
            case "Batalha Facil"|"Batalha Dificil":
                self.Printer(f"Você irá prosseguir para uma {choose_room}, se prepare para a batalha!",preText=False)
                batalha.iniciar_batalha(dHandler = cdialogo,bHandler = batalha,Batalha = choose_room)
            case "Sala de Descanso":
                self.Printer(f"Você chega a uma sala e vê uma fogueira... Você decide descansar um pouco...",preText=False)
                cura = bHandler.playerStats["VidaMax"] / 4
                bHandler.playerStats["Vida"]+= cura
                if bHandler.playerStats["Vida"] > bHandler.playerStats["VidaMax"]:
                    bHandler.playerStats["Vida"] = bHandler.playerStats["VidaMax"]
                self.Printer(f"Você se curou em "+Fore.LIGHTGREEN_EX+f"{cura} de Vida!\nVida atual {bHandler.playerStats["Vida"]} / {bHandler.playerStats["VidaMax"]}"+Fore.RESET,preText=False)
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.ProximaSala(batalha,cdialogo)
            case "Tesouro":
                qntTesouro = random.randrange(3,5)
                self.Printer(f"Você entra em uma sala com um bau... Você encontra {qntTesouro} poções!",preText=False)
                pots = loot.GerarLoot(qntTesouro)
                for i in pots:
                    batalha.UsarPot(i)
                time.sleep(2.5)
                self.ProximaSala(batalha,cdialogo)
            case "Shop":
                opcoes = loot.GerarShop()
                self.Printer(f"Você chega em uma loja esquisita... Um sapo? falante te oferece os itens dele! Porem, Você so poderá comprar 1, use os numeros para escolher",preText=False)
                self.Printer("[0]Sair sem comprar nada",preText=False)
                num = 1
                for i in opcoes:
                    self.Printer(f"[{num}]Ele te oferece o(a) {i["Nome"]} que é {i["Descricao"]}, Custa {i["Preco"]} Gold",preText=False)
                    num +=1
                
                escolha = self.Respostas("Shop",bHandler=batalha,dHandler=cdialogo,ShopLen=len(opcoes))
                print(opcoes[escolha])
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.Printer("Você possui\n"+Fore.LIGHTGREEN_EX+f"{batalha.playerStats["Vida"]} / {batalha.playerStats["VidaMax"]} de Vida"+Fore.RED+f"\n{batalha.playerStats["Ataque"]} de Ataque!"+Fore.LIGHTYELLOW_EX+f"\n{batalha.playerStats["Gold"]} de Gold"+Fore.RESET,preText=False)
                self.ProximaSala(bHandler=batalha,dHandler=cdialogo,Salas=salas)


    def Respostas(self,Caso,bHandler = None,dHandler=None,ShopLen=None):
        if bHandler != None: batalha = bHandler
        if dHandler != None: cdialogo = dHandler
        match Caso:
            case "Inicio":
                while True:
                    nome = input("\n>")
                    self.Printer(f"Seu nome é realmente {nome}?(S/N)",preText=False)
                    while True:
                        r = input(">").lower().strip()
                        if r in ["s","n"]:
                            break
                        self.Printer("Use apenas S/N",preText=False)

                    if r == "s":
                        batalha.playerStats["Nome"] = nome
                        break
                    else:
                        self.Printer("Então vamos tentar novamente, Digite o seu nome!",preText=False)
            case "Batalha1":
                self.Printer("Use S/N (ou T para skipar o tutorial, bom para rejogar!)",preText=False)
                resposta = input(">").lower().strip()
                if resposta == "s":
                    batalha.iniciar_batalha(dHandler = cdialogo,bHandler = batalha)
                elif resposta == "t":
                    batalha.iniciar_batalha(Skip = True,dHandler = cdialogo, bHandler = batalha)
                else:
                    self.Printer("Quando estiver pronto apresse enter",preText=False)
                    input(">")
                    batalha.iniciar_batalha(dHandler = cdialogo,bHandler = batalha)
            case "Salas":
                while True:
                    resposta = input(">")
                    try:
                        if int(resposta.strip()) not in [1,2,3,4]:
                            self.Printer("Salas")
                        else:
                            break
                    except ValueError:
                        self.Printer("Use os NUMEROS 1,2 ou 3!",preText=False)
                match int(resposta.strip()):
                    case 1:
                        return 0
                    case 2:
                        return 1
                    case 3:
                        return 2
                    case 4:
                        return 3
            case "Shop":
                while True:
                    resposta = input(">")
                    opcoes = ", ".join(map(str,list(range(ShopLen+1))))
                    try:
                        if int(resposta.strip()) not in list(range(ShopLen+1)):
                            self.Printer(f"Use {opcoes}",preText=False)
                        else:
                            break
                    except ValueError:
                        self.Printer(f"Use os numeros:{opcoes}",False)
                return (int(resposta.strip())-1)




        


