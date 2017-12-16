import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def twice_around(G, r):
	R = nx.Graph()
	T = nx.MultiGraph(nx.minimum_spanning_tree(G))
	
	for e in list(T.edges()):
		T.add_edge(*e)

	Q = list(nx.eulerian_circuit(T, r))
	P = list()
	for u,v in Q:
		P.append(u)
		P.append(v)
	P = list(set(P))

	for i in range(len(P)-1):
		now = P[i]
		fol = P[i+1]
		data = G.get_edge_data(now, fol)
		R.add_edge(now, fol, data=data)

	return R

def weight_sum(G): 
	total = 0
	for e in G.edges():
		total += G.get_edge_data(*e)['data']['weight']
	return total

# Load
M = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(M)

# Para 10 raizes aleatórias
for r in range(10):
    # Twice'Round
    R = twice_around(G, 0)

    # Weigth
    print(weight_sum(R))

    # Draw graph
    nx.draw_networkx(R, nx.spring_layout(R))

    # Draw to image
    plt.savefig("Caixeiro_{}.png".format(r), dpi=96, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1)
    plt.show()
    plt.close()
	
	