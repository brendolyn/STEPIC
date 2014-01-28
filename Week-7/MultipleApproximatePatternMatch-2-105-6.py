# ===============================
# == much fast using str.find() =
# ===============================

import sys
from time import time

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
patterns=filter(lambda x: x.strip()!='',Input[1].strip().split(" "))
d=int(Input[2])
out=open("output.txt",'w')

#text=text+"$"

t0=time()

def BWT_match(s,perm,p,suffixArray,start):
   '''
   s: bwt(text);
   p: pattern
   '''
   indexs=filter(lambda x: s[x]==p[0], range(len(s)))
   i=1
   while i<len(p):
     indexs=filter(lambda x: s[perm[x]]==p[i],indexs)
     indexs=[perm[x] for x in indexs]
     i+=1
   return [suffixArray[x]-len(p)-start for x in indexs]



def split_into(n, d):
    l = n / d
    a = n % d
    s = 0
    for _ in range(d):
        e = s + l
        if a > 0:
            a -= 1
            e += 1
        yield s, e
        s = e

def ApproxMatch(s1,s2,d):
  assert(len(s1)==len(s2))
  k=0
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      k+=1
    if k>d:
      return False
  return True

def find_all(a_str, sub):
  start = 0
  while True:
    start = a_str.find(sub, start)
    if start == -1: return
    yield start
    start += len(sub)


'''
dualText=text+text
rotation=[]
for i in range(len(text)):
  rotation.append(dualText[i:(i+len(text))])


suffixArray=[]
bwt=""
for i in sorted(enumerate(rotation), key=lambda x:x[1]):
  suffixArray.append(i[0])
  bwt+=i[1][-1]


perm = sorted(range(len(bwt)), key=lambda x: bwt[x])
'''

indexs=[]
i=0
count=[]
for p in patterns:
  i+=1
  if i%100==0:
    print >>sys.stderr,"%d/%d\r"%(i,len(patterns)),
  index=[]
  for (s,e) in split_into(len(p),d+1): 
    kmer=p[s:e]
    #index+=BWT_match(bwt,perm,kmer,suffixArray,s)
    for k in find_all(text,kmer):
      k=k-s
      if k>0 and k<=len(text)-len(p) and k not in index:
        index.append(k)
  #index=filter(lambda x: (x>0) and (x<=len(text)-len(p)), list(set(index)))
  #print index
  #if len(index)==0: continue
  try:
    temp=filter(lambda x: ApproxMatch(text[x:(x+len(p))],p,d), index)
    indexs+=temp
    count.append(len(temp))
  except:
    print index

print {j: count.count(j) for j in set(count)}
print '\n',len(indexs),len(patterns)
print >>out, " ".join([str(f) for f in sorted(indexs)])

print time()-t0
