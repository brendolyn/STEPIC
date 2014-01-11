#52_7
import sys

out = open("output.txt",'w')
Input = open(sys.argv[1],'r').read().split("\n")
Strings = [s.strip() for s in Input if s!=""]

Strings = sorted(Strings)
print >> sys.stderr, "number of strings: %d"%(len(Strings))

for s1 in Strings:
  for s2 in Strings:
    if s1[1:] == s2[:-1]:
      print >> out, s1+" -> "+s2

