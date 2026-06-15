from LojaDepartamentos import Produto

produto1 = Produto(782531, "Camiseta Ardidas", "Camiseta M", 50.00, 100, "06/07/2067")
produto2 = Produto(123456, "Cola-Cola", "Refrigerante 1L", 12, 10, "12/01/2008")

produto1.cadastroEstoque()
produto2.cadastroEstoque()
produto1.atualizarNome("Teste")
print(Produto.mostraEstoque())

# Objetivo: ADICIONAR AS PROPRIEDADES DO OBJETO (EX: produto1) DENTRO DO DICIONÁRIO dict_estoqu
