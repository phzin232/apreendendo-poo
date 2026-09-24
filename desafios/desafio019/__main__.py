from rich import print
from rich import inspect
from rich.traceback import install
from polygon import Polygon
from quadrado import quadrado
install()

status = "start"

if(status >= "start"):
    status ="ask"
    print(f"Gostaria de ver um quadrado ou um circulo?")
    r = input("")
    if r == "quadrado":
        status = r
    if r == "circulo":
        status = r
    else:
        r2 = input(f"Digite exatamente quadradou ou circulo por gentileza!\n")
if(status == "quadrado" ):
    lado = input(print(f"[blue]Qual a quantidade de lados?[/]\n"))
    lado * quadrado
    

