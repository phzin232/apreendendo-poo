class Gafanhoto:
    """Essa classe é feita para criar pessoas como gafanhoto
    """

    lista_gafanhas = []

    def __init__(self, nome ="" , idade = 0):
        self.nome = nome
        self.idade = idade
        Gafanhoto.lista_gafanhas.append(self)

    def aniversario(self):
        self.idade += 1

    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.nome}"
    
    def __str__(self):
     return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade."
    

def teste():
    quantos = 0
    quantos = int(input("Quantos Gafanhotos:"))

    while(quantos > 0):
        quantos -=1
       
        nome = input("insira seu nominho:")

        idade = float(input("insina sua idadizinha:"))

        print(" ")

        Gafanhoto(nome, idade)
        
    if(quantos <= 0):
        for g in Gafanhoto.lista_gafanhas:
        
            print(g.__str__)
            print(g.__getstate__())

teste()   


