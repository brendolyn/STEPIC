#26-7
import sys
out = open("output.txt",'w')
Input = open(sys.argv[1],'r')
Input=Input.read().split("\n")
M = int(Input[0])
N = int(Input[1])
Spec = [int(x) for x in Input[2].split(" ")]


#######################
## Convolution ########
#######################
Spec = sorted(Spec)
convo={}
for i in range(len(Spec)):
  for j in range(i+1,len(Spec)):
    diff = Spec[j]-Spec[i]
    if diff>=57 and diff<200:
      if diff in convo:
        convo[diff]+=1
      else:
        convo[diff]=1

value = []
c = max(convo.values())
print c
while len(value)<M:
  for i in convo:
    if convo[i]==c:
      value.append(i)
  c-=1
print convo
print "Amino Acids: " + " ".join(str(f) for f in value)


#########################
#### LeaderBoard ########
#########################
from copy import copy

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
        if new_score[j]==Max:
          LP.append(new_list[j])  
        elif new_score[j]>Max:
          Max=new_score[j]
          LP=[new_list[j]]


    s-=1
  print Max,max(new_score),len(LB),len(LP)

  
print >> out, " ".join(["-".join(str(f) for f in x) for x in LP])
