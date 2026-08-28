class ContaBancaria:
    """
    Criar uma conta bancaria e permite fazer saque e depositos
     """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo =saldo

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




c1 = ContaBancaria(112, "Pablo", 3000)
c1.deposito(5000)
c1.saque(2000)
print(c1)

