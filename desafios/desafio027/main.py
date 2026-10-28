from characters.npc import nStatus
from characters.player import pStatus
from rich import print
from rich import inspect
from rich.traceback import install
from random import randint, choices,choice
from rich.panel import Panel

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

def detail(personagem):
    conteudo = (
        f"[bold blue]Nome:[/]{personagem.name}\n" 
        f"[bold red]HP: [/]{personagem.hp}\n"
        f"[bold cyan]Estamina:[/]{personagem.stamina}\n"
     )

    return Panel(conteudo,
                 expand=False,
                 title=f"{personagem.name}",
                 border_style="red"
                 )

def start():
    listvalidar = ["npc","player"]
    ask = validar("Gostaria de criar um player ou NPC? escreva sua solicitação por favor\n",listvalidar )
    
    
    if ask == "player":
        name = input("Nome por favor!\n")
        hp = randint(5,50)
        stamina = randint(10,120)
        playerst = pStatus(hp,stamina, name)
        player.append(playerst)
        print(detail(playerst))

    elif ask == "NPC":
        pass

start()