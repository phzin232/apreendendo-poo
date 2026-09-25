from rich import print
from rich import inspect
from rich.traceback import install
from polygon import Polygon
from quadrado import Quadrado
from circulo import Circulo
install()

status = "start"



if(status >= "start"):
    status ="ask"
    print(f"Gostaria de ver um quadrado ou um circulo?")
    r = input("")
    if r == "quadrado":
        status = r
    elif r == "circulo":
        status = r
    else:
        r2 = input(f"Digite exatamente quadrado ou circulo por gentileza!\n")

if(status == "quadrado" ):
    print(f"[blue]Qual o tamanho do lado em centimetros?[/]\n")
    tam_lado = input()
    tam_lado = float(tam_lado)

    q1 = quadrado(tam_lado)
    print(f"Perímetro do quadrado: {q1.perimitry()} cm")

    print(f"Área do quadrado: [blue]{q1.area()}[/] cm²")


if(status =="circulo"):
   print(f"Qual o tamanho do raio?")
   tam__raio = input()
   tam__raio = float(tam__raio)

   c1 = Circulo(tam__raio)

   print(f"A área é: {c1.area():.2f}")

   print(f"O perimetro é:{c1.perimitry():.2f}")

