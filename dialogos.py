import time

class CDialogos:

    def __init__(self):
        self.dialogosProntos = {
            "Inicio":"Olá Aventureir@, qual seria o seu nome?",
            "firstRoom": "Está pronto para entrar na sua primeira batalha? Ela será facil!"
        }


    def Printer(self,dialogo,preText = True,Resposta = "",bHandler = None):
        if bHandler != None: batalha = bHandler
        if preText:
            texto = self.dialogosProntos[dialogo]
        else:
            texto = dialogo
        for c in texto:
            print(c,end = "",flush= True)
            time.sleep(0.005)
        print("")
        if Resposta != "":
            match Resposta:
                case "Inicio":
                    self.Respostas("Inicio",batalha)
                case "Batalha1":
                    self.Respostas("Batalha1",batalha)
                    


    def Respostas(self,Caso,bHandler = None):
        if bHandler != None: batalha = bHandler
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
                    batalha.iniciar_batalha()
                elif resposta == "t":
                    batalha.iniciar_batalha(Skip = True)
                else:
                    self.Printer("Quando estiver pronto apresse enter",preText=False)
                    input(">")
                    batalha.iniciar_batalha()



        


