import os
import shutil
import snap
import sys

file = sys.argv[1]

gr = snap.LoadEdgeList(snap.PNGraph, file, 0, 1)
results = {}

#Part A
#a
results['cnt_nodes'] = gr.GetNodes()

#b
results['cnt_edges'] = gr.GetEdges()

#Part B
#a
results['cnt_deg4_nodes'] = gr.CntDegNodes(4)

#b
un_gr = gr.GetUnDir()
ps = os.getcwd()
pd = ps+"/plots"
fn = "Email"
plotFilename = "deg-dist"
snap.PlotInDegDistr(un_gr, plotFilename)
if os.path.exists("./plots") == False:
    os.mkdir("./plots")
shutil.move(os.path.join(ps, "inDeg.deg-dist.png"), os.path.join(pd, "deg-dist.png"))
  
#Part C
#a
max_wcc = gr.GetMxWcc()
results['max_wcc_cnt_nodes'] = max_wcc.GetNodes()
results['max_wcc_cnt_edges'] = max_wcc.GetEdges()

#b
max_scc = gr.GetMxScc()
results['max_scc_cnt_nodes'] = max_scc.GetNodes()
results['max_scc_cnt_edges'] = max_scc.GetEdges()

#D
avg_cluster_coeff, cc_vec = gr.GetClustCf(True, -1)
results['avg_cluster_coeff'] = avg_cluster_coeff

#E
tri = gr.GetTriadsAll(-1)
results['triangle_cnt'] = tri[0]

gr2 = snap.LoadEdgeList(snap.PNGraph, file, 0, 1)
cnt = 0
for nx in gr2.Nodes():
    for ny in gr2.Nodes():
        if(nx.GetId() != ny.GetId()):
            cnt_shared_neigh, shared_neigh_list = gr2.GetCmnNbrs(nx.GetId(), ny.GetId(), True)
            cnt += (cnt_shared_neigh*(cnt_shared_neigh-1))//2
        else:
            continue
    gr2.DelNode(nx.GetId())

results['rectangle_cnt'] = cnt


#F
strong_bridges = 0
cnt2 = 0

#before deletion
comps = gr.GetSccSzCnt()
cnt = 0
for comp in comps:
    cnt += comp.GetVal2()

for nx in gr.Nodes():
    for ny in gr.Nodes():
        if(gr.IsEdge(nx.GetId(),ny.GetId()) == True):
            gr2 = snap.LoadEdgeList(snap.PNGraph, file, 0, 1)
            #after deletion
            gr2.DelEdge(nx.GetId(),ny.GetId())
            comps = gr2.GetSccSzCnt()
            cnt2 = 0
            for comp in comps:
                cnt2 += comp.GetVal2()
            
            if(cnt < cnt2):
                strong_bridges += 1


#Printing
print("Number of nodes: ",results['cnt_nodes'])
print("Number of edges: ",results['cnt_edges'])
print("Number of nodes with degree=4: ",results['cnt_deg4_nodes'])
print("Number of nodes in largest weakly connected component: ",results['max_wcc_cnt_nodes'])
print("Number of edges in largest weakly connected component: ",results['max_wcc_cnt_edges'])
print("Number of nodes in largest strongly connected component: ",results['max_scc_cnt_nodes'])
print("Number of edges in largest strongly connected component: ",results['max_scc_cnt_edges'])
print("Average clustring coefficient: ",results['avg_cluster_coeff'])
print("Number of trangles: ",results['triangle_cnt'])
print("Number of rectangles: ",results['rectangle_cnt'])
print("Number of edge bridges: ", strong_bridges)

#Saving in answers.txt
s1="Number of nodes: {}\n".format(results['cnt_nodes'])
s2="Number of edges: {}\n".format(results['cnt_edges'])
s3="Number of nodes with degree=4: {}\n".format(results['cnt_deg4_nodes'])
s4="Number of nodes in largest weakly connected component: {}\n".format(results['max_wcc_cnt_nodes'])
s5="Number of edges in largest weakly connected component: {}\n".format(results['max_wcc_cnt_edges'])
s6="Number of nodes in largest strongly connected component: {}\n".format(results['max_scc_cnt_nodes'])
s7="Number of edges in largest strongly connected component: {}\n".format(results['max_scc_cnt_edges'])
s8="Average clustring coefficient: {}\n".format(results['avg_cluster_coeff'])
s9="Number of trangles: {}\n".format(results['triangle_cnt'])
s10="Number of rectangles: {}\n".format(results['rectangle_cnt'])
s11="Number of edge bridges: {}\n".format(strong_bridges)

save_file = open("answers.txt","w")
ans_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]
save_file.writelines(ans_list)
save_file.close()