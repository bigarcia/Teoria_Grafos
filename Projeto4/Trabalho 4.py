import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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

def Peso(x,y):
   return (G.get_edge_data(x,y,'weight'))

Fila = []
Vfec = []
Pesov = nx.get_node_attributes(G,'distancia')
Pesoe = nx.get_edge_attributes(G, 'distancia')

def relax(u,v,Pesoe):
    if (Pesov[v] > (Pesov[u] + Pesoe[u,v])):
        G.node[v]['distancia'] = G.node[u]['distancia'] + G.edge[u,v]['peso']
        G.node[v]['pi'] = u
        
def remove_menor(Fila,Vfec,s): 
    u = Fila.pop()
    menor = s
    for v in G.neighbors(u):
        if v in Fila:
            if (Pesov[v] < Pesov[menor]):
                menor = v
    return menor
        
        

def Dijkstra(G, Pesoe, s):
    for v in G.nodes:
        G.node[v]['distancia'] = np.inf
        G.node[v]['pi'] = -1
        G.node[s]['distancia'] = 0
        Fila.append(v)
    while (len(Fila) != 0):
        u = remove_menor(Fila,Vfec,s)
        Vfec.append(u)
    for v in nx.neighbors(G,u):
        relax(u,v,Pesoe)

G2 = Dijkstra(G,Pesoe,2)
        
        
    

