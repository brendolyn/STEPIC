#53_6

import sys

out = open("output.txt",'w')
Input = open(sys.argv[1],'r').read().split("\n")
K = int(Input[0])
String = Input[1].strip()

links = {}

for i in range(len(String)-K+1):
  pre = String[i:(i+K-1)]
  suf = String[(i+1):(i+K)]
  if pre not in links:
    links[pre] = [suf]
  else:
    links[pre].append(suf)

for key in sorted(links.iterkeys()):
  print >> out, key+" -> "+",".join(sorted(links[key]))
