from random import randint, choices,choice

class nStatus():
    def __init__(self, hp = 0, stamina = 0, name = "", type = ""): 
        self.hp = hp
        self.stamina = stamina
        self.name = name
        self.type = type



def gerar_npc():
    hp = randint(10,50)
    stamina = randint(10,120)
    type = choices(["Goblin", "Orc", "Wolf", "Demon", "Fallen Angel"], weights=[40, 20, 30,9,1],k=1)[0]