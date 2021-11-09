import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from networkx.algorithms import community
from networkx.algorithms import centrality
import os

imdb = "./datasets/imdb_prodco.adj"
plot = "./PLOT"


def shortest_path(src, G):
    visited = {}
    q = []
    q.append(src)
    dist = []
    dist.append(0)
    visited[src] = 0
    while(q):
        curr = q.pop(0)
        for c in G[curr]:
            if(visited.get(c, -1) == -1):
                visited[c] = visited[curr] + 1
                q.append(c)
                dist.append(visited[c])

    return dist

def calc_cent(G, nodes):
    ###centrality = [0]*nodes 
    centrality = [0 for i in range(nodes)]
    for node in range(nodes):
        x_paths = shortest_path(node, G)
        all_paths = sum(x_paths)
        cnt_paths = len(x_paths)
        curr_cent = 0

        if all_paths > 0 and nodes > 1:
            curr_cent = ((cnt_paths - 1) / all_paths) * ((cnt_paths - 1) / (nodes - 1))
        centrality[node] = curr_cent

    return centrality

def top_50(l):
    temp_a = sorted(list(enumerate(l)), key=lambda x: x[1], reverse=True)[ : 50]
    temp_b = [x for x, w in temp_a]

    return temp_b

#read file
f = open(imdb, "r")
adj = f.readlines()
rows, cols = map(int, adj[0].strip().split(","))


# 2A
#graph creation
G = [[] for i in range(rows)]
for line in adj[1 : ]:
    u, v, w = map(int, line.strip().split(","))
    G[u].append(v)
    G[v].append(u)

cent_list = calc_cent(G, rows)
f = open("./output_2_closeness.txt", "w")

for i in range(len(cent_list)):
    output = str(i) + " " + str(cent_list[i]) +"\n"
    f.writelines(output)


# 2B
H = nx.Graph()
for line in adj[1 : ]:
    u, v, w = map(int, line.strip().split(","))
    H.add_edge(u, v)

def_cent_dict = nx.algorithms.centrality.closeness_centrality(H)
def_cent_list = [0 for i in range(rows)]

for key, value in def_cent_dict.items():
    def_cent_list[key] = value

plt.hist(def_cent_list)
plt.xlabel("CENTRALITIES")
plt.ylabel("FREQ.")
plt.savefig(plot + "/closeness_dist.png")
plt.close()


top_50_list = top_50(cent_list)
def_top_50_list = top_50(def_cent_list)
f = open("./output_2.txt", "w")
f.write("#overlaps for Closeness Centrality: " + str(len(list(set(top_50_list) & set(def_top_50_list)))))
