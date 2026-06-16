dict_estoque = {
    'codigo': [],
    'produto': [],
    'tipo': [],
    'valor': [],
    'quantidade': [],
    'data': []
}


class Produto:
    def __init__(self, GTIN, nome_produto, tipo, valor, quantidade, data_importacao):
        self.__GTIN = GTIN
        self.__nome_produto = nome_produto
        self.__tipo = tipo
        self.__valor = valor
        self.__quantidade = quantidade
        self.__data_importacao = data_importacao

    def cadastroEstoque(self):
        dict_estoque['codigo'].append(self.__GTIN)
        dict_estoque['produto'].append(self.__nome_produto)
        dict_estoque['tipo'].append(self.__tipo)
        dict_estoque['valor'].append(self.__valor)
        dict_estoque['quantidade'].append(self.__quantidade)
        dict_estoque['data'].append(self.__data_importacao)

    def removerDoEstoque(self):
        dict_estoque['codigo'].remove(self.__GTIN)
        dict_estoque['produto'].remove(self.__nome_produto)
        dict_estoque['tipo'].remove(self.__tipo)
        dict_estoque['valor'].remove(self.__valor)
        dict_estoque['quantidade'].remove(self.__quantidade)
        dict_estoque['data'].remove(self.__data_importacao)

    def procuraGTIN(self):
        index = 0
        while (index < len(dict_estoque['codigo'])):
            if (self.__GTIN == dict_estoque['codigo'][index]):
                return index
            else:
                index += 1
                return index

    @staticmethod
    def GTIN(self):
        return self.__GTIN

    @property
    def nome(self):
        return self.__nome_produto

    @property
    def tipo(self):
        return self.__tipo

    @property
    def valor(self):
        return self.__valor

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def data(self):
        return self.__data_importacao

    @nome.setter
    def nome(self, novoNome):
        index = self.procuraGTIN()
        dict_estoque['produto'][index] = novoNome

    @tipo.setter
    def tipo(self, novoTipo):
        index = self.procuraGTIN()
        dict_estoque['tipo'][index] = novoTipo

    @valor.setter
    def valor(self, novoValor):
        index = self.procuraGTIN()
        dict_estoque['valor'][index] = novoValor

    @quantidade.setter
    def quantidade(self, novaQuantidade):
        index = self.procuraGTIN()
        dict_estoque['quantidade'][index] = novaQuantidade

    @data.setter
    def data(self, novaData):
        index = self.procuraGTIN()
        dict_estoque['data'][index] = novaData

    def calcularDespesa():
        despesa = 0
        x = 0
        for x in range(len(dict_estoque['valor'])):
            despesa += dict_estoque['valor'][x] * dict_estoque['quantidade'][x]
        print(despesa)

    def mostraEstoque():
        print(f'GTIN: {dict_estoque['codigo']}\nProdutos: {dict_estoque['produto']}\nTipos: {dict_estoque['tipo']}\nValores(R$): {dict_estoque['valor']}\nUnidades: {dict_estoque['quantidade']}\nData de importação: {dict_estoque['data']}')
