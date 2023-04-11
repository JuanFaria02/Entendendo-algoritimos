import busca_binaria
if __name__ == "__main__":
    lista = [x for x in range(2,100)]
    for i in lista:
        print()
        print(busca_binaria.BuscaBinaria.makeSearch(lista, i))
        print(busca_binaria.BuscaBinaria.stepCount(i))
        print()
