import sys

Out=open("output.txt",'w')
Input=open(sys.argv[1])
Input=Input.read().split("\n")
P=Input[0]
String=Input[1]
mis=int(Input[2])

def a_match(s1,s2,mis):
  m=0
  match=True
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      m+=1
    if m>mis:
      match=False
      break
  return match

match_loc=[]
for i in range(len(String)-len(P)+1):
  if a_match(P,String[i:(i+len(P))],mis):
    match_loc.append(i)

print >>Out," ".join(str(x) for x in match_loc)


