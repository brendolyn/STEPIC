# 77_7

import sys


out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
S1=Input[0].strip()
S2=Input[1].strip()

p = -2 # penalty for indel
n=len(S1)
m=len(S2)


s=[[0]*(m+1) for i in range(n+1)]
backtrack = [[0]*(m+1) for i in range(n+1)]

def score(c1,c2):
  if c1==c2:
    return 1
  else:
    return -2


for j in range(1,(m+1)):
  s[0][j]=s[0][j-1]+p
  backtrack[0][j]=2

Max=0
for i in range(1,(n+1)):
  for j in range(1,(m+1)):
    s[i][j]=max(s[i][j-1]+p,s[i-1][j]+p,s[i-1][j-1]+score(S1[i-1],S2[j-1]))
    if (s[i][j]==s[i-1][j-1]+score(S1[i-1],S2[j-1])):
      backtrack[i][j]=3
    elif s[i][j]==s[i][j-1]+p:
      backtrack[i][j]=2
    else:
      backtrack[i][j]=1
    if (i==n) and s[i][j]>Max:
      Max=s[i][j]
      final_j=j
print >>out, Max

# backtrack
def outLCS(backtrack,Str1,Str2,i,j):
  if (j==0):
    return
  if backtrack[i][j]==1:    
    for k in outLCS(backtrack,Str1,Str2,i-1,j):
      yield k
    yield (Str1[i-1],"-")
  elif backtrack[i][j]==2:
    for k in outLCS(backtrack,Str1,Str2,i,j-1):
      yield k
    yield ("-",Str2[j-1])
  elif backtrack[i][j]==3:
    for k in outLCS(backtrack,Str1,Str2,i-1,j-1):
      yield k
    yield (Str1[i-1],Str2[j-1])


Align1=""
Align2=""
for i in outLCS(backtrack,S1,S2,n,final_j):
  Align1+=i[0]
  Align2+=i[1]

print >>out, Align1
print >>out, Align2
