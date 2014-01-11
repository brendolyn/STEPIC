#57_6
import sys
import networkx as nx

out = open("output.txt",'w')
Input = open(sys.argv[1],'r').read().split("\n")
edges=[]
for e in Input:
  if e == "": continue
  e = e.split(" -> ")
  for i in e[1].split(","):
    if i != "":
      edges.append((e[0],i))

G=nx.DiGraph()
G.add_edges_from(edges)

found = 0
for n in G.nodes_iter():
  if G.in_degree(n) > G.out_degree(n):
    n1 = n
    found +=1
  if G.out_degree(n) > G.in_degree(n):
    n2 = n
    found +=1
  if found>=2:
    break

G.add_edge(n1,n2)
print n2 + "->" + n1


if nx.is_eulerian(G):
  nodes = []
  temp_nodes = []
  start = False
  for u,v in nx.eulerian_circuit(G,source=n1):
    if (u == n1) and (v == n2):
      start = True
    if start:
      nodes.append(v) 
    else:
      temp_nodes.append(v)
  nodes += temp_nodes
  String=nodes[0] ## store the final result
  for n in nodes[1:]:
    String+=n[-1]
  print >>out, String
  print >> sys.stderr, "Finished!"
else:
  print "Not Eulerian"
  print G.edges()
