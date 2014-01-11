#57_2
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
if nx.is_eulerian(G):
  nodes = [u for u,v in nx.eulerian_circuit(G)]
  nodes.append(nodes[0])
  print >>out, "->".join(str(n) for n in nodes)
  print >> sys.stderr, "Finished!"
else:
  print "Not Eulerian"
  print G.edges()
    
