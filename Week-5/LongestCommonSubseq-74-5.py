# 74-5
import sys
sys.setrecursionlimit(100000)

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
S1=Input[0].strip()
S2=Input[1].strip()

n=len(S1)
m=len(S2)

s=[[0]*(m+1) for i in range(n+1)]
backtrack = [[0]*(m+1) for i in range(n+1)]

for i in range(1,(n+1)):
  for j in range(1,(m+1)):
    s[i][j]=max(s[i][j-1],s[i-1][j],s[i-1][j-1]+int(S1[i-1]==S2[j-1]))
    if (s[i][j]==s[i-1][j-1]+1) and S1[i-1]==S2[j-1]:
      backtrack[i][j]=3
    elif s[i][j]==s[i][j-1]:
      backtrack[i][j]=2
    else:
      backtrack[i][j]=1



def outLCS(backtrack,Str1,i,j):
  if i*j==0:
    return
  if backtrack[i][j]==1:    
    for k in outLCS(backtrack,Str1,i-1,j):
      yield k
  elif backtrack[i][j]==2:
    for k in outLCS(backtrack,Str1,i,j-1):
      yield k
  elif backtrack[i][j]==3:
    for k in outLCS(backtrack,Str1,i-1,j-1):
      yield k
    yield Str1[i-1]

print >> out, "".join(outLCS(backtrack,S1,n,m))

    
    
