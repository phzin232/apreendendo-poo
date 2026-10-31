from random import randint, choices
class pStatus():
    def __init__(self, hp = 0, stamina = 0, name = " ",dano = 0):
        self.hp = hp
        self.stamina = stamina
        self.name = name
        self.dano = dano
def gerar_player():
        name = input("Nome por favor!\n")
        hp = randint(10,50)
        stamina = randint(10,120)
        dano = randint(5,10)
        return pStatus(hp,stamina, name, dano)

def ataque_player(self, alvo):
     dano = self.dano
     tipo_dano = choices(["normal", "critico"], weights=[ 90,10],k=1)[0]
     if tipo_dano == "critico":
          dano *= 3
     return dano

    




