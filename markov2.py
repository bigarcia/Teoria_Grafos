# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:08:33 2017

@author: Bianca Garcia
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class DiGraph():
    G = nx.DiGraph()
    N= nx.DiGraph()
    P=np.zeros((37,37)) # Adicinou-se uma linha a mais, uma vez que não será considerado os vértices 0 (i=0 e j=0)
     
    for n in range (1,36):
        # Adicionando arestas especiais ( escadas e cobras) e seus pesos
        G.add_path(range(n,n+1))
        if n==2:
            G.add_edge(n,15, weight = 1)
            P[n][15] = 1.0
        elif n==5:
            G.add_edge(n,7, weight = 1)
            P[n][7] = 1.0
        elif n==9:
            G.add_edge(n,27,weight = 1)
            P[n][27] = 1.0
        elif n==17:
            G.add_edge(n,4,weight = 1)
            P[n][4] = 1
        elif n==18:
            G.add_edge(n,29,weight = 1)
            P[n][29] = 1
        elif n==20:
            G.add_edge(n,6,weight = 1)
            P[n][6] = 1
        elif n==24:
            G.add_edge(n,16,weight = 1)
            P[n][16] = 1
        elif n==25:
            G.add_edge(n,35,weight = 1)
            P[n][35] = 1
        elif n==32:
            G.add_edge(n,30,weight = 1)
            P[n][30] = 1
        elif n==34:
            G.add_edge(n,12,weight = 1)
            P[n][12] = 1
        elif n==35:
            G.add_edge(n,36,weight = 1)
            P[n][36] = 1
         #Adicionando vértices comuns (anda uma ou duas casas)   
        else:
            G.add_edge(n,n+1, weight = 0.5)
            P[n][n+1] = 0.5
            G.add_edge(n,n+2, weight = 0.5)
            P[n][n+2] = 0.5
            
    pos = nx.shell_layout(G)
    name = { v: (v) for v, data in G.nodes(data=True) }
    dist = dict([((u,v,),data['weight']) for u,v,data in G.edges(data=True)]) 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=dist)
    nx.draw_networkx_labels(G,pos,labels=name)
    nx.draw_networkx_edges(G,pos)
    nx.draw(G,pos) 
    plt.savefig("graph.png", dpi=96, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)
    with open('matrix.txt','wb') as f:
        np.savetxt(f, P, fmt='%.1f')
     
            
    plt.show();
    print (P)
    plt.close();
 
    #distribuição estacionária
    w=np.zeros(36)
    w[35]=1
    for k in range(100):
        aux = []
        aux.append(0)
        for ln in range(1,36):
            ai = 0
            for col in range(1,36):
                ai += w[col]*P[ln][col]
            aux.append(ai)
        w = aux
    max=0
    # imprime a distribuição de probabilidades em %
    for i in range(36):
        print("%d: %.5f" %(i+1, w[i]*100))
    
    
    wo = list(w)
    wo.sort()
    wo.reverse()
    print(" ")
    print ("w ordenado: ")
    print (wo)
    print(" ")
    print("TOP")
    for woi in wo[:5]:
        print("%d: %.5f" %(w.index(woi), woi*100))
        
    
        
