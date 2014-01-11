# 77_3

import sys


out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
S1=Input[0].strip()
S2=Input[1].strip()

p = -1 # penalty for indel
n=len(S1)
m=len(S2)

s=[[0]*(m+1) for i in range(n+1)]
backtrack = [[0]*(m+1) for i in range(n+1)]

for i in range(1,(n+1)):
  s[i][0]=s[i-1][0]+p

for j in range(1,(m+1)):
  s[0][j]=s[0][j-1]+p

for i in range(1,(n+1)):
  for j in range(1,(m+1)):
    s[i][j]=max(s[i][j-1]+p,s[i-1][j]+p,s[i-1][j-1]+int(S1[i-1]==S2[j-1])-1)


print -s[n][m]
