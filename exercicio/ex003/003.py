import random

class ContaBancaria:
    """
    Criar uma conta bancaria e permite fazer saque e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo =saldo
        
        Contas = []

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo"

    def deposito(self, valor):
        self.saldo += valor
        print(f"Deposito de {valor:,.2f} autorizado na conta {self.id}")


    def saque(self, valor):
        if valor > self.saldo:
            print(f"saque NEGADO tentativa de saque no valor de {valor:,.2f} saldo em conta {self.saldo:,.2f}")
        else:
         self.saldo -=valor
         print(f"saque de {valor:,.2f} autorizado na conta {self.id}")


def iniciar():
    start = 1

    menu = "inicio"
    while(start > 0):
        if menu == "inicio":
            resposta = ""
            print("Gostaria de criar uma conta nova?")

            resposta = input("sim, não: ")

            if resposta == "sim":
                nome = ""
                print("Insira seu nome")
                nome = input("")
                id = random.randint(100,300)
                ContaBancaria = id , nome

            

    

iniciar()
        
        