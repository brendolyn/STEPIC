import sys

Out=open("output.txt",'w')
Input=open(sys.argv[1])
String=Input.read().strip()

score=0
scores=[0]
for i in range(len(String)):
  sub=String[i]
  if sub=="C":
      score-=1
  elif sub=="G":
      score+=1
  scores.append(score)

min_loc=[]
for i in range(len(scores)):
  if scores[i]==min(scores):
    min_loc.append(i)

#print >>Out," ".join(str(x) for x in scores)
print >>Out," ".join(str(x) for x in min_loc)
  
