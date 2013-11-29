#24-4
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
Input = Input.read().split('\n')
N = int(Input[0])

Spec = [int(x) for x in Input[1].split(" ")]
LB = [[]]
LP = []

def Score(seq,Spec):
  score = 1
  Spec_c=copy(Spec)
  for i in range(len(seq)):
    v=0
    for j in range(len(seq)-1):
      v+=seq[(i+j)%len(seq)]
      if v in Spec_c:
        score+=1
        Spec_c.remove(v)
  if sum(seq) in Spec_c: score+=1
  return score

  
def expand(List):
  new_list=[]
  new_score=[]
  for i in List:
    for j in value:
      if sum(i)+j<=max(Spec):
        temp=copy(i)
        temp.append(j)
        new_list.append(temp)
        new_score.append(Score(temp,Spec))
  return new_list,new_score

Max=0
LP=[]
for i in range(200):
  new_list,new_score=expand(LB)
  if len(new_list)==0: break
  LB=[]
  s=max(new_score)
  while len(LB)<N and s>0:
    for j in range(len(new_score)):
      if new_score[j]==s:
        LB.append(new_list[j])
      if new_score[j]==83:
        LP.append(new_list[j])
      if new_score[j]>Max:
        Max=new_score[j]

    s-=1
  print Max,max(new_score),len(LB),len(LP)

print >> out, " ".join(["-".join(str(f) for f in x) for x in LP])
  
  
