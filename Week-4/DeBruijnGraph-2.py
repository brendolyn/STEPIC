#54_7

import sys

out = open("output.txt",'w')
Input = open(sys.argv[1],'r').read().split("\n")
Strings = [s.strip() for s in Input if s!=""]

links = {}

for s in Strings:
  pre = s[:-1]
  suf = s[1:]
  if pre not in links:
    links[pre] = [suf]
  else:
    links[pre].append(suf)

for key in sorted(links.iterkeys()):
  print >> out, key+" -> "+",".join(sorted(links[key]))
