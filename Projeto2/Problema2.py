from Funcoes_problema2 import abre_matriz,plot,raiz
import numpy as np
import networkx as nx
from heapq import heappush as push
from heapq import heappop as pop


G = abre_matriz("ha30_dist.txt")

raiz = raiz(G)


def PRIM(G,raiz):
    Grafo = G.copy()
    nodes = Grafo.nodes()
 
    for n in nodes:
        #define o peso de todos os nós como infinito
        Grafo.node[n]['lambda'] = np.inf
        Grafo.node[n]['pi'] = None

    #Define o peso da raiz como 0 
    Grafo.node[raiz]['lambda'] = 0
 
    #Fila de prioridades
    Fila = []
    #Vértice finalizados
    Finalizados = []
 
    for n in nodes:
        push(Fila, (Grafo.node[n]['lambda'], n))
 
    while (len(Fila)!=0):
        #Remove da fila o vértice de menor prioridade
        u = pop(Fila)
        u = u[1]
        Finalizados.append(u)
        for v in Grafo.neighbors(u):
            #Se o vértice ainda estiver na fila, verifica se a aresta vizinha tem custo menor
            if ((not v in Finalizados) and (Grafo.node[v]['lambda'] > Grafo[u][v]['weight'])):
                #Remove o vértice de maior custo
                Fila.remove((Grafo.node[v]['lambda'], v))
                Grafo.node[v]['lambda'] = Grafo[u][v]['weight']
                push(Fila, (Grafo.node[v]['lambda'], v))
                #Atualiza a fila de predecessores
                Grafo.node[v]['pi'] = u
 
    Arvore = nx.Graph()
    for u in Grafo.nodes():
        Arvore.add_node(u)
        if Grafo.node[u]['pi'] is not None:
            Arvore.add_edge(u, Grafo.node[u]['pi'])
            Arvore[u][Grafo.node[u]['pi']]['weight'] = Grafo[u][Grafo.node[u]['pi']]['weight']
    return Arvore

#Gera a MST
G2 = PRIM(G,raiz)
                

#Plota o Grafo inicial
plot(G, "Grafo_prim") 

#Plota a MST
plot(G2,"MST")
                
            
        

        
        
        
    
        
        
    
        
               
        
    
    
    
    
    
    
    