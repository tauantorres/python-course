class Mae:

    def __init__(self, nome, sobrenome, endereco) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco

    def comer(self) -> None:
        print("Estou comendo.")

    def estudar(self) -> None:
        print("Estou estudando.")


class Filha(Mae):

    def __init__(self, nome, endereco=None) -> None:
        super().__init__(nome, "", endereco)  # Inicialize o sobrenome como vazio
        self.nome = nome

    def brincar(self, brinquedo: str) -> None:
        print(f"Estou brincando com {brinquedo}.")


# Exemplo de criação de instâncias
maria = Mae("Maria", "Silva", "Lisboa")
ana = Filha("Ana", endereco="Porto")

# Configurar o sobrenome da mãe após a criação
ana.sobrenome = maria.sobrenome

print(maria.nome, maria.sobrenome, maria.endereco)
print(ana.nome, ana.sobrenome, ana.endereco)
