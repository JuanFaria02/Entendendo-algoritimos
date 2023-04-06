# Entendendo-algoritimos
Repositório criado para os códigos usados nos exercícios do livro Entendendo Algoritmos.

## Busca binária

O primeiro ensinamento do livro Entendo os algorítmos é a respeito da Busca Binária. Ela consiste em procurar um valor em uma lista ordenada consumindo menos tempo e realizando menos passos. 

##### Exemplo: Temos uma lista com 10 números ordenados de forma crescente, se formos buscar o valor 1 realizaremos apenas um passo mas se quisermos o valor 10 executaremos 10 passos e se a lista for de 1000 termos e quisermos o milésimo termo, executaremos 1000 passos e assim a complexidade e o tempo de resposta cresce linearmente. Porém, temos uma forma de executar menos passos e deixar o problema mais eficiente e menos complexo, esse é o algoritmo da busca binária que foi escrito nesse exercício.

A busca binária é feita pegando o valor do meio da lista e comparando com o valor desejado, se o valor desejado for maior que o encontrado então a dividiremos novamente pela metade do valor posterior caso o valor desejado seja maior e o anterior caso seja menor até que encontre o valor desejado. 
