class Gafanhoto:
    def __init__(self):
        self.nome = " "
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade."
lista_gafanhas = []
    

def teste():
    quantos = 0
    quantos = int(input("Quantos Gafanhotos:"))

    while(quantos > 0):
        quantos -=1
        g = Gafanhoto()

        g.nome = input("insira seu nominho:")

        g.idade = float(input("insina sua idadizinha:"))
        print(" ")

        lista_gafanhas.append(g)
    if(quantos <= 0):
        for g in lista_gafanhas:
            print(g.mensagem())
            print(" ")

teste()   