# 87-2
import sys,copy

out=open("output.txt",'w')

Input=open(sys.argv[1],'r')
List=Input.read().strip()[1:(-1)].split(" ")

def complement(e):
  if e[0]=="-":
    f="+"+e[1:]
  else:
    f="-"+e[1:]
  return f
  
def reversal(n,m):
  global List
  temp=[]
  for i in range(m-n+1):
    temp.append(complement(List[m-i]))
  List[(n):(m+1)]=temp



for i in range(len(List)):
  k=i
  while abs(int(List[k]))!=i+1:
    k=k+1
  if k==i and List[i][0]=="+":
    continue
  reversal(i,k)
  print >>out, "("+" ".join(List)+")"
  if List[i][0]=="-":
    reversal(i,i)
    print >>out, "("+" ".join(List)+")"
