# 39_3

import sys
from itertools import product

out = open("output.txt",'w')
Input = open(sys.argv[1])
Input = Input.read().split("\n")
Seq = Input[0].strip()
K = int(Input[1])
order = Input[2].split(" ")
matrix = [[float(x) for x in l.split(" ")] for l in Input[3:(3+K)]]

order = {x[1]:x[0] for x in enumerate(order)}

def Prob(kmer,matrix):
  Prob = 1
  for i in range(K):
    Prob = Prob * matrix[i][order[kmer[i]]]
  return Prob

max_p = 0
for i in range(len(Seq)-K+1):
  p = Prob(Seq[i:(i+K)],matrix) 
  if p > max_p:
    motif = Seq[i:(i+K)]
    max_p = p

print motif
