import matplotlib.pyplot as plt
from collections import deque

def bfs(G, s):
    # dicionário para armazenar os antecessores
    P = {} # estrutura de dados que mapeia uma chave a um valor
    # inicialização do algoritmo 
    bfskaratetxt = open ("BFS_Karate.txt", 'w')
    bfskaratetxt.write ("Considere que lambda é a menor custo até o momento para o caminho entre a raíz e o vértice analisado\n")
    
    for v in G.nodes():
        G.node[v]['color'] = 'white'
        G.node[v]['lambda'] = float('inf')
        bfskaratetxt.write("O vértice {} possui lambda igual a {} e ainda não foi descoberto.\n".format(v,G.node[v]['lambda']))
       
        
    
    # iniciar cor da raiz como cinza
    G.node[s]['color'] = 'gray'
    G.node[v]['lambda'] = 0
   
    bfskaratetxt.write("O vértice {} foi descoberto.\n".format(s))
    
    # custo para a raiz é 0
    G.node[s]['lambda'] = 0
   
    bfskaratetxt.write("O vértice {} possui lambda igual a {}.\n".format(s,G.node[v]['lambda']))
    # iniciar fila Q vazia
    Q = deque()
    
    # inserir nó raiz no início da fila
    Q.append(s)
    
    bfskaratetxt.write("A fila de prioridade Q é: {}.\n".format(Q))
   
    print("\nVerificar o arquivo bfs.txt para analisar as alterações geradas nos vértices e arestas pelo algoritmo\n")
    # enquanto fila não estiver vazia
    while (len(Q) > 0):
        # obter o primeiro elemento da fila
        u = Q.popleft()
       
        bfskaratetxt.write("\nA fila de prioridade Q é: {}.\n".format(Q))
        # para cada vertice adjacênte a u
        for v in G.neighbors(u):
            # se v é branco            
            bfskaratetxt.write("\nPara vértice {} existe o vizinho {}.".format(u,v))
            print("Para vértice {} existe o vizinho {}".format(u,v))
            if (G.node[v]['color'] == 'white'):
                # atualizar custo de v
                G.node[v]['lambda'] = G.node[u]['lambda'] + 1
                bfskaratetxt.write("\nLambda atual do vértice {}: {}".format(v, G.node[v]['lambda']))
                print("Lambda atual do vértice {}: {}".format(v, G.node[v]['lambda']))
                # adicionar u como antecessor de v
                P[v] = u
                # atualizar cor de v
                G.node[v]['color'] = 'gray'
                bfskaratetxt.write("\nVértice {} foi descoberto.".format(v))
                print("Vértice {} foi descoberto".format(v))
                # incluir v em  Q
                Q.append(v)
                bfskaratetxt.write("A fila de prioridade Q é: {}.\n".format(Q))
                
                
        # atualizar cor de u
        G.node[u]['color'] = 'black'
        bfskaratetxt.write("\nVértice {} foi analisado.".format(u))
        print("Vértice {} foi analisado".format(u))
    
    for v in G.nodes():
        bfskaratetxt.write("\nVertice {} tem lambda {}.".format(v, G.node[v]['lambda']))
        print("Vertice {} tem lambda {}".format(v, G.node[v]['lambda']))
    # retorna a lista de antecessores
    return P

def dfs(G, s):
    P = {}
    for u in G.nodes():
        P[u] = None
        G.node[u]['color'] = 'white' # ainda não foi visitado
    dfs_visit(G, s, P)
    return P

def dfs_visit(G, u, P):
    G.node[u]['color'] = 'gray'
    for v in G.neighbors(u):
        if G.node[v]['color'] == 'white':
            P[v] = u
            dfs_visit(G, v, P)


import networkx as nx

G = nx.read_pajek('karate.paj')
# fazer busca em largura
P = bfs(G, "1")
# árvore da busca em largura
T = nx.Graph()
# inserir arestas em T
T.add_edges_from([ (u, v) for u, v in P.items() ])

#Antes do BFS
pos = nx.random_layout(G)
name = { v: (v) for v, data in G.nodes(data=True) }
print("\nGrafo original\n")
print("Para visualizar a imagem de forma ampliada, abra BFS_Karate_Before.png na pasta do projeto\n")
#imprimindo grafo
nx.draw_networkx_labels(G,pos,labels=name)
nx.draw_networkx_edges(G,pos)
nx.draw(G,pos) 
plt.savefig("Karate_Before.png", dpi=96, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)
plt.show()
plt.close()

#Após BFS
pos = nx.spring_layout(T)
name = { v: (v) for v, data in G.nodes(data=True) }
print("\nGrafo após aplicação do BFS\n")
print("Para visualizar a imagem de forma ampliada, abra BFS_Karate_After.png na pasta do projeto\n")
#imprimindo grafo
nx.draw_networkx_labels(T,pos,labels=name)
nx.draw_networkx_edges(T,pos)
nx.draw(T,pos)
plt.savefig("BFS_Karate_After.png", dpi=96, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)
plt.show()
plt.close()



#DFS
P = dfs(G, "1")
T = nx.Graph()
T.add_edges_from([ (u, v) for u, v in P.items() ])

pos = nx.spring_layout(T)
name = { v: (v) for v, data in G.nodes(data=True) }
print("\nGrafo após aplicação do DFS\n")
print("Para visualizar a imagem de forma ampliada, abra DFS_Karate_After.png na pasta do projeto\n")
nx.draw_networkx_labels(T,pos,labels=name)
nx.draw_networkx_edges(T,pos)
nx.draw(T,pos)
plt.savefig("DFS_Karate_After.png", dpi=96, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)
plt.show()
plt.close()

