# 74_7

import sys
sys.setrecursionlimit(100000)

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
start=int(Input[0])
end=int(Input[1])
edges={}
in_nodes={}
for i in Input[2:]:
  if i.strip()=='': continue
  i=i.split(":")
  n1=int(i[0].split("->")[0])
  n2=int(i[0].split("->")[1])
  edges[(n1,n2)]=int(i[1])
  if n2 in in_nodes:
    in_nodes[n2].append(n1)
  else:
    in_nodes[n2]=[n1]

s=[0]*(end+1) # store the max length
backtrack=[0]*(end+1)

for j in range(start+1,end+1):
  if j not in in_nodes: continue
  for n in in_nodes[j]:
    if (n!=start) and s[n]==0: continue
    if s[n]+edges[(n,j)]>s[j]:
      s[j]=s[n]+edges[(n,j)]
      backtrack[j]=n

print >>out,s[end]

n=end
route=[]
while n!=start:
  route.insert(0,n)
  n=backtrack[n]

route.insert(0,start)
print >>out,"->".join([str(f) for f in route])
  

