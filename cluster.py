#!/usr/bin/env python
import sys
import numpy as np
import scipy as sp
from scipy import linalg, mat, dot
from sklearn.cluster import KMeans

mat=[]
cos=[]

for line in sys.stdin:
	
	
	res=[int(i) for i in line.split(',')]
	mat.append(res)

X=np.array(mat)
kmeans=KMeans(n_clusters=2,random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)


