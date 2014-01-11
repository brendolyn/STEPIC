# 72_9

import sys

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
n=int(Input[0])
m=int(Input[1])
down = [ [int(j) for j in i.split(" ")] for i in Input[2:(2+n)]]
right = [ [int(j) for j in i.split(" ")] for i in Input[(3+n):(4+2*n)]]

S=[[0]*(m+1) for i in range(n+1)]

for i in range(1,n+1):
  S[i][0]=S[i-1][0]+down[i-1][0]

for j in range(1,m+1):
  S[0][j]=S[0][j-1]+right[0][j-1]

for i in range(1,n+1):
  for j in range(1,m+1):
    S[i][j] = max(S[i][j-1]+right[i][j-1],S[i-1][j]+down[i-1][j])

print S[n][m]
