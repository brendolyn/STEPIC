#51_3

import sys

out = open("output.txt",'w')
Input = open(sys.argv[1]).read().split("\n")
K = int(Input[0])
String = Input[1].strip()

Kmers = []
for i in range(len(String)-K+1):
  Kmers.append(String[i:(i+K)])

Kmers = sorted(Kmers)
Kmers = [i.strip() for i in Kmers]
print >>out,"\n".join(Kmers)
