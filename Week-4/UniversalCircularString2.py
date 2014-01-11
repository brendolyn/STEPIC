#57_10
import sys
import networkx as nx
from itertools import product
from time import time

out = open("output1.txt",'w')
k = int(open(sys.argv[1],'r').read())

def fast_exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exp(x*x, n/2)
    else:
        return x * fast_exp(x, n-1)


for k in range(4,7):
  t1=time()
  print >> out, k
  stack=["".join(["0"]*k)]
  nodes=[]
  while len(nodes)<fast_exp(2,k):
    i=stack.pop()
    nodes.append(i)
    if len(nodes)==fast_exp(2,k):
      break
    i1 = i[1:]+"1"
    i0 = i[1:]+"0"
    if i0 in nodes and i1 in nodes:
      print "MARK"
      i=stack[-1]
      while nodes[-1]!=i[:-1]+"1":
        nodes.pop()
      nodes.pop()
    elif i1 in nodes:
      stack.append(i0)
    elif i0 in nodes:
      stack.append(i1)
    else:
      stack.append(i0)
      stack.append(i1)
  String = nodes[0]
  for n in nodes[1:-k+1]:
    String+=n[-1]
  print >>out, String
  print >> sys.stderr, "Finished!"   
  print >> sys.stderr, "K:%d, time: %.2f"%(k,time()-t1) 
    
