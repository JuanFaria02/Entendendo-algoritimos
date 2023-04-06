import busca_binaria

lista_inteiro = [x for x in range(0,128)]
print("Qual o valor inteiro você quer procurar? ")
valor = int(input())
print("Valor buscado: ", busca_binaria.BuscaBinaria.makeSearch(lista_inteiro, valor))
print("Quantidade de passos ", busca_binaria.BuscaBinaria.stepCount(valor))
