import sys
sys.setrecursionlimit(100000)

out=open("output.txt",'w')

Input=open(sys.argv[1],'r').read().split("\n")
S1=Input[0].strip()
S2=Input[1].strip()
S3=Input[2].strip()

n=len(S1)
m=len(S2)
o=len(S3)

s=[[[0]*(o+1) for i in range(m+1)] for j in range(n+1)]
backtrack = [[[0]*(o+1) for i in range(m+1)] for j in range(n+1)]

for i in range(1,(n+1)):
  backtrack[i][0][0]=3
  for j in range(1,(m+1)):
    backtrack[i][j][0]=4

for j in range(1,m+1):
  backtrack[0][j][0]=2
  for k in range(1,o+1):
    backtrack[0][j][k]=6

for k in range(1,o+1):
  backtrack[0][0][k]=1
  for i in range(1,n+1):
    backtrack[i][0][k]=5

for i in range(1,(n+1)):
  for j in range(1,(m+1)):
    for k in range(1,(o+1)):
      s[i][j][k]=max(s[i][j-1][k],s[i-1][j][k],s[i][j][k-1],s[i][j-1][k-1],s[i-1][j][k-1],s[i-1][j-1][k],s[i-1][j-1][k-1]+int((S1[i-1]==S2[j-1])&(S2[j-1]==S3[k-1])))
      if (s[i][j][k]==s[i-1][j-1][k-1]+1) and (S1[i-1]==S2[j-1])&(S2[j-1]==S3[k-1]):
        backtrack[i][j][k]=7
      elif s[i][j][k]==s[i][j-1][k-1]:
        backtrack[i][j][k]=6
      elif s[i][j][k]==s[i-1][j][k-1]:
        backtrack[i][j][k]=5
      elif s[i][j][k]==s[i-1][j-1][k]:
        backtrack[i][j][k]=4
      elif s[i][j][k]==s[i-1][j][k]:
        backtrack[i][j][k]=3
      elif s[i][j][k]==s[i][j-1][k]:
        backtrack[i][j][k]=2
      elif s[i][j][k]==s[i][j][k-1]:
        backtrack[i][j][k]=1

print >>out, s[n][m][o]


def outLCS(backtrack,Str1,Str2,Str3,i,j,k):
  if i+j+k==0:
    return
  if backtrack[i][j][k]==1:    
    for l in outLCS(backtrack,Str1,Str2,Str3,i,j,k-1):
      yield l
    yield ("-","-",Str3[k-1])
  elif backtrack[i][j][k]==2:
    for l in outLCS(backtrack,Str1,Str2,Str3,i,j-1,k):
      yield l
    yield ("-",Str2[j-1],"-")
  elif backtrack[i][j][k]==3:
    for l in outLCS(backtrack,Str1,Str2,Str3,i-1,j,k):
      yield l
    yield (Str1[i-1],"-","-")
  elif backtrack[i][j][k]==4:
    for l in outLCS(backtrack,Str1,Str2,Str3,i-1,j-1,k):
      yield l
    yield (Str1[i-1],Str2[j-1],"-")
  elif backtrack[i][j][k]==5:
    for l in outLCS(backtrack,Str1,Str2,Str3,i-1,j,k-1):
      yield l
    yield (Str1[i-1],"-",Str3[k-1])
  elif backtrack[i][j][k]==6:
    for l in outLCS(backtrack,Str1,Str2,Str3,i,j-1,k-1):
      yield l
    yield ("-",Str2[j-1],Str3[k-1])
  elif backtrack[i][j][k]==7:
    for l in outLCS(backtrack,Str1,Str2,Str3,i-1,j-1,k-1):
      yield l
    yield (Str1[i-1],Str2[j-1],Str3[k-1])
    
    
Align1=""
Align2=""
Align3=""
for i in outLCS(backtrack,S1,S2,S3,n,m,o):
  Align1+=i[0]
  Align2+=i[1]
  Align3+=i[2]

print >>out, Align1
print >>out, Align2
print >>out, Align3

    
    
