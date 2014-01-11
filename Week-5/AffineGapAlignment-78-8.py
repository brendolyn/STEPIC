# 77_5

import sys,copy

# input BLOSUM62 matrix
Matrix = open("BLOSUM62.txt").read().split("\n")
score = {}
aa = filter(lambda x: x!="",Matrix[0].split(" "))
for i in range(len(aa)):
  line = filter(lambda x: x!="",Matrix[i+1].split(" "))
  assert line[0]==aa[i]
  for j in range(len(aa)):
    score[(aa[i],aa[j])]=int(line[j+1])

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
S1=Input[0].strip()
S2=Input[1].strip()

o_p = -11 # penalty for opening indel
e_p = -1  # penalty for extending indel
n=len(S1)
m=len(S2)

s=[[0]*(m+1) for i in range(n+1)]
backtrack = [[0]*(m+1) for i in range(n+1)]


for i in range(1,(n+1)):
  if i == 1:
    s[i][0]=s[i-1][0]+o_p
  else:
    s[i][0]=s[i-1][0]+e_p
  backtrack[i][0]=1

for j in range(1,(m+1)):
  if j == 1:
    s[0][j]=s[0][j-1]+o_p
  else:
    s[0][j]=s[0][j-1]+e_p
  backtrack[0][j]=2

s_low = copy.deepcopy(s)
s_up = copy.deepcopy(s)

for i in range(1,(n+1)):
  for j in range(1,(m+1)):
    s_low[i][j]=max(s_low[i-1][j]+e_p,s[i-1][j]+o_p)
    s_up[i][j]=max(s_up[i][j-1]+e_p,s[i][j-1]+o_p)
    s[i][j]=max(s_low[i][j],s_up[i][j],s[i-1][j-1]+score[(S1[i-1],S2[j-1])])
    if (s[i][j]==s[i-1][j-1]+score[(S1[i-1],S2[j-1])]):
      backtrack[i][j]=3
    elif s[i][j]==s_up[i][j]:
      backtrack[i][j]=2
    else:
      backtrack[i][j]=1

print >>out, s[n][m]

# backtrack
def outLCS(backtrack,Str1,Str2,i,j):
  if (j==0) and (i==0):
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
for i in outLCS(backtrack,S1,S2,n,m):
  Align1+=i[0]
  Align2+=i[1]

print >>out, Align1
print >>out, Align2
