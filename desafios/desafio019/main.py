from rich import print
from rich import inspect
from rich.traceback import install
from polygon import Polygon
from quadrado import Quadrado
from circulo import Circulo
install()



c1 = None
q1 = None
def start():
    status = ""
    forma = ""
    print(f"Gostaria de ver um quadrado ou um circulo?")
    r = input("")
    if r == "quadrado":
        status = r
    elif r == "circulo":
        status = r
    else:
        r = input(f"Digite exatamente quadrado ou circulo por gentileza!\n")
        status = r
    return status



status = start()


print(f"[debug] status: {status!r}")
def criar_quadrado():
    print(f"[blue]Qual o tamanho do lado em centimetros?[/]\n")
    tam_lado = input()
    tam_lado = float(tam_lado)
    q1 = Quadrado(tam_lado)
    return q1


def criar_circulo():
    print(f"Qual o tamanho do raio?")
    tam__raio = input()
    tam__raio = float(tam__raio)
    c1 = Circulo(tam__raio)
    return c1

def info():

    if c1 == None:
        print("info ta aqui pai")
        print(f"Perímetro do quadrado: {q1.perimitry()} cm")

        print(f"Área do quadrado: [blue]{q1.area()}[/] cm²")
        
    if q1 == None:
        print(f"A área é: {c1.area():.2f}")

        print(f"O perimetro é:{c1.perimitry():.2f}")
    elif c1 and q1 !=None:
        print(f"A área é: {c1.area():.2f}")

        print(f"O perimetro é:{c1.perimitry():.2f}")
        print("info ta aqui pai")
        

        print(f"Perímetro do quadrado: {q1.perimitry()} cm")

        print(f"Área do quadrado: [blue]{q1.area()}[/] cm²")


def pergunta():
        print(f"\nGostaria de ver fazer mais alguma coisa?\n"
            "Ver informações digite: info\n"
            "criar mais alguma coisa? digite: criar\n"
            "sair digite: sair")
        status = input()
        print(f"[debug] status: {status!r}")
        if status =="info":
            info()
        if status == "criar":
            start()

if(status == "circulo"):
    c1 = criar_circulo()
    print("chamado")
    print(f"[debug] status: {status!r}")
    pergunta()


if(status == "quadrado"):
    q1 = criar_quadrado()
    print("chamado")
    print(f"[debug] status: {status!r}")
    pergunta()



