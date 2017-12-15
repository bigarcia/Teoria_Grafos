import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random as rd



#Cria p grafo a partir de uma matriz em um arquivo .txt
A = np.loadtxt('Distancias.txt')
G = nx.from_numpy_matrix(A)


#Cria labels para os nós a partir de um arquivo .txt com o nome das cidades
B = open("Nomes.txt", 'r')
Cidades = []
for linha in B:
    linha = linha.strip("\n")
    Cidades.append(linha)

for v in G.nodes():
    G.nodes[v]['label'] = Cidades[v]
    

plt.figure(1, figsize=(12, 8))             
pos=nx.spring_layout(G)      
plt.axis('off')                            
nx.draw_networkx_nodes(G,pos,node_size=0) 
nx.draw_networkx_edges(G,pos,alpha=0.4)    
plt.title('Distância', size=16)     
plt.show()


rd.seed(None)
#Define o vértice de início
raiz = rd.randint(0,29)

Node = G.nodes() 
lambd = nx.get_node_attributes(G,'weight')       
     
def MST_PRIM(G,raiz):
    Vertices = {}
    Fila = {}
    for v in G.nodes():
        Vertices[v] = Node[v]
    Fila = dict(Vertices)
    Fila[raiz].lambd = 0
    while Fila:
        u = Node('min')
        for tag,v in Fila.items():
            if(u.lambd > v.lambd):
                u = v
        Fila.pop(u.tag,u)
        for v in G.neighbors(u.tag):
            if(v in Fila and (Fila[v].lambd > G[u.tag][v]['weight'])):
                Vertices[v].lambd = G[u.tag][v]['weight']
                Vertices[v].pi = u.tag
        arvore = nx.Graph()
        Vertices.pop(raiz,None)
        for v in Vertices:
            arvore.add_edge(Vertices[v].tag,Vertices[v].pi,weight=Vertices[v].lambd)
        return arvore
                
G2 = MST_PRIM(G,0)
                
            

plt.figure(1, figsize=(12, 8))             
pos=nx.spring_layout(G2)      
plt.axis('off')                            
nx.draw_networkx_nodes(G2,pos,node_size=100) 
nx.draw_networkx_edges(G2,pos,alpha=0.4)    
plt.title('Distância', size=16)     
plt.show() 
                
            
        

        
        
        
    
        
        
    
        
               
        
    
    
    
    
    
    
    