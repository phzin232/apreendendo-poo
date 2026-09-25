from polygon import Polygon


class Quadrado(Polygon):
   def __init__(self, tam_lado):
       self.tam_lado = tam_lado
   qtd_lado = 4
   
   def perimitry(self):
      
        perimitro = self.tam_lado * self.qtd_lado
        return perimitro
   
   def area(self):
    area = self.tam_lado **2
    return area
      

