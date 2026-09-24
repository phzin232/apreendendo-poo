from rich import print, inspect
from classs import Aluno, Pessoa, Funcionario

def main():
    a1 = Aluno("josé", 17, "informatica", "T01")
    a1.fazer_matricula
    a1.estudar
    a1.fazer_aniversario
    
    inspect(a1)




if __name__ == "__main__":
    main()