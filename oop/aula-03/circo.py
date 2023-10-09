class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Circense:

    def apresentar_show(self, nome: str, habilidade: str): 
        print(f"O {habilidade} {nome} está fazendo seu show!")

class Malabarista(Circense):

    def __init__(self, nome: str):
        self.nome = nome


class Palhaco:

    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_show(self):
        print(f"O palhaço {self.nome} está fazendo seu show!")

class Domador:

    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_show(self):
        print(f"O domador {self.nome} está fazendo seu show!")


# [TESTE]
print("\n")
circo = Circo()
palhaco = Palhaco("Pipoca")

circo.apresentar(palhaco)
print("\n")
