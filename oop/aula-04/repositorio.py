class Repositorio:

    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f"Conectado ao banco de dados {connection}")
        print("SELECT * FROM tabela")
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f"Conectado ao banco de dados {connection}")
        print("INSERT INTO tabela VALUES (1, 'valor')")
        db_connection.desconectar()
        