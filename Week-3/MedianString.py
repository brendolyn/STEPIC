# 38_7

import sys
from itertools import product

out = open("output.txt",'w')
Input = open(sys.argv[1])
Input = Input.read().split("\n")
K = int(Input[0])
Seqs = filter(lambda s: s!='', Input[1:])

def diff(seq1,seq2):
  '''
  hamming distance between two seqs with same length
  '''
  n = 0
  for i in range(len(seq1)):
    if seq1[i]!=seq2[i]:
      n += 1
  return n

def dist(kmer,String):
  '''
  the shortest distance between kmer and string longer than kmer
  '''
  K = len(kmer)
  min_dist = K
  for i in range(len(String)-K+1):
    min_dist = min(min_dist,diff(kmer,String[i:(i+K)]))
    if min_dist == 0:
      break
  return min_dist

min_dist_sum = K*len(Seqs)
for s1 in product("ACGT",repeat=K):
  s1="".join(s1)
  dist_sum = 0
  for s in Seqs:
    dist_sum += dist(s1,s)
  if dist_sum<min_dist_sum:
    pattern = s1
    min_dist_sum = dist_sum

print pattern
    
