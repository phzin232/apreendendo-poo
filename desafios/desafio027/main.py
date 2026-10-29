from characters.npc import nStatus, gerar_monstro
from characters.player import pStatus, gerar_player
from rich import print,inspect
from rich.traceback import install
from random import randint, choices,choice, shuffle
from rich.panel import Panel
import time


install()
player = []
npc = []
game_started = False
status = "waiting"


def validar(pergunta, lista):
    text_a_validar = input(pergunta)

    while text_a_validar  not in lista:
        text_a_validar = input("Digite novamente por gentileza!\n")
        text_a_validar = text_a_validar.strip().lower()
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
    listvalidar = ["player","npc"]
    ask = validar("Gostaria de criar um Player ou NPC? escreva sua solicitação por favor\n",listvalidar )
    
    
    if ask == "player":
        playerst = gerar_player()
        player.append(playerst)
        print(detail(playerst))
        global game_started
        game_started = True
        time.sleep(2)
        gerar_horda()


    elif ask == "npc":
        monterst = gerar_monstro()
        npc.append(monterst)
        print(detail(monterst))
        print("feito")

def novo_jogo():
    listvalidar = ["sim", "não"]
    ask = validar(f"Gostaria de começar um novo jogo? Sim ou não?\n",listvalidar)
    if ask == "não":
        print(f"[purple] obrigado por jogar!")
        quit()
    if ask == "sim":
        start()

def end():
    print(f"[red]Game Over")
    time.sleep(3)
    novo_jogo()

def gerar_horda():
    if game_started == True:
        global status
        status = "preparing"
        global quantia_montro 
        quantia_montro = randint(1,7)
        while quantia_montro > 0:
            monterst = gerar_monstro()
            npc.append(monterst)
            quantia_montro -= 1    
       
        quantia_montro = len(npc)
        ordem()

def ordem():
    ordemataque = []
    global status
    if status == "preparing":
        if quantia_montro >=1:
                shuffle(npc)
        ordemataque.extend(player)
        ordemataque.extend(npc)
        shuffle(ordemataque)

        status = "ready"
        numerar_inimigos(ordemataque)

def numerar_inimigos(ordemataque):
    contador = 0
    inimigos = []
    if status == "ready":
        print(f"A ordem do combate é:\n")
        for cabacice in ordemataque:
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})")
                contador += 1
        time.sleep(2)
        print(f"Já a de inimigos sem você é:")
        contador = 0
        for cabacice in ordemataque:
            if isinstance(cabacice, nStatus):
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})")
                contador += 1
                inimigos.append(cabacice)
        atacar(inimigos)
        
def atacar(inimigos):
    if status == "ready":
        
        pass


start()