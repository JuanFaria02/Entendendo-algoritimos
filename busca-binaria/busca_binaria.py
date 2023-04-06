import math

class BuscaBinaria:
    @staticmethod
    def makeSearch(lista, valor):
        valor_inicial = 0
        valor_final = len(lista)-1
        metade = int((valor_final - valor_inicial)/2)
       
        if(lista[metade]==valor):
            return lista[metade]
        elif(valor<lista[metade]):
            return BuscaBinaria.makeSearch(lista[0:metade], valor)
        elif(valor>lista[metade]) :
            return BuscaBinaria.makeSearch(lista[metade+1::], valor)
        elif(valor_final<valor_inicial):
            return None
        
    @staticmethod
    def stepCount(valor):
        return int(math.log2(int(valor)))


if __name__ == "__main__":
    lista = [10,11,13]
    print(lista[0:1])
        