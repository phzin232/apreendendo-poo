from characters.npc import nStatus
from characters.player import pStatus
from rich import print
from rich import inspect
from rich.traceback import install
from random import randint
install()
player = []
npc = []
def end():
    print(f"[red]Game Over")


def validar(pergunta, lista):
    text_a_validar = input(pergunta)

    while text_a_validar  not in lista:
        text_a_validar = input("Digite novamente por gentileza!\n")

    return text_a_validar


def start():
    listvalidar = ["npc","player"]
    ask = validar("Gostaria de criar um player ou NPC? escreva sua solicitação por favor\n",listvalidar )
    
    
    if ask == "player":
        name = input("Nome por favor!\n")
        hp = randint(5,50)
        stamina = randint(10,120)
        playerst = pStatus(hp,stamina, name)
        player.append(playerst)

        inspect(playerst)
start()