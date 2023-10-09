class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_dados(nome, idade)
        else:
            self.__indicar_erro()

    # Métodos privados
    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False
    
    def __armazenar_dados(self, nome: str, idade: int) -> None:
        print("Acessando o Banco de Dados...")
        print(f"Cadastrando [{nome}] [{idade}].")

    def __indicar_erro(self) -> None:
        print("Dados inválidos")



# [TESTE] : Cadastro válido
cadastro = SistemaCadastral()
cadastro.cadastrar("Tauan", 18)


# [TESTE] : Cadastro inválido
cadastro = SistemaCadastral()
cadastro.cadastrar(18, "Tauan")
