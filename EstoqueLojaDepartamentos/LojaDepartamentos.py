dict_estoque = {
    'produto': [],
    'quantidade': [],
    'valor': []
}


class LojaDepartamento:
    def __init__(self, GTIN, nome_produto, tipo, valor, quantidade, data_importacao):
        self.__GTIN = GTIN
        self.__nome_produto = nome_produto
        self.__tipo = tipo
        self.__valor = valor
        self.__quantidade = quantidade
        self.__data_importacao = data_importacao

    def DemonstraProduto(self):
        print(f'O Produto {self.__nome_produto}')

    def criarEstoque(self):

    def cadastroProdutos(self):
        self.dict_estoque['produto'].append(self.__nome_produto)

    def mostraEstoque(self):
        return self.__dict_estoque
