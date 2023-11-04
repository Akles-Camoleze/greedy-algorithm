# Problema BeeCrowd #1084

## Programação Gulosa
### Akles Pires Camoleze & João Felipe Silva Lamounier

## Abordagem

### Estratégia de Solução
Para resolver este problema, o código utiliza uma abordagem baseada em programação
gulosa, utilizando-se de uma pilha (stack). O algoritmo percorre a sequência de dígitos,
mantendo uma pilha onde os dígitos são empilhados. Ao percorrer a sequência, o algoritmo
compara o dígito atual com o elemento no topo da pilha. Se o dígito atual for maior que o
elemento no topo da pilha e ainda houver dígitos para serem removidos (D > 0), o algoritmo
remove o dígito do topo da pilha e decrementa D. Esse processo é repetido até que o dígito
atual não seja maior que o elemento no topo da pilha ou D seja igual a 0. Após o loop, o
algoritmo remove os dígitos restantes necessários para atender a condição D > 0, realizando
assim o processo de solução do problema.

### Justificativa
A escolha da pilha como estrutura de dados é fundamental para este problema, pois permite
manter uma ordem de dígitos que pode ser facilmente manipulada para atender aos requisitos
de maximização do prêmio. A estratégia de comparação do dígito atual com o elemento no
topo da pilha garante que os dígitos removidos