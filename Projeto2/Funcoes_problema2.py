import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random as rd

def abre_matriz(arquivo):
    A = np.loadtxt(arquivo)
    G = nx.from_numpy_matrix(A)
    return G

def cria_labels(G,arquivo):
    B = open("ha30_name.txt", 'r')
    Cidades = []
    for linha in B:
        linha = linha.strip("\n")
        Cidades.append(linha)
    for v in G.nodes():
        G.nodes[v]['label'] = Cidades[v]
    return nx.get_edge_attributes(G,'label')

    for v in G.nodes():
        G.nodes[v]['label'] = Cidades[v]
    return nx.get_node_attributes(G,'label')

def plot(nome,titulo):
    plt.figure(1, figsize=(12, 8))             
    pos=nx.spring_layout(nome)      
    plt.axis('off')
    nx.draw_networkx(nome,pos)
    plt.title(titulo, size=16)
    arquivo = titulo + ".png"
    plt.savefig(arquivo)
    plt.show()

def raiz(G):
    rd.seed(None)
    return rd.randint(0,G.number_of_nodes())