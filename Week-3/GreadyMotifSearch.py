# 39_5

import sys

out = open("output.txt",'w')
Input = open(sys.argv[1])
Input = Input.read().split("\n")
K = int(Input[0].split(" ")[0])
t = int(Input[0].split(" ")[1])
Seqs = filter(lambda s: s!='', Input[1:])

order = {"A":0,"C":1,"G":2,"T":3}

def findMatrix(motifs):
  t = len(motifs)
  matrix=[]
  for i in range(K):
    p = [0.0,0.0,0.0,0.0]
    for j in range(t):
      p[order[motifs[j][i]]] += 1.0/t
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



BestMotifs = []
for s in Seqs:
  BestMotifs.append(s[0:K])

for i in range(len(Seqs[0])-K+1):
  motif0 = Seqs[0][i:(i+K)]
  Motifs = [motif0]
  for j in range(1,t):
    matrix = findMatrix(Motifs)
    Motif = findMotif(Seqs[j],matrix)
    Motifs.append(Motif)
  assert len(Motifs) == len(BestMotifs)

  if score(Motifs)<score(BestMotifs):
    BestMotifs = Motifs

print >>out, "\n".join(map(str, BestMotifs))  
  
