class PostgresDB:

    def __init__(self) -> None:
        self.__connection = "\033[34m[PostgresDB]\033[0m"

    def conectar(self) -> str:
        print("\033[32m[CONECTAR]\033[0m")
        return self.__connection
    

    def desconectar(self) -> str:
        print("\033[31m[DESCONECTAR]\033[0m")
        return self.__connection
    
