# Problema BeeCrowd #1084

## Programação Gulosa
### Akles Pires Camoleze & João Felipe Silva Lamounier

## Objetivo
O objetivo do algoritmo é encontrar o maior número possível removendo exatamente d dígitos de um número n.

## Entrada
- n: Tamanho do número de entrada.
- d: Número de dígitos a serem removidos.
- number: O número de entrada como uma sequência de dígitos.

## Condições de Entrada
- O programa verifica se n, d estão na faixa válida: `1 <= d <= 10⁵`.
- Verifica se o comprimento do número de entrada é igual a n.

## Lógica Gulosa

### Escolha Localmente Ótima

Em cada iteração do loop que percorre os dígitos do número de entrada, o algoritmo toma uma decisão localmente ótima. Ele escolhe o dígito mais alto possível para aquela posição específica, levando em consideração os dígitos restantes no número.

### Escolha Gulosa

A escolha gulosa é evidenciada no momento em que o algoritmo decide remover ou manter um dígito. A lógica é remover dígitos que são menores do que os dígitos à sua esquerda, sempre que possível. Isso maximiza o valor do número resultante.

### Remoção de Dígitos

O algoritmo mantém uma pilha (stack) para construir o número resultante. Quando encontra um dígito menor que o último dígito na pilha, ele remove o último dígito da pilha para garantir que o número seja o maior possível. Isso é feito repetidamente até que o número desejado de dígitos (d) tenha sido removido.

## Aspectos Gulosos Específicos
### Remoção de Dígitos Menores

A lógica principal é focada em remover dígitos menores para garantir que o número final seja maximizado. Isso é feito iterativamente enquanto percorre os dígitos do número de entrada.

### Escolha Baseada no Contexto

A decisão de remover um dígito é tomada com base no contexto local, ou seja, considerando o dígito atual e os dígitos que ainda precisam ser processados.

### Por que é Guloso
O algoritmo é guloso porque, em cada passo, toma a decisão que parece ser a melhor localmente, sem considerar as consequências a longo prazo e sem desfazer decisões passadas. A escolha é baseada puramente no contexto imediato, buscando maximizar o valor do número resultante a cada passo.

Em resumo, a programação gulosa neste algoritmo se manifesta na tomada de decisões locais que, esperançosamente, levam a uma solução globalmente ótima para o problema de otimização proposto.
