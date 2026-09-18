from rich import print, inspect
from aluno import Aluno
from funcionario import Funcionario
from professor import Professor




def main():
    a1 = Aluno("josé", 17, "informatica", "T01")

    inspect(a1)


if __name__ == "__main__":
    main()