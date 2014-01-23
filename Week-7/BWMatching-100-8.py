import sys

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
patterns=Input[1].strip().split(" ")
out=open("output.txt",'w')

def BWT_match(s,perm,p):
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
   return len(indexs)

perm = sorted(range(len(text)), key=lambda x: text[x])

print "order generated"

i=0
for p in patterns:
  i+=1
  if i%100==0:
    print >>sys.stderr,"%d/%d\r"%(i,len(patterns)),
  print >>out, BWT_match(text,perm,p),
