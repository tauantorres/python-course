from typing import Type


class Interruptor():

    def __init__(self, comodo):
        self.comodo = comodo

    def acender(self):
        print(f"Acendendo a luz do(a) {self.comodo}")

    def apagar(self):
        print(f"Apagando a luz do(a) {self.comodo}")


class Pessoas():

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print("Dormindo...")


# [TESTE]

pessoa = Pessoas()
interruptor = Interruptor("Quarto")
pessoa.acender_luz(interruptor)
pessoa.apagar_luz(interruptor)
pessoa.dormir()
