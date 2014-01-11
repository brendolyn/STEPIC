# 90-2
import sys
import string,time

def rc(dna):
  complements = string.maketrans('acgtrymkbdhvACGTRYMKBDHV', 'tgcayrkmvhdbTGCAYRKMVHDB')
  rcseq = dna.translate(complements)[::-1]
  return rcseq

out=open("output.txt",'w')
Input=open(sys.argv[1],'r').read().split("\n")
k=int(Input[0])
str1=Input[1].strip()
str2=Input[2].strip()

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

str2_rc=rc(str2)
t0=time.time()
for i in range(len(str1)-k+1):
  kmer1=str1[i:(i+k)]
  if i%1000==0:
    t1=time.time()
    print >>sys.stderr, "%d/%d, time:%.2f\r"%(i,len(str1)-k+1,t1-t0),
  for j in find_all(str2,kmer1):
    print >>out,(i,j)
  for j in find_all(str2_rc,kmer1):
    print >>out,(i,len(str2)-j-k)
