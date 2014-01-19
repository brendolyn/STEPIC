import sys

Input=open(sys.argv[1],'r').read().split("\n")
text=Input[0].strip()
Array=[int(x) for x in Input[1].strip().split(", ")]
LCP=[int(x) for x in Input[2].strip().split(", ")]

out=open("output.txt",'w')

def PrintTraceBack(text,pool,start,end):
  i=len(pool)-1
  while pool[i]>start:
    if pool[i]<end:
      print text[pool[i]:end]
    end=pool[i]
    i-=1
  if start<end:
    print text[start:end]
  return(pool[:(i+1)])

pool=[0]
for i in range(len(Array)):
  s=text[Array[i]:]
  if i==len(Array)-1:
    print s[LCP[i]:]
    pool=PrintTraceBack(s,pool,0,LCP[i])
  else:
    print s[max(LCP[i],LCP[i+1]):]
    if LCP[i]>LCP[i+1]:
      pool=PrintTraceBack(s,pool,LCP[i+1],LCP[i])
    else:
      pool.append(LCP[i])


  

