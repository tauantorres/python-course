class Alarme: 

    def __init__(self, estado: bool):
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor


alarme = Alarme(False)
print(f"Estado do alarme: {alarme.get_estado()}")
alarme.set_estado(True)
print(f"Estado do alarme: {alarme.get_estado()}")
