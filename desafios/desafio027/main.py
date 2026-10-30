from characters.npc import nStatus, gerar_monstro, npc_ataque
from characters.player import pStatus, gerar_player
from rich import print,inspect
from rich.traceback import install
from random import randint, choices,choice, shuffle
from rich.panel import Panel
import time


install()
player = []
npc = []




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
    game_started = False
    status = "waiting"
    listvalidar = ["player","npc"]
    ask = validar("Gostaria de criar um Player ou NPC? escreva sua solicitação por favor\n",listvalidar )
    
    
    if ask == "player":
        playerst = gerar_player()
        player.append(playerst)
        print(detail(playerst))
        game_started = True
        time.sleep(2)
        gerar_horda(status, game_started)


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

def end(status):
   if status == "game_over":
        print(f"[red]Game Over")
        time.sleep(3)
        novo_jogo()

def gerar_horda(status,game_started):
    if game_started == True:
       
        status = "preparing"
        global quantia_montro 
        quantia_montro = randint(1,7)
        while quantia_montro > 0:
            monterst = gerar_monstro()
            npc.append(monterst)
            quantia_montro -= 1    
       
        quantia_montro = len(npc)
        ordem(status)
    else:
        print("Valide o codigo primeiro. Erro fatal.")

def ordem(status):
    ordemataque = []
    if status == "preparing":
        if quantia_montro >=1:
                shuffle(npc)
        ordemataque.extend(player)
        ordemataque.extend(npc)
        shuffle(ordemataque)

        status = "ready"
        numerar_inimigos(status, ordemataque)

def numerar_inimigos(status, ordemataque):
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
        atacar(status, inimigos, ordemataque)
        
def atacar(status, inimigos, ordemdeataque):
    if status == "ready":
        turno = ordemdeataque[0]
        if status == "ready":
            dano = int
            status = "combate"
            if isinstance(turno, nStatus):
                dano = npc_ataque(turno,player[0])
                print(f"O monstro {turno[0].name} ira te atacar com: {dano} de dano \n"
                      "Agora você tem\n")
                player[0].hp -= dano
                print(detail(player[0]))
                
                        



        


start()