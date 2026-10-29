from random import randint
class pStatus():
    def __init__(self, hp = 0, stamina = 0, name = " "):
        self.hp = hp
        self.stamina = stamina
        self.name = name
def gerar_player():
        name = input("Nome por favor!\n")
        hp = randint(5,50)
        stamina = randint(10,120)
        return pStatus(hp,stamina, name)


