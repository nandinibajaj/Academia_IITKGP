import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from networkx.algorithms import community
import os

dataset = "./datasets"
plots = "./PLOT"
football = os.path.join(dataset, "football.gml")
polbooks = os.path.join(dataset, "polbooks.gml")

#1a
def gen_comm_GN(G, ground_truth):
    comm = list(list(community.girvan_newman(G))[ground_truth-2])
    return comm

def gen_comm_clauset(G):
    comm = list(community.greedy_modularity_communities(G))
    return comm

#1b
def comm_distrib_GN(G, data):
    comm_dist = []

    for comm in G:
        comm_dist.append(len(comm))

    plt.hist(comm_dist)
    plt.xlabel("COMMUNITIES")
    plt.ylabel("FREQ.")
    img = plots + "/" + data + "_Newman-Girvan_dist.png"
    plt.savefig(img)
    plt.close() 

def comm_distrib_clauset(G, data):
    comm_dist = []

    for comm in G:
        comm_dist.append(len(comm))

    plt.hist(comm_dist)
    plt.xlabel("COMMUNITIES")
    plt.ylabel("FREQ.")
    img = plots + "/" + data + "_Clauset_dist.png"
    plt.savefig(img)
    plt.close() 

#1c
def comm_distrib_default(G, data):
    communities = {}

    for node in G.nodes:
        if G.nodes[node]['value'] not in communities:
            communities[G.nodes[node]['value']] = set()
        communities[G.nodes[node]['value']].add(node)

    comm_dist = [] #nodes, edges, community
    for index in communities:
        temp = [len(communities[index]), 
                len(G.subgraph(communities[index]).edges), 
                communities[index]]
        comm_dist.append(temp)
    #comm_dist = sorted(comm_dist)

    x = []
    for n in comm_dist:
        x.append(n[0])

    plt.hist(x)
    plt.xlabel("COMMUNITIES")
    plt.ylabel("FREQ.")
    img = plots + "/ground_truth_communities_dist_" + data + ".png"
    plt.savefig(img)
    plt.close()

    return comm_dist  

#1d
def top_5_comm(G, communities, data, method):
    com_size = []
    i = 1
    for com in communities:
        com_size.append([len(com), len(G.subgraph(com).edges)])
    
    com_size = sorted(com_size)
    if(len(com_size)>=5):
        s = 5
    else:
        s = len(com_size)
    for i in range(s):
        #no mention of method in the print statement
        s5 = "Dataset: " + data + "\n Community" + str(i+1) + ": (number_of_nodes = " + str(com_size[len(com_size)-i -1][0]) + ", number_of_edges = " + str(com_size[len(com_size)-i -1][1]) + ")\n"
        if method == "Newman-Girvan":
            save_file_GN.writelines(s5)
            save_file_GN.writelines("\n")
        else:
            save_file_C.writelines(s5)
            save_file_C.writelines("\n")

        #print(s5)
    

#1e, 1f
def Jaccard_GN(G, newman_comm, def_comm, data):
    #jaccard between GN topmost community and topmost ground truth community
    GN_comm = []
    for c in newman_comm:
        GN_comm.append([len(c), len(G.subgraph(c).edges), c])
    #print(GN_comm[0])

    GN_comm = sorted(GN_comm)
    def_comm = sorted(def_comm)

    string = []
    if(len(GN_comm)>=5):
        s = 5
    else:
        s = len(GN_comm)
    for i in range(s):
        c = float(GN_comm[len(GN_comm)-1][1])/len(G.edges())
        string.append("Dataset:" + data + "\n coverage of community " + str(i+1) + "=" + str(c) +"\n")
        save_file_GN.writelines(string[i])
        #print (string[i])
    save_file_GN.writelines("\n")

    intersecting = len(GN_comm[len(GN_comm)-1][2] and def_comm[len(def_comm)-1][2])
    unioned = GN_comm[len(GN_comm)-i-1][0] + def_comm[len(GN_comm)-1][0] - intersecting
    #print(intersecting, unioned)

    jacc = float(intersecting)/unioned
    s6 = "Dataset: " + data + "\n Jaccard coefficient = " + str(jacc) + "\n"
    save_file_GN.writelines(s6)
    save_file_GN.writelines("\n")

def Jaccard_C(G, Clauset_comm, def_comm, data):
    
    C_comm = []
    for c in Clauset_comm:
        C_comm.append([len(c), len(G.subgraph(c).edges), c])

    C_comm = sorted(C_comm)
    def_comm = sorted(def_comm)

    string = []
    if(len(C_comm)>=5):
        s = 5
    else:
        s = len(C_comm)
    for i in range(s):
        c = float(C_comm[len(C_comm)-i-1][1])/len(G.edges())
        string.append("Dataset:" + data + "\n coverage of community " + str(i+1) + "=" + str(c) +"\n")
        save_file_C.writelines(string[i])
        #print (string[i])
    save_file_C.writelines("\n")

    intersecting = len(C_comm[len(C_comm)-1][2] and def_comm[len(def_comm)-1][2])
    unioned = C_comm[len(C_comm)-1][0] + def_comm[len(C_comm)-1][0] - intersecting
    #print(intersecting, unioned)

    jacc = float(intersecting)/unioned
    s7 = "Dataset: " + data + "\n Jaccard coefficient = " + str(jacc) + "\n"
    save_file_C.writelines(s7)
    save_file_C.writelines("\n")
    
#########

#1a
football = nx.read_gml(football)
polbooks = nx.read_gml(polbooks)

football_comm_GN = gen_comm_GN(football, 12)
polbooks_comm_GN = gen_comm_GN(polbooks, 3)

GN_football_com_size = len(football_comm_GN)
GN_polbooks_com_size = len(polbooks_comm_GN)

football_comm_C = gen_comm_clauset(football)
polbooks_comm_C = gen_comm_clauset(polbooks)

C_football_com_size = len(football_comm_C)
C_polbooks_com_size = len(polbooks_comm_C)

#Write in txt file
s1 = "Dataset: Football\n Number of communities using Newman-Girvan method:" + str(GN_football_com_size) + "\n"
s2 = "Dataset: Football\n Number of communities using Clauset method:" + str(C_football_com_size) + "\n"
s3 = "Dataset: Polbooks\n Number of communities using Newman-Girvan method:" + str(GN_polbooks_com_size) + "\n"
s4 = "Dataset: Polbooks\n Number of communities using Clauset method:" + str(C_polbooks_com_size) + "\n"

save_file_GN = open("output_1_NEWMAN.txt","a")
ans_list_GN = [s1,s3,"\n"]
save_file_GN.writelines(ans_list_GN)
#save_file.close()

save_file_C = open("output_1_CLAUSET.txt","a")
ans_list_C = [s2,s4,"\n"]
save_file_C.writelines(ans_list_C)
#save_file.close()

#1b
comm_distrib_GN(football_comm_GN, "Football")
comm_distrib_GN(polbooks_comm_GN, "Polbooks")

comm_distrib_clauset(football_comm_C, "Football")
comm_distrib_clauset(polbooks_comm_C, "Polbooks")

#1c
football_default = comm_distrib_default(football, "Football")
polbooks_default = comm_distrib_default(polbooks, "Polbooks")
#check why we need method

#1d
#print
top_5_comm(football, football_comm_GN, "Football", "Newman-Girvan")
top_5_comm(football, football_comm_C, "Football", "Clauset")
top_5_comm(polbooks, polbooks_comm_GN, "Polbooks", "Newman-Girvan")
top_5_comm(polbooks, polbooks_comm_C, "Polbooks", "Clauset")

#1e,f
#txt file add
Jaccard_GN(football, football_comm_GN, football_default, "Football")
Jaccard_GN(polbooks, polbooks_comm_GN, football_default, "Polbooks")

#txt file add
Jaccard_C(football, football_comm_C, football_default, "Football")
Jaccard_C(polbooks, polbooks_comm_C, football_default, "Polbooks")

save_file_C.close()
save_file_GN.close()


