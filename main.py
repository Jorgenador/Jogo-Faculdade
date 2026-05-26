import dialogos
import batalha

# Começo do desenvolvimento 25/05 as 20:00, basicamente 48 horas antes da deadline

dHandler = dialogos.CDialogos()
bHandler = batalha.Batalhas()

dHandler.Printer("Inicio",preText=True,Resposta="Inicio",bHandler=bHandler)
dHandler.Printer("firstRoom",preText=True,Resposta="Batalha1",bHandler=bHandler)