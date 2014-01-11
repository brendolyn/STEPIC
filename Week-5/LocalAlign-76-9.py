# 76_9

import sys

# input PAM250 matrix
Matrix = open("PAM250_1.txt").read().split("\n")
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

p = -5 # penalty for indel
n=len(S1)
m=len(S2)

s=[[0]*(m+1) for i in range(n+1)]
backtrack = [[0]*(m+1) for i in range(n+1)]


Max=0
for i in range(1,(n+1)):
  for j in range(1,(m+1)):
    s[i][j]=max(s[i][j-1]+p,s[i-1][j]+p,s[i-1][j-1]+score[(S1[i-1],S2[j-1])],0)
    if s[i][j]!=0:      
      if (s[i][j]==s[i-1][j-1]+score[(S1[i-1],S2[j-1])]):
        backtrack[i][j]=3
      elif s[i][j]==s[i][j-1]+p:
        backtrack[i][j]=2
      else:
        backtrack[i][j]=1
      if s[i][j]>Max:
        Max=s[i][j]
        final_i=i
        final_j=j

print >>out, Max
print "End:",final_i,final_j
# backtrack
def outLCS(backtrack,Str1,Str2,i,j):
  if backtrack[i][j]==0:
    print "Start:",i,j
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
for i in outLCS(backtrack,S1,S2,final_i,final_j):
  Align1+=i[0]
  Align2+=i[1]

print >>out, Align1
print >>out, Align2
 

# test output alignment in 50 aa per line
'''
temp1=""
temp2=""
for i in range(len(Align1)):
  if i%50==0:
    print temp1
    print temp2
    print
    temp1=""
    temp2=""
  temp1+=Align1[i]
  temp2+=Align2[i]

print temp1
print temp2
'''
