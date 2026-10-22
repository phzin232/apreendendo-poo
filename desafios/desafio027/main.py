from characters.npc import nStatus
from characters.player import pStatus
from rich import print
from rich import inspect
from rich.traceback import install
from random import randint
install()

def end():
    print(f"[red]Game Over")

def start():
    hp = 0
    ask = input("Gostaria de criar um player?")
    if ask == "player":
        hp = randint(0,50)
    print(hp)



start()