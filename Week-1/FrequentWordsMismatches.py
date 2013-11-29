import sys
from itertools import product,combinations
from time import time
'''
python FrequentWordsMismatch.py input.txt
'''

Out=open("output.txt",'w')
Input=open(sys.argv[1])
Input=Input.read().split(" ")
String=Input[0]
K=int(Input[1])
mis=int(Input[2])

def a_match(s1,s2,mis):
  m=0
  match=True
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      m+=1
    if m>mis:
      match=False
      break
  return match

def match_num(P,String,mis):
  num=0
  for i in range(len(String)-len(P)+1):
    if a_match(P,String[i:(i+len(P))],mis):
      num+=1
  return num


Max=0
result_list=[]
t0=time()
pattern_list=[]

for i in range(len(String)-K+1):
  sub=String[i:(i+K)]
  for locs in combinations(range(K),mis):
    for replaces in product("ACGT",repeat=mis):
      p=list(sub)
      for j in range(mis):
        p[locs[j]]=replaces[j]
      p="".join(p)
      if p in pattern_list: continue
      pattern_list.append(p)
      Num=match_num(p,String,mis)
      #print p,Num
      if Num>Max:
        result_list=[p]
        Max=Num
      elif Num==Max:
        result_list.append(p)
  if i%20==0:
    print >> sys.stderr,i,sub+"\r",
'''
for p in product("ACGT",repeat=K):
  p="".join(p)
  Num=match_num(p,String,mis)
  #print p,Num
  if Num>Max:
    result_list=[p]
    Max=Num
  elif Num==Max:
    result_list.append(p)
'''
print "Time: ",(time()-t0)/60, "min"
print >>Out," ".join(result_list)
