class Exercicios:
    def __init__(self):
        print('Construtor')

    def exercicio1(self):
        nome_funcionario = "Debora"
        idade = 23
        salario = 3500.00
        cargo = "Analista de Dados"
        turno = "matutino"
        setor = "RH"

        print("Nome do funcionário:", nome_funcionario)
        print("Idade:", idade)
        print("Salário:", salario)
        print("Cargo:", cargo)
        print("Turno:", turno)
        print("Setor:", setor)

# Criando uma instância da classe Exercicios
ex = Exercicios()
ex.exercicio1()

class Exercicios:
    def __init__(self):
        print('Construtor')

    def exercicio1(self):
        print("Resolução do exercício 1")

    def exercicio2(self):
        nome_escola = "Escola Estadual ABC"
        estado = "São Paulo"
        num_professores = 50
        cidade = "São Paulo"
        num_militares = 10
        logradouro = "Rua das Escolas"
        numero_endereco = 123
        num_alunos = 1000
        colegio_militar = False
        disciplinas = ["Matemática", "Português", "Ciências", "História"]

        print("Nome da escola:", nome_escola)
        print("Estado:", estado)
        print("Número de professores:", num_professores)
        print("Cidade:", cidade)
        print("Número de militares:", num_militares)
        print("Logradouro:", logradouro)
        print("Número:", numero_endereco)
        print("Número de alunos:", num_alunos)
        print("Colégio é militar?", "Sim" if colegio_militar else "Não")
        print("Disciplinas:", disciplinas)

# Criando uma instância da classe Exercicios
ex = Exercicios()
ex.exercicio2()

class Exercicios:
    def __init__(self):
        print('Construtor')

    def exercicio1(self):
        print("Resolução do exercício 1") 

    def exercicio3(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"
        valor4 = 8
        valor5 = -5

        print("valor1 + valor2 =", valor1 + valor2)
        print("valor1 + valor2 + valor4 =", valor1 + valor2 + valor4)
        print("valor1 + valor2 - valor5 =", valor1 + valor2 - valor5)

        # Conversão de valor3 para inteiro antes da operação
        print("valor1 + int(valor3) =", valor1 + int(valor3))

        print("valor1 * valor2 =", valor1 * valor2)
        print("(valor4 * valor2) / 2 =", (valor4 * valor2) / 2)

        # Correção do nome da variável de valor4 para valor5
        print("(valor1 + valor2 + valor5) / 4 =", (valor1 + valor2 + valor5) / 4)

ex = Exercicios()
ex.exercicio3()