class Cadastro: 
    def __init__(self,nome,idade,saldo,statusCadastro):
        self.nome = nome
        self.idade = idade 
        self.saldo = saldo
        self.tatusCadastro = statusCadastro 

    def exibir_info(self):
        print("Nome:",self.nome)
        print("Saldo:", self.saldo)
        print("Status do Cadastro:", self.statusCadastro)

# Exemplo de uso:
if __name__ == "__main__":
    # Criando um objeto da classe Cadastro
    pessoa1 = Cadastro("João", 30, 1000.50, "Ativo")
    
    # Exibindo as informações do objeto
    pessoa1.exibir_info()

    class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro, endereco):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_saldo(saldo)
        self.set_statusCadastro(statusCadastro)
        self.set_endereco(endereco)

    def set_nome(self, nome):
        if len(nome) > 0:
            self.nome = nome
        else:
            raise ValueError("O nome não pode ser vazio.")

    def set_idade(self, idade):
        if idade >= 18:
            self.idade = idade
        else:
            raise ValueError("A idade precisa ser maior ou igual a 18 anos.")

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.saldo = saldo
        else:
            raise ValueError("O saldo não pode ser negativo.")

    def set_statusCadastro(self, statusCadastro):
        if statusCadastro:
            self.statusCadastro = statusCadastro
        else:
            raise ValueError("O status do cadastro precisa ser verdadeiro.")

    def set_endereco(self, endereco):
        if len(endereco) >= 3:
            self.endereco = endereco
        else:
            raise ValueError("O endereço precisa ter pelo menos 3 letras.")

    def exibir_info(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Saldo:", self.saldo)
        print("Status do Cadastro:", self.statusCadastro)
        print("Endereço:", self.endereco)

# Exemplo de uso:
if __name__ == "__main__":
    # Criando um objeto da classe Cadastro
    pessoa1 = Cadastro("João", 30, 1000.50, True, "Rua A")
    
    # Exibindo as informações do objeto
    pessoa1.exibir_info()