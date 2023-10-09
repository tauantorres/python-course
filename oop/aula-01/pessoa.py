class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def beber(self, bebida):
        if bebida == 'cerveja' and self.idade < 18:
            print('Não pode beber')

        elif bebida == 'cerveja' and self.idade >= 18:
            print('Mostrar o CPF: ', self.__cpf)

        else:
            print(f'Bebendo {bebida}')

    
tauan = Pessoa('Tauan', 18, '123.456.789-00')
tauan.beber('cerveja')