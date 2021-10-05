import os
import shutil
import snap
import sys

file = sys.argv[1]

gr = snap.LoadEdgeList(snap.PUNGraph, file, 0, 1)
results={}

#1
results['cnt_nodes'] = gr.GetNodes()

#2
gr2 = gr
div_3 = []
for i in gr.Nodes():
    x = i.GetId()
    if(x%3 == 0):
        div_3.append(x)

gr2.DelNodes(div_3)
results['cnt_nodes_2'] = gr2.GetNodes()

#3
results['cnt_edges'] = gr.GetEdges()

#4
results['cnt_edges_2'] = gr2.GetEdges()

#5
deg_no = gr.GetDegCnt()
max_deg = 0
n=0
for i in deg_no:
    max_deg = max(max_deg, i.GetVal1())

results['Max_deg'] = max_deg

max_deg_nodes = []
for node in gr.Nodes():
    if node.GetDeg() == max_deg:
        max_deg_nodes.append(node.GetId())

#6
ps = os.getcwd() 
pd = ps+"/plots"
fn = "facebook_combined"
plotFilename = f"shortest_path_{fn}"
snap.PlotShortPathDistr(gr, plotFilename)
if os.path.exists("./plots") == False:
    os.mkdir("./plots")
shutil.move(os.path.join(ps, "diam.shortest_path_facebook_combined.png"), os.path.join(pd, "shortest_path_facebook_combined.png"))

#Part B
#1 
results['fraction_largest_comp'] = gr.GetMxSccSz()

#2
art_pts = gr.GetArtPoints()
results['art_pts_cnt'] = len(art_pts)

#3
comps = gr.GetSccSzCnt()
cnt = 0
for comp in comps:
    cnt += comp.GetVal2()

results['comp_cnt'] = cnt

#4
ps = os.getcwd() 
pd = ps+"/plots"
plotFilename = f"connected_comp_{fn}"
snap.PlotSccDistr(gr, plotFilename)
if os.path.exists("./plots") == False:
    os.mkdir("./plots")    
shutil.move(os.path.join(ps, "scc.connected_comp_facebook_combined.png"), os.path.join(pd, "connected_comp_facebook_combined.png"))

#5
max_comp = gr.GetMxScc()
max_comp_dia = max_comp.GetBfsFullDiam(100, False)
results['max_comp_dia'] = max_comp_dia


#Printing
print("Number of nodes: ",results['cnt_nodes'])
print("Number of nodes after removing nodes with ID=3:  ",results['cnt_nodes_2'])
print("Number of edges: ",results['cnt_edges'])
print("Number of edges after removing nodes with ID=3: ",results['cnt_edges_2'])
print("Number of nodes with highest degree: ",results['Max_deg'])
print("Node IDs of nodes with highest degree: ",max_deg_nodes)
print("Fraction of nodes in the largest connected component: ",results['fraction_largest_comp'])
print("Number of articulation points: ",results['art_pts_cnt'])
print("Number of connected components: ",results['comp_cnt'])
print("Diameter of the largest connected component: ",results['max_comp_dia'])

#Saving results
s1="Number of nodes: {}\n".format(results['cnt_nodes'])
s2="Number of nodes after removing nodes with ID=3:  {}\n".format(results['cnt_nodes_2'])
s3="Number of edges: {}\n".format(results['cnt_edges'])
s4="Number of edges after removing nodes with ID=3: {}\n".format(results['cnt_edges_2'])
s5="Number of nodes with highest degree: {}\n".format(results['Max_deg'])
s6="Node IDs of nodes with highest degree: {}\n".format(max_deg_nodes)
s7="Fraction of nodes in the largest connected component: {}\n".format(results['fraction_largest_comp'])
s8="Number of articulation points: {}\n".format(results['art_pts_cnt'])
s9="Number of connected components: {}\n".format(results['comp_cnt'])
s10="Diameter of the largest connected component: {}\n".format(results['max_comp_dia'])

save_file = open("answers.txt","w")
ans_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
save_file.writelines(ans_list)
save_file.close()