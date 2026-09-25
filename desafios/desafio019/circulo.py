from polygon import Polygon
from math import pi

class Circulo(Polygon):
    def __init__(self,tam_raio):
        self.tam_raio = tam_raio



    def perimitry(self):
        
       return 2* pi * self.tam_raio

    def area(self):
       return self.tam_raio **2 * pi
   
    def diametro(self):
      return self.tam_raio * 2
     