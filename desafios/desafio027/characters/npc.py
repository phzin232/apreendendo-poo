from random import randint, choices,choice

class nStatus():
    def __init__(self, hp = 0, stamina = 0, name = "", tipo_npc = ""): 
        self.hp = hp
        self.stamina = stamina
        self.name = name
        self.tipo_npc = tipo_npc



def gerar_monstro():
    hp = randint(10,50)
    stamina = randint(10,120)
    tipo_npc = choices(["Goblin", "Orc", "Wolf", "Demon", "Fallen Angel"], weights=[40, 20, 30,9,1],k=1)[0]
    name = f"{tipo_npc} {choice(["Avançado", "Novo", "Batedor"])}"
    if tipo_npc == "Goblin":
        stamina /= 1.3
        hp *= 1.02
    if tipo_npc == "Orc":
        hp *=2
        stamina /= 2
    if tipo_npc == "Wolf":
        hp /= 1.2
        stamina *= 4
    if tipo_npc == "Demon":
        hp *= 15
        stamina *= 25
    if tipo_npc == "Fallen Angel":
        hp *= 130
        stamina *= 1160
    return nStatus( int(hp), int(stamina), name, tipo_npc)




