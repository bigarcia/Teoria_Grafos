import matplotlib.pyplot as plt
from collections import deque

def bfs(G, s):
    # dicionário para armazenar os antecessores
    P = {} # estrutura de dados que mapeia uma chave a um valor
    # inicialização do algoritmo 
    bfstxt = open ("BFS.txt", 'w')
    bfstxt.write ("Considere que lambda é a menor custo até o momento para o caminho entre a raíz e o vértice analisado\n")
    for v in G.nodes():
        G.node[v]['color'] = 'white'
        G.node[v]['lambda'] = float('inf')
        bfstxt.write("O vértice {} possui lambda igual a {} e ainda não foi descoberto.\n".format(v,G.node[v]['lambda']))
        
    
    # iniciar cor da raiz como cinza
    G.node[s]['color'] = 'gray'
    bfstxt.write("O vértice {} foi descoberto.\n".format(s))
    
    # custo para a raiz é 0
    G.node[s]['lambda'] = 0
    bfstxt.write("O vértice {} possui lambda igual a {}.\n".format(s,G.node[v]['lambda']))
    # iniciar fila Q vazia
    Q = deque()
    
    # inserir nó raiz no início da fila
    Q.append(s)
    bfstxt.write("A fila de prioridade Q é: {}.\n".format(Q))
   
    
    # enquanto fila não estiver vazia
    while (len(Q) > 0):
        # obter o primeiro elemento da fila
        u = Q.popleft()
        bfstxt.write("\nA fila de prioridade Q é: {}.\n".format(Q))
        # para cada vertice adjacênte a u
        for v in G.neighbors(u):
            # se v é branco
            bfstxt.write("\nPara vértice {} existe o vizinho {}.".format(u,v))
            print("Para vértice {} existe o vizinho {}".format(u,v))
            if (G.node[v]['color'] == 'white'):
                # atualizar custo de v
                G.node[v]['lambda'] = G.node[u]['lambda'] + 1
                bfstxt.write("\nLambda atual do vértice {}: {}".format(v, G.node[v]['lambda']))
                print("Lambda atual do vértice {}: {}".format(v, G.node[v]['lambda']))
                # adicionar u como antecessor de v
                P[v] = u
                # atualizar cor de v
                G.node[v]['color'] = 'gray'
                bfstxt.write("\nVértice {} foi descoberto.".format(v))
                print("Vértice {} foi descoberto".format(v))
                # incluir v em  Q
                Q.append(v)
                bfstxt.write("A fila de prioridade Q é: {}.\n".format(Q))
                
                
        # atualizar cor de u
        G.node[u]['color'] = 'black'
        bfstxt.write("\nVértice {} foi analisado.".format(u))
        print("Vértice {} foi analisado".format(u))
    
    for v in G.nodes():
        bfstxt.write("\nVertice {} tem lambda {}.".format(v, G.node[v]['lambda']))
        print("Vertice {} tem lambda {}".format(v, G.node[v]['lambda']))
    # retorna a lista de antecessores
    return P

        

import networkx as nx

G = nx.read_pajek('karate.paj')
# fazer busca em largura
bfs(G, "1")

pos = nx.random_layout(G)
name = { v: (v) for v, data in G.nodes(data=True) }
nx.draw_networkx_labels(G,pos,labels=name)
nx.draw_networkx_edges(G,pos)
nx.draw(G,pos) 
plt.savefig("BFS.png", dpi=96, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)
with open('matrix.txt','wb') as f:
    np.savetxt(f, P, fmt='%.1f')