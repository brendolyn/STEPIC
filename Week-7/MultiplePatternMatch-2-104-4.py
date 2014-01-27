#======================
## much faster >20X
## but works only when pattern lengths are the same
# =====================


import sys
from time import time

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
patterns=filter(lambda x: x.strip()!='',Input[1:])
out=open("output.txt",'w')

text=text+"$"
t0=time()
index=[]
for i in range(len(text)-len(patterns[1])):
  if text[i:(i+len(patterns[0]))] in patterns:
    index.append(i)

print len(index)
print >>out, " ".join([str(f) for f in index])
print time()-t0
