import sys
from time import time

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
patterns=filter(lambda x: x.strip()!='',Input[1].strip().split(" "))
d=int(Input[2])
out=open("output.txt",'w')

text=text+"$"

t0=time()

def BWT_approx_match(s,perm,p,suffixArray,d):
   '''
   s: bwt(text);
   p: pattern;
   d: mismatch allowed
   '''
   indexs=range(len(s))
   misArray=map(lambda x: 1-int(s[x]==p[0]),range(len(s)))
   i=1
   while i<len(p):
     assert(len(indexs)==len(misArray))
     indexs=[perm[x] for x in indexs]
     misArray=map(lambda x: misArray[x]+1-int(s[indexs[x]]==p[i]),range(len(misArray)))
     temp=filter(lambda x: misArray[x]<=d,range(len(misArray)))
     misArray=list(misArray[i] for i in temp)
     indexs=list(indexs[i] for i in temp)
     i+=1
   return [suffixArray[x]-len(p) for x in indexs]

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

index=[]
i=0
for p in patterns:
  i+=1
  if i%100==0:
    print >>sys.stderr,"%d/%d\r"%(i,len(patterns)),
  k=int(len(p)/(d+1))
  j=0
  kmerMatch=False
  while (kmerMatch==False) and (j<=len(p)-k):
    kmer=p[j:(j+k)]
    if text.find(kmer)!=-1:
      kmerMatch=True
    j+=1
  if kmerMatch:  
    index+=BWT_approx_match(bwt,perm,p,suffixArray,d)

print len(index)
print >>out, " ".join([str(f) for f in sorted(index)])

print time()-t0
