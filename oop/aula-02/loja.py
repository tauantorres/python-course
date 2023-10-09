class Loja: 

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco


    def get_endereco(self) -> None:
        return self.__endereco

    @classmethod
    def vender(cls) -> float:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: float) -> None:
        cls.tarifa = nova_tarifa


# [TESTE]

print("\n\n", "="*50, "\n")
praia = Loja("Rua da Praia")
centro = Loja("Rua do Centro")

print(f"  Endereço da loja da Praia: {praia.get_endereco()}")
print(f"  Endereço da loja do Centro: {centro.get_endereco()}")

print("\n","< ANTES >".center(50, "-"), "\n")

print(f"  Valor da venda na loja da Praia: {praia.vender()}")
print(f"  Valor da venda na loja do Centro: {centro.vender()}")

print("\n", "< DEPOIS >".center(50, "-"), "\n")

centro.alterar_tarifa(10)
print(f"  Valor da venda na loja da Praia: {praia.vender()}")
print(f"  Valor da venda na loja do Centro: {centro.vender()}")

print("\n", "="*50, "\n\n")
