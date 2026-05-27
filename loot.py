import random

loots = {
    "Pot De Vida":{
        "Pocao Grande":{"Tipo":"Pocao Grande de Vida","Chance":80,"Aumento":35, "Stats":"VidaMax"},
        "Pocao Media":{"Tipo":"Pocao Media de Vida","Chance":50, "Aumento":22, "Stats":"VidaMax"},
        "Pocao Pequena":{"Tipo":"Pocao Pequena de Vida","Chance":0,"Aumento":10,"Stats":"VidaMax"}},
    "Pot de Força":{
        "Pocao Grande":{"Tipo":"Pocao Grande de Força","Chance":80,"Aumento":11,"Stats":"Ataque"},
        "Pocao Media":{"Tipo":"Pocao Media de Força","Chance":50, "Aumento":6,"Stats":"Ataque"},
        "Pocao Pequena":{"Tipo":"Pocao Pequena de Força","Chance":0, "Aumento":3,"Stats":"Ataque"}},
}

shop = {
    "Artefato da Vida":{"Descricao":"Um artefato que aumenta drasticamente a sua vida!(+60 Vida Maxima)","Tipo1":"VidaMax","Tipo2":None,"Valor1":60,"Valor2":0,"Preco":500},
    "Espada Sagrada":{"Descricao":"Uma espada com uma aura amedrontadora!(+15 de Ataque)","Tipo1":"Ataque","Tipo2":None,"Valor1":15,"Valor2":0,"Preco":500},
    "Escudo com Espinhos":{"Descricao":"Um escudo com habilidades defensivas e ofensivas.(+20 Vida Maxima +8 Ataque)","Tipo1":"VidaMax","Tipo2":"Ataque","Valor1":20,"Valor2":8,"Preco":650},
    "Armadura Eterea":{"Descricao":"Uma armadura cintilante com altas capcidades protetivas(+100 Vida Maxima)","Tipo1":"VidaMax","Tipo2":None,"Valor1":100,"Valor2":0,"Preco":1000},
}
 

Gold = {
    "EsqueletoTutorial":{"Min":25,"Max":60},
    "Dificil":{"Min":100,"Max":250},
    "Facil":{"Min":50,"Max":140}
}
def GerarLoot(QuantidadeMax):
    loot_escolhido = []
    
    categorias = list(loots.keys())
    for i in range(QuantidadeMax):
        chance = random.randrange(100)
        tipo_categoria = random.choice(categorias)
        for nome_pocao, stats in loots[tipo_categoria].items():
            if chance >= stats["Chance"]:
                item_formatado = stats.copy()
                item_formatado["Nome"] = nome_pocao
                loot_escolhido.append(item_formatado)
                break 
    return loot_escolhido

def GerarGold(Tipo):
    return random.randrange(Gold[Tipo]["Min"],Gold[Tipo]["Max"]+1)

def GerarShop():
    items = []
    possibilidades = list(shop.keys())
    for i in range(2):
        possib = random.choice(possibilidades)
        escolhido = shop[possib]
        item = escolhido.copy()
        item["Nome"] = possib
        items.append(item)
    return items
