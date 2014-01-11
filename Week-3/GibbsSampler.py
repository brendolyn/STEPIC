#43_4

import sys
import random

out = open("output.txt",'w')
Input = open(sys.argv[1])
Input = Input.read().split("\n")
K = int(Input[0].split(" ")[0])
t = int(Input[0].split(" ")[1])
N = int(Input[0].split(" ")[2])
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

def rand_dist(p_dist):
  '''  random number based on a discret distribution '''
  Sum = sum(p_dist)
  r = random.uniform(0.0,Sum)
  n = 0
  while True:
    r -= p_dist[n]
    if r < 0:
      break 
    n += 1
  return(n)
  
def findMotif(Seq,matrix):
  p_dist=[]
  for i in range(len(Seq)-K+1):
    p_dist.append(Prob(Seq[i:(i+K)],matrix)) 
  r = rand_dist(p_dist)
  motif = Seq[r:(r+K)] 
  return motif

n = 0
min_score = t*K
while n < 20:
  n+=1
  print >> sys.stderr,"Iteration: %d\r"%(n),
  BestMotifs = []
  for s in Seqs:
    r = random.randint(0, len(s)-K)
    BestMotifs.append(s[r:(r+K)])
  for i in range(N):
    j = random.randint(0, t-1)
    tempMotifs=[]
    for k in range(t):
      if k!=j: tempMotifs.append(BestMotifs[k])
    matrix = findMatrix(tempMotifs)
    motif = findMotif(Seqs[j],matrix)
    Motifs = BestMotifs[:]
    Motifs[j] = motif
    if score(Motifs)<score(BestMotifs):
      BestMotifs = Motifs
      
  if score(BestMotifs)<min_score:
    finalBestMotifs = BestMotifs
    min_score = score(BestMotifs)
    
print >>out, "\n".join(map(str, finalBestMotifs))
  
