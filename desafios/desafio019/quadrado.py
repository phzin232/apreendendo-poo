from polygon import Polygon


class Quadrado(Polygon):
   def __init__(self, tam_lado):
       self.tam_lado = tam_lado
   qtd_lado = 4
   
   def perimitry(self):
      
    return self.tam_lado * self.qtd_lado
        
   
   def area(self):
    return self.tam_lado ** 2
    
  
      

