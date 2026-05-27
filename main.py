import dialogos
import batalha
import random
import loot
import os
# Começo do desenvolvimento 25/05 as 20:00, basicamente 48 horas antes da deadline

dHandler = dialogos.CDialogos()
bHandler = batalha.Batalhas()

os.system('cls' if os.name == 'nt' else 'clear')
dHandler.Printer("Inicio",preText=True,Resposta="Inicio",bHandler=bHandler,dHandler = dHandler)
dHandler.Printer("firstRoom",preText=True,Resposta="Batalha1",bHandler=bHandler,dHandler = dHandler)
