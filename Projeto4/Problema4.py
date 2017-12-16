import numpy as np
import networkx as nx
from heapq import heappush as push
from heapq import heappop as pop
from Funcoes_problema4 import abre_matriz,plot,raiz


#Cria p grafo a partir da matriz de adjacências de um arquivo .txt
G = abre_matriz('wg59_dist.txt')


def Dijkstra(G, r1, r2, r3):
    Grafo = G.copy()

    
    for v in Grafo.nodes:
        #Inicilaiza todos os vértices com custo 0
        Grafo.node[v]['lambda'] = np.inf
        Grafo.node[v]['pi'] = None
    
    #Inicializa as raízes das árvores com custo 0
    Grafo.node[r1]['lambda'] = 0
    Grafo.node[r2]['lambda'] = 0
    if r3 != None:
        Grafo.node[r3]['lambda'] = 0
 
    Fila = []
 
    
    for v in Grafo.nodes:
        push(Fila, (Grafo.node[v]['lambda'], v))
 
    Finalizados = []
    
    while Fila:
        #Remove da fila o vértice de menor peso
        menor = pop(Fila)
        menor = menor[1]
        Finalizados.append(menor)
 
        for v in Grafo.neighbors(menor):
            #Se v não está nos finalizados, verifica se há um vértice vizinho de menor custo
            if v not in Finalizados and Grafo.node[v]['lambda'] > (Grafo.node[menor]['lambda'] + Grafo[menor][v]['weight']):
                Fila.remove((Grafo.node[v]['lambda'], v))
                Grafo.node[v]['lambda'] = Grafo.node[menor]['lambda'] + Grafo[menor][v]['weight']
                push(Fila, (Grafo.node[v]['lambda'], v))
                Grafo.node[v]['pi'] = menor
 
    #Cria as árvores de caminhos ótimos
    floresta = nx.Graph()
    for v in Grafo.nodes():
        floresta.add_node(v)
        if Grafo.node[v]['pi'] is not None:
            floresta.add_edge(v, Grafo.node[v]['pi'])
            floresta[v][Grafo.node[v]['pi']]['weight'] = G[v][Grafo.node[v]['pi']]['weight']
    return floresta



#Define as raizes da floresta 1
r1 = raiz(G)
r2 = raiz(G)
#Define as raizes da floresta 2
raiz1 = raiz(G)
raiz2 = raiz(G)
raiz3 = raiz(G)

#Cria a Floresta 1, que tem 2 raizes
Floresta1 = Dijkstra(G, r1, r2, None)

#Cria a Floresta 2, que tem 3 raizes 
Floresta2 = Dijkstra(G, raiz1, raiz2, raiz3) 

#Plota o grafo inicial
plot(G,"Grafo inicial")

#Plota a Floresta 1
plot(Floresta1,"Floresta 1")

#Plota a Floresta 2
plot(Floresta2,"Floresta 2")

        
    

