#59_5
import sys
sys.setrecursionlimit(5000000)

out = open("output.txt",'w')
Input = open(sys.argv[1],'r').read().split("\n")

edges={}
In_out_degree={}
for e in Input:
  e1=e[:-1]
  e2=e[1:]

  if e1 in In_out_degree:  # record in and out degree
    In_out_degree[e1][1]+=1
  else:
    In_out_degree[e1]=[0,1]

  if e2 in In_out_degree:
    In_out_degree[e2][0]+=1
  else:
    In_out_degree[e2]=[1,0]

  if e1 in edges:
    edges[e1].append(e2)
  else:
    edges[e1]=[e2]

# search for start positions
starts = []
for n in In_out_degree:
  degree=In_out_degree[n]
  if degree!=[1,1] and degree[1]>0:
    starts.append(n)


routes=[]
for s in starts:
  for i in edges[s]:
    route = s+i[-1]
    while In_out_degree[i]==[1,1]:
      i=edges[i][0]
      route+=i[-1]
    routes.append(route)

print >> out, " ".join(sorted(routes))


