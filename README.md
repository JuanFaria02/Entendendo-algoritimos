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

## Memória

A memória é um item muito importante ao se criar um programa mas, apesar disso, alguns programadores acabam não se importando com o gasto da memória. Segundo o livro, a memória é como um armário com diversas gavetas em que cada gaveta é um SLOT. Se por algum motivo tivermos que guardar algo e não couber em um armário teremos que utilizar o outro que pode não ser o seguinte pois o seguinte já está ocupado. Nesse caso o que se deve fazer é a alocação de memória, no caso do exemplo é reservar o armário do lado para caso precise usá-lo. 

## Lista e Arrays 

Listas e Arrays são duas estruturas de dados que apesar de parecidas devem ser usadas em situações diferentes. 

**Array**: É uma estrutura de dados fixa na qual a memória é alocada previamente e os objetos são inseridos sequencialmente. Para acessar um objeto em um array, temos uma complexidade de O(1), pois podemos localizá-lo pelo seu índice, como se estivesse "guardado no armário ao lado". No entanto, quando é necessário inserir um objeto após o espaço alocado ter sido preenchido, todos os objetos precisam ser movidos para um novo espaço, o que tem uma complexidade de O(n). Se o array não estiver cheio, cada objeto precisa ser movido para acomodar a inserção, o que também pode ter complexidade O(n).
 
Dessa forma, um array é uma estrutura de dados eficiente para operações de busca, mas pode se tornar ineficiente para inserções e remoções de elementos, especialmente quando o tamanho do array está fixo e precisa ser realocado para acomodar as mudanças.

**Listas**: São estruturas de dados semelhantes aos arrays, mas ao contrário deles, não é necessário alocar a memória sequencialmente. Em uma lista, cada objeto é alocado em um espaço de memória e possui um ponteiro para o espaço de memória do objeto seguinte. Como não há índices predefinidos, as listas não são eficientes para buscas, pois é necessário percorrer um por um até encontrar o objeto desejado, resultando em uma complexidade O(n).

Por outro lado, as listas são muito eficientes para inserções e remoções, pois não é necessário alocar um novo espaço de memória ou mover os objetos. Em vez disso, basta atualizar os ponteiros dos objetos vizinhos. Isso resulta em uma complexidade menor para essas operações, o que as torna mais eficientes do que os arrays para situações em que os objetos precisam ser adicionados ou removidos continuamente.

Portanto, embora as listas não sejam eficientes para operações de busca, elas são uma ótima escolha quando a adição ou remoção de objetos é uma prioridade.
