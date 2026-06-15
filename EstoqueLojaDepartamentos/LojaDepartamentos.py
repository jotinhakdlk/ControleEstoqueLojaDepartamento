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

    def atualizarNome(self, novoNome):
        index = self.GTIN()
        dict_estoque['produto'][index] = novoNome
    
    def atualizarTipo(self, novoTipo):
        index = self.GTIN()
        dict_estoque['tipo'][index] = novoTipo

    def atualizarValor(self, novoValor):
        index = self.GTIN()
        dict_estoque['valor'][index] = novoValor

    def atualizarQuantidade(self, novaQuantidade):
        index = self.GTIN()
        dict_estoque['quantidade'][index] = novaQuantidade

    def atualizarData(self, novaData):
        index = self.GTIN()
        dict_estoque['data'][index] = novaData

    def GTIN(self):
        index = 0
        while(index < len(dict_estoque['codigo'])):
            if(self.__GTIN == dict_estoque['codigo'][index]):
                return index
            else:   
                index += 1
                return index



##self.__nome_produto = dict_estoque['produto'].append()

    def mostraEstoque():
        return f'GTIN: {dict_estoque['codigo']}\nProdutos: {dict_estoque['produto']}\nTipos: {dict_estoque['tipo']}\nValores(R$): {dict_estoque['valor']}\nUnidades: {dict_estoque['quantidade']}\nData de importação: {dict_estoque['data']}'
    
