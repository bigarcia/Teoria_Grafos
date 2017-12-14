# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:07:25 2017

@author: Bianca Garcia
"""



from collections import deque

def bfs(G, s):
    
    # dicionário para armazenar os antecessores
    P = {} # estrutura de dados que mapeia uma chave a um valor
    # inicialização do algoritmo 
    for v in G.nodes():
        G.node[v]['color'] = 'white'
        G.node[v]['lambda'] = float('inf')
    
    # iniciar cor da raiz como cinza
    G.node[s]['color'] = 'gray'
    # custo para a raiz é 0
    G.node[s]['lambda'] = 0
    # iniciar fila Q vazia
    Q = deque()
    # inserir nó raiz no início da fila
    Q.append(s)
    
    # enquanto fila não estiver vazia
    while (len(Q) > 0):
        # obter o primeiro elemento da fila
        u = Q.popleft()
        # para cada vertice adjacênte a u
        for v in G.neighbors(u):
            # se v é branco
            if (G.node[v]['color'] == 'white'):
                # atualizar custo de v
                G.node[v]['lambda'] = G.node[u]['lambda'] + 1
                # adicionar u como antecessor de v
                P[v] = u
                # atualizar cor de v
                G.node[v]['color'] = 'gray'
                # incluir v em  Q
                Q.append(v)
        
        # atualizar cor de u
        G.node[u]['color'] = 'black'
    
    # retorna a lista de antecessores
    return P

        