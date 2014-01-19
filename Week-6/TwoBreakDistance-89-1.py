import networkx as nx
import sys
out=open("output.txt",'w')
Input=open(sys.argv[1],'r').read().split("\n")
genome1=Input[0].strip()
genome2=Input[1].strip()

def reverse(block):
  '''
  change "+"/"-" on block
  '''
  if block.startswith("+"):
    temp="-"+block[1:]
  else:
    temp="+"+block[1:]
  return temp

def add_edges(str):
  global graph
  str=str[:-1].split(" ")
  for i in range(len(str)):
    graph.add_edge(str[i-1],reverse(str[i]))

global graph
graph=nx.Graph()

n=0
for i in genome1.split("("):
  if i=="": continue
  add_edges(i)
  n+=len(i.split(" "))

for i in genome2.split("("):
  if i=="": continue
  add_edges(i)

print n
print n-len(nx.connected_components(graph))

