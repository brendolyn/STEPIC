import sys
from time import time

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
patterns=filter(lambda x: x.strip()!='',Input[1:])
out=open("output.txt",'w')

text=text+"$"

t0=time()

def BWT_match(s,perm,p,suffixArray):
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
  index+=BWT_match(bwt,perm,p,suffixArray)

print len(index)
print >>out, " ".join([str(f) for f in sorted(index)])

print time()-t0
