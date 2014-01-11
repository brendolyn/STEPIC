#57_10
import sys
import networkx as nx
from itertools import product
from time import time

out = open("output.txt",'w')
k = int(open(sys.argv[1],'r').read())

for k in range(4,15):
  t1=time()
  print >> out, k
  edges=[]
  for i in product("01",repeat=k-1):
    i = "".join(i)
    i1 = i[1:]+"1"
    i0 = i[1:]+"0"
    edges.append((i,i0))
    edges.append((i,i1))

  G=nx.DiGraph()
  G.add_edges_from(edges)
  if nx.is_eulerian(G):
    nodes = [u for u,v in nx.eulerian_circuit(G)]
    String = nodes[0]
    for n in nodes[1:-k+2]:
      String+=n[-1]
    print >>out, String
    print >> sys.stderr, "Finished!"
  else:
    print "Not Eulerian"
    print G.edges()
  print >> sys.stderr, "K:%d, time: %.2f"%(k,time()-t1)
