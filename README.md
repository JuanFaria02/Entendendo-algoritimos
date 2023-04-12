# Entendendo-algoritimos
Repositório criado para os códigos usados nos exercícios do livro Entendendo Algoritmos.

## Busca binária

O primeiro ensinamento do livro Entendo os algorítmos é a respeito da Busca Binária. Ela consiste em procurar um valor em uma lista ordenada consumindo menos tempo e realizando menos passos. 

##### Exemplo: Temos uma lista com 10 números ordenados de forma crescente, se formos buscar o valor 1 realizaremos apenas um passo mas se quisermos o valor 10 executaremos 10 passos e se a lista for de 1000 termos e quisermos o milésimo termo, executaremos 1000 passos e assim a complexidade e o tempo de resposta cresce linearmente. Porém, temos uma forma de executar menos passos e deixar o problema mais eficiente e menos complexo, esse é o algoritmo da busca binária que foi escrito nesse exercício.

A busca binária é feita pegando o valor do meio da lista e comparando com o valor desejado, se o valor desejado for maior que o encontrado então a dividiremos novamente pela metade do valor posterior caso o valor desejado seja maior e o anterior caso seja menor até que encontre o valor desejado. 

## Complexidade

A complexidade de um algoritmo é denotada pelo tempo de execução do mesmo. A notação que informa se ele é rápido ou não é a notação Big O, ele mede o tempo de execução de um algoritmo pois eles crescem a taxas diferentes. 

##### Exemplo: Se possuímos uma lista com 10 números ordenados de forma crescente, se formos buscar o valor 1 realizaremos apenas um passo mas se quisermos o valor 10 executaremos 10 passos e se a lista for de 1000 termos e quisermos o milésimo termo, executaremos 1000 passos e assim a complexidade e o tempo de resposta cresce linearmente, portanto, temos a notação O(n), se usarmos então busca binária para essa busca então temos os passos caindo de forma logaritma. No caso dos 1000 termos temos por volta de 9.96 ms, a notação é a O(log n). 

Outras notações do mais rápido para o mais lento são: 

* O(log n)
* O(n)
* O(n * log n)
* O(n²)
* O(n!)
