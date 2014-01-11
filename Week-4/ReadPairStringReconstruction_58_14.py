#58_14
import sys
sys.setrecursionlimit(5000000)


out = open("output.txt",'w')
Input = open(sys.argv[1],'r').read().split("\n")
d=int(Input[0])
edges=[]
K=len(Input[1])/2

In_out_degree={}
for p in Input[1:]:
  if p == "": continue
  p = [i.strip() for i in p.split("|")]
  e1 = (p[0][:-1],p[1][:-1])
  e2 = (p[0][1:],p[1][1:])
  
  if e1 in In_out_degree:  # record in and out degree
    In_out_degree[e1][1]+=1
  else:
    In_out_degree[e1]=[0,1]

  if e2 in In_out_degree:
    In_out_degree[e2][0]+=1
  else:
    In_out_degree[e2]=[1,0]
    
  edges.append((e1,e2))


# find start and end point
found=0
for i in In_out_degree:
  degree=In_out_degree[i]
  if degree[0] > degree[1]:
    n1 = i
    found +=1
  if degree[1] > degree[0]:
    n2 = i
    found +=1
#  if found>=2:
#    break

print n1
print n2

# find eulerian tour
def find_eulerian_tour(start,graph):
    tour=[]
    tour1=[]
    find_tour(start,graph,tour,tour1)
    return tour,tour1
def find_tour(u,E,tour,tour1): 
  for (a,b) in E:
    if (a==u) and (len(tour1)<(K+d) or tour1[-K-d+1][1]==u[0]):
        tour1.append(u)
        print len(tour1)
        E.remove((a,b))
        find_tour(b,E,tour,tour1)
        tour1.pop()
  tour.insert(0,u)


tour,tour1 = find_eulerian_tour(n2,edges)

print tour[:-1]==tour1
print len(tour1)
S1=tour[0][0]
S2=tour[0][1]
for i in tour[1:]:
  S1+=i[0][-1]
  S2+=i[1][-1]
print S1[(K+d-1):]==S2[:(-K-d+1)]
if S1[(K+d-1):]==S2[:(-K-d+1)]:
  print >>out,S1+S2[(-K-d+1):]

