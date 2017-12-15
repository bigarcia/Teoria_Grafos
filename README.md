# trab-grafos
Teoria dos Grafos - Professor Alexandre Levada - Universidade Federal de São Carlos - UFSCar
Alunos:
Bianca Garcia Martins RA:606723
Gabriel Tanasovici Nardy RA:726521
Samara M. M. S. Almeida RA:592790

O trabalho proposto nesta disciplina teve como objetivo aprender Teoria dos Grafos na prática, utilizando a linguagem Python.
Serão apresentados os problemas, suas soluções, e pequenas introduções importantes para a sua execução. Para mais detalhes sobre teorias acesse a apostila do professor:
https://github.com/bigarcia/trab-grafos/blob/master/Notas_de_Aula_TG.pdf



PROJETO 1: SNAKES AND LADDERS

Problema:

O problema é baseado no jogo Snakes and Ladders.
Snakes and Ladders é um famoso jogo de tabuleiro em que a cada rodada um jogador joga uma moeda não viciada e avança 1 casa se obtiver cara ou avança 2 casas se obtiver coroa. Se o jogador para no pé da escada, então ele imediatamente sobe para o topo da escada. Se o jogador cai na boca de um cobra então ele imediatamente escorrega para o rabo. O jogador sempre inicia no quadrado de número 1. O jogo termina quando ele atinge o quadrado de número 36.

O objetivo é :

a)
Gerar o diagrama de estados da cadeia de Markov que representa o jogo, computando para isso a matriz de transição de estados P

b)
1.Desenvolver um script em Python para calcular a distribuição estacionária da cadeia de Markov homogênea em questão
2.Encontrar  a probabilidade de um jogador vencer o jogo, ou seja, a probabilidade de se atingir o estado 36 no longo prazo.
3.Para k = 100 um número suficiente de iterações no Power Method, encontrar os estados mais prováveis de serem acessados.

c)
Especificara matriz P_ (P_barra) referente ao modelo Pagerank considerando alpha = 0.1. 
Para k = 100, aplicar o Power method e comparar o resultado com o obtido no item b). 
Determinar se as distribuições estacionárias obtidas em b) e c) são iguais ou diferentes.

Solução:

a)
Antes de resolver o exercício é interessante relembrar o  de Cadeia de Markov:

A cadeia de markov é um processo estocástico caracterizado por seu estado futuro depender apenas do seu estado atual, sendo que os estados passados não influenciam no estado futuro. 

Quando o código é compilado, é gerado a cadeia de Markov resultante no arquivo Markov.png, presente na pasta do projeto, como pode ser visto abaixo
![Imagens](LINK)





b) 



Resolução:
A imagem que representa a cadeia de Markov é gerada na pasta do projeto com o nome Markov.pgn, como pode ser observado abaixo
![Imagens](LINK)





PROJETO 3: BUSCA EM LARGURA E PROFUNDIDADE

O objetivo é Implementar os algoritmos BFS (Breadth- First Search, ou também conhecido como Busca em Largura) e DFS (Depth-First Search, ou também conhecido como Busca em Profundidade)  para extrair as árvores BFS-tree e DFS-tree dos grafos a seguir.

Introdução:

Um algoritmo de busca é um algoritmo que percorre um grafo andando pelas arestas de um vértice a outro, examinando estes sistematicamente. Ele parte de um vértice inicial (raiz) e percorre todos as outras arestas e seus vértices até alcançar um vértice final, sendo que cada aresta é examinado no máximo uma vez.

No BFS a cada novo nível descoberto, todos os vértices daquele nível devem ser visitados antes de prosseguir para o próximo nível.
No DFS  a cada vértice descoberto, explora - se um de seus vizinhos não visitados ( sempre que possível). Imita exploração de labirinto, aprofundando sempre que possível.

Solução:

O primeiro grafo, nomeado de Karate (como mostrado abaixo), é encontrado na pasta do projeto com o nome Karate_Before.pgn e foi construído importando o documento karate.paj, que contém todos os vértices e arestas do grafo.
![Imagens](Karate_Before)

Após a implementação do BFS no grafo original, a seguinte imagem do grafo é gerado na pasta do projeto, com nome BFS_Karate_After.png.
![Imagens](Karate_After)
Todos os passos de execução do BFS são apresentado no BFS_Karate.txt, que se encontra na página do projeto

Após a implementação do DFS no grafo original, a seguinte imagem do grafo é gerado na pasta do projeto, com nome DFS_Karate_After.png
![Imagens](DFS_Karate_After)

O primeiro grafo, nomeado de Dolphins (como mostrado abaixo), é encontrado na pasta do projeto com o nome Dolphins_Before.pgn e foi construído importando o documento karate.paj, que contém todos os vértices e arestas do grafo.
![Imagens](Dolphins_Before)

Após a implementação do BFS no grafo original, a seguinte imagem do grafo é gerado na pasta do projeto, com nome BFS_Karate_After.png.
![Imagens]BFS_Karate_After)
Todos os passos de execução do BFS são apresentado no BFS_Karate.txt, que se encontra na página do projeto

Após a implementação do DFS no grafo original, a seguinte imagem do grafo é gerado na pasta do projeto, com nome DFS_Karate_After.png
![Imagens]DFS_Karate_After)

