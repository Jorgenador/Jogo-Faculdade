import random

class Salas():

    def __init__(self):
        pass


    def GerarSalas(self):
        Salas = {
            "Tesouro":99,
            "Shop":1,
            "Batalha Facil":0
            }
        batalhaGarantida = {
            "Batalha Dificil":80,
            "Batalha Facil":0
        }
        luck = random.randrange(100)
        bLuck = random.randrange(100)
        salaT = ["Sala de Descanso"]
        for room,value in Salas.items():
             if luck >= value:
                salaT.append(room)
                break
        for room,value in batalhaGarantida.items():
             if bLuck >= value:
                salaT.append(room)
                break    
        return salaT 

