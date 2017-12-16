
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappush
from heapq import heappop
import random as rd


#Cria p grafo a partir da matriz de adjacências de um arquivo .txt
A = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(A)


#Cria labels para os nós a partir de um arquivo .txt com o nome das cidades
B = open("wg59_name.txt", 'r')
Cidades = []
for linha in B:
    linha = linha.strip("\n")
    Cidades.append(linha)

for v in G.nodes():
    G.nodes[v]['label'] = Cidades[v]
    

plt.figure(1, figsize=(12, 8))             
pos=nx.spring_layout(G)      
plt.axis('off')                            
nx.draw_networkx_nodes(G,pos,node_size=50) 
nx.draw_networkx_edges(G,pos,alpha=0.4)    
plt.title('Distância', size=16)     
plt.show()

def Dijkstra(G, r1, r2, r3):
    Grafo = G.copy()
 
    for v in Grafo.nodes:
        Grafo.node[v]['lambda'] = np.inf
        Grafo.node[v]['pi'] = None
 

    Grafo.node[r1]['lambda'] = 0
    Grafo.node[r2]['lambda'] = 0
    if r3 != None:
        Grafo.node[r3]['lambda'] = 0
 
    Q = []
    
    for v in Grafo.nodes:
        heappush(Q, (Grafo.node[v]['lambda'], v))
 
    visitados = []
    
    while Q:
        v_menorCusto = heappop(Q)
        v_menorCusto = v_menorCusto[1]
        visitados.append(v_menorCusto)
 
        for i in Grafo.neighbors(v_menorCusto):
            if i not in visitados and Grafo.node[i]['lambda'] > (Grafo.node[v_menorCusto]['lambda'] + Grafo[v_menorCusto][i]['weight']):
                Q.remove((Grafo.node[i]['lambda'], i))
                Grafo.node[i]['lambda'] = Grafo.node[v_menorCusto]['lambda'] + Grafo[v_menorCusto][i]['weight']
                heappush(Q, (Grafo.node[i]['lambda'], i))
                Grafo.node[i]['pi'] = v_menorCusto
 
    floresta = nx.Graph()
    for v in Grafo.nodes():
        floresta.add_node(v)
        if Grafo.node[v]['pi'] is not None:
            floresta.add_edge(v, Grafo.node[v]['pi'])
            floresta[v][Grafo.node[v]['pi']]['weight'] = G[v][Grafo.node[v]['pi']]['weight']
    return floresta



#Cria uma raiz aleatória para iniciar o algoritmo
rd.seed(None)
#Define as raizes da floresta 1
r1 = rd.randint(0,G.number_of_nodes())
r2 = rd.randint(0,G.number_of_nodes())
#Define as raizes da floresta 2
raiz1 = rd.randint(0,G.number_of_nodes())
raiz2 = rd.randint(0,G.number_of_nodes())
raiz3 = rd.randint(0,G.number_of_nodes())


Floresta1 = Dijkstra(G, r1, r2, None)
 
Floresta2 = Dijkstra(G, raiz1, raiz2, raiz3) 

#Plota a floresta 1
plt.figure(1, figsize=(12, 8))             
pos=nx.spring_layout(Floresta1)      
plt.axis('off')                            
nx.draw_networkx_nodes(Floresta1,pos,node_size=100) 
nx.draw_networkx_edges(Floresta1,pos,alpha=0.4)    
plt.title('Floresta 1', size=16)     
plt.show()

#Plota a floresta 2
plt.figure(1, figsize=(12, 8))             
pos=nx.spring_layout(Floresta2)      
plt.axis('off')                            
nx.draw_networkx_nodes(Floresta2,pos,node_size=100) 
nx.draw_networkx_edges(Floresta2,pos,alpha=0.4)    
plt.title('Floresta 2', size=16)     
plt.show() 
        
    

