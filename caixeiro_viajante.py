import numpy as np
import networkx as nx
from collections import deque

def Prim(G,r):
    P = {}
    for v in G.nodes():
      G.node[v]['lambda'] = float('inf')
    G.node[r]['lambda'] = 0
    Q = list(G.nodes())
    Q.sort()
    Q = deque(Q)
    S = []  
    
    while (len(Q) > 0):
        # obter o primeiro elemento da fila
        
        u = Q.popleft()
        S.append(u)
        for v in G.neighbors(u):
            w = G.get_edge_data(u,v)['weight']
            if (v in Q and G.node[v]['lambda']>w):
                G.node[v]['lambda'] = w
                P[v] = u
    T = nx.Graph()
    T.add_edges_from([ (u, v) for u, v in P.items() ])
    return T
    

def twice_around (G, r):
    H=[] # se inicia como lista vazia
    T=Prim(G, r)
    for e in T.edges():
        T.add_edge(*e)
    L = Fleury(T, r)
    while(len(L)>0):
        l = L.popleft()
        if l not in H:
            H.insert(l)
    print(H)
        
            
def DFSCount(G, v, visited):
    count = 1
    visited[v] = True
    for i in G.neighbors(v):
        if visited[i] == False:
            count = count + DFSCount(G,i, visited)        
    return count
 
def isValidNextEdge(G, u, v):
   
    if len(list(G.neighbors(u))) == 1:
        return True
    else:
        visited =[False]*(len(list(G.nodes())))
        count1 = DFSCount(G,u, visited)
        data = G.get_edge_data(u, v)
        G.remove_edge(u, v)
        visited =[False]*(len(list(G.nodes())))
        count2 = DFSCount(G,u, visited)
 
       
        G.add_edge(u,v, data=data)
 
    
        return False if count1 > count2 else True
    
  # Print Euler tour starting from vertex u
def EulerUtil(G, u, P):
    #Recur for all the vertices adjacent to this vertex
    for v in G.neighbors(u):
        print(v)
        #If edge u-v is not removed and it's a a valid next edge
        if isValidNextEdge(G,u, v):
            P.append(v)
            G.remove_edge(u, v)
            EulerUtil(G,v)
 
def Fleury(G, u):
    #Find a vertex with odd degree
    P = []
    for i in G.nodes():
        if len(list(G.neighbors(i))) %2 != 0 :
            u = i
            break
    
    EulerUtil(G,u,P)
    return P
    

M = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(M)
twice_around(G, 0)