import sys

lis=[]
count=1
for line in sys.stdin:
	phase,cos_sim=line.strip().split()
	try:float(cos_sim)
	except:ValueError
	lis.append([int(phase),float(cos_sim)])
flag=0
thold=0.9996
for i in range(0,10):
	sum=0
	for j in range(0,len(lis)):
		if(lis[j][0]==i and lis[j][1]>=thold):
			sum=sum+1
	print i,sum
	

	
