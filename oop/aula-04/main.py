from repositorio import Repositorio
from database import PostgresDB, MysqlDB


banco_MYSQL = MysqlDB()
banco_POSTGRES = PostgresDB()

repositorio = Repositorio()

print("\n")
repositorio.select(banco_MYSQL)
repositorio.select(banco_POSTGRES)
print("\n")
repositorio.insert(banco_MYSQL)
repositorio.insert(banco_POSTGRES)
print("\n")
