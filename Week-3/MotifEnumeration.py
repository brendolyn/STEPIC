# 36_7

import sys
from itertools import product

out = open("output.txt",'w')
Input = open(sys.argv[1])
Input = Input.read().split("\n")
K = int(Input[0].split(" ")[0])
d = int(Input[0].split(" ")[1])
Seqs = filter(lambda s: s!='', Input[1:])

def diff(seq1,seq2,d):
  ''' 
  seq1 and seq2 must be same length
  True if difference of seq1/2 no larger than d 
  '''
  n = 0
  for i in range(len(seq1)):
    if seq1[i]!=seq2[i]:
      n += 1
    if n>d:
      return False
  return True

result = []
for s1 in product("ACGT",repeat=K):
  s1="".join(s1)
  for s in Seqs:
    exist_mark = False
    for i in range(len(s)-K+1):
      s2 = s[i:(i+K)]
      if diff(s1,s2,d):
        exist_mark = True
        break
    if not exist_mark:
      break
  if exist_mark:
    result.append(s1)

print >>out, " ".join(result)
        

