#!/usr/bin/env python
import sys
import numpy as np
import scipy as sp
from scipy import linalg, mat, dot

mat=[]
cos=[]

for line in sys.stdin:
	
	
	res=[int(i) for i in line.split(',')]
	mat.append(np.mat(res))

for i in range(0,len(mat)-1):
	a=mat[i]
	b=mat[i+1]
	c = dot(a,b.T)/linalg.norm(a)/linalg.norm(b)
	cos.append(c)
	A = c.tolist()
	print i%10,A[0][0]
	
