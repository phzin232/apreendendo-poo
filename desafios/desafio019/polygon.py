from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados



    @abstractmethod
    def perimitry(self):
        pass
    
    @abstractmethod
    def area():
        pass