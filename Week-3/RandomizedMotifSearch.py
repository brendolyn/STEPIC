#41_4

import sys

out = open("output.txt",'w')
Input = open(sys.argv[1])
Input = Input.read().split("\n")
K = int(Input[0].split(" ")[0])
t = int(Input[0].split(" ")[1])
Seqs = filter(lambda s: s!='', Input[1:])
Seqs = [s.strip() for s in Seqs]

order = {"A":0,"C":1,"G":2,"T":3}

def findMatrix(motifs):
  t = len(motifs)
  matrix=[]
  for i in range(K):
    p = [1.0/(t+4)]*4
    for j in range(t):
      p[order[motifs[j][i]]] += 1.0/(t+4)
    matrix.append(p)
  return matrix

def score(motifs):
  matrix = findMatrix(motifs)
  score = 0
  for p in matrix:
    score += len(motifs)*(1-max(p))
  return score


def Prob(kmer,matrix):
  Prob = 1
  for i in range(K):
    Prob = Prob * matrix[i][order[kmer[i]]]
  return Prob

def findMotif(Seq,matrix):
  max_p = 0
  for i in range(len(Seq)-K+1):
    p = Prob(Seq[i:(i+K)],matrix) 
    if p > max_p:
      motif = Seq[i:(i+K)]
      max_p = p
  if max_p ==0: return Seq[0:K] 
  return motif

from random import randint

min_score = t*K

n=0
while n<1000:
  n+=1
  print >> sys.stderr,"Iteration: %d\r"%(n),
  BestMotifs = []
  for s in Seqs:
    r = randint(0, len(s)-K)
    BestMotifs.append(s[r:(r+K)])
  while True:
    matrix = findMatrix(BestMotifs)
    Motifs = [findMotif(s,matrix) for s in Seqs]
    if score(Motifs)<score(BestMotifs):
      BestMotifs = Motifs
    else:
      break
  if score(BestMotifs)<min_score:
    finalBestMotifs = BestMotifs
    min_score = score(BestMotifs)
    
print >>out, "\n".join(map(str, finalBestMotifs))
