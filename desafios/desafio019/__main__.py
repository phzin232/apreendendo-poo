from rich import print
from rich import inspect
from rich.traceback import install
from polygon import Polygon
from quadrado import Quadrado
from circulo import Circulo
install()

status = "start"
circulo_criado = False
quadrado_criado = False

def start():
    status ="ask"
    print(f"Gostaria de ver um quadrado ou um circulo?")
    r = input("")
    if r == "quadrado":
        status = r
    elif r == "circulo":
        status = r
    else:
        r2 = input(f"Digite exatamente quadrado ou circulo por gentileza!\n")

start()

def criar_quadrado():
    print(f"[blue]Qual o tamanho do lado em centimetros?[/]\n")
    tam_lado = input()
    tam_lado = float(tam_lado)
    q1 = Quadrado(tam_lado)
    quadrado_criado = True

    return q1, status , quadrado_criado

def criar_circulo():
    print(f"Qual o tamanho do raio?")
    tam__raio = input()
    tam__raio = float(tam__raio)
    circulo_criado = True
    c1 = Circulo(tam__raio)
    return c1, status ,circulo_criado

if circulo_criado == True:
    print(f"Gostaria de ver fazer mais alguma coisa?\n"
        "Ver informações digite: info\n"
        "criar um quadrado: digite quadrado\n"
        "sair digite: sair")
    status = input()
    

if(status == "circulo"):
    criar_circulo()

if(status == "quadrado" ):
    criar_quadrado


if(status == "info"):
    print(f"Perímetro do quadrado: {q1.perimitry()} cm")
    print(f"Área do quadrado: [blue]{q1.area()}[/] cm²")


print(f"A área é: {c1.area():.2f}")
    
print(f"O perimetro é:{c1.perimitry():.2f}")