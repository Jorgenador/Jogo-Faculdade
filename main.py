import dialogos
import batalha

dHandler = dialogos.CDialogos()
bHandler = batalha.Batalhas()

dHandler.Printer("Inicio",preText=True,Resposta="Inicio",bHandler=bHandler)
dHandler.Printer("firstRoom",preText=True,Resposta="Batalha1",bHandler=bHandler)