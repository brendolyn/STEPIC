#22-4
import sys
from copy import copy
out = open("output.txt",'w')
table_file = open("integer_mass_table.txt",'r')
table={}
for l in table_file.read().split("\n"):
  l=l.strip().split(" ")
  table[l[0]]=int(l[1])

value = [table[x] for x in table]
value = set(value)

Input = open(sys.argv[1],'r')
Spec = [int(x) for x in Input.read().split(" ")]
List = [[]]

def Spectrum(seq,Spec):
  spec = [0]
  for i in range(len(seq)):
    v=0
    for j in range(len(seq)-i):
      v+=seq[(i+j)%len(seq)]
      if v not in Spec:
        return False
  return sum(seq) in Spec


def expand(List):
  new_list=[]
  for i in List:
    for j in value:
      if sum(i)+j in Spec:
        temp=copy(i)
        temp.append(j)
        if Spectrum(temp,Spec):
          new_list.append(temp)
  return new_list

Max=0

while Max<max(Spec):
  List=expand(List)
  Max=max([sum(x) for x in List])

print >>out, " ".join(["-".join(str(x) for x in y) for y in List])
        
