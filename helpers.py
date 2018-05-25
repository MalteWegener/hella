import numpy as np
from numpy.linalg import solve, norm

def reflectray(a,b,p,q):
	a = np.array(a)
	b = np.array(b)
	p = np.array(p)
	q = np.array(q)

	abn = (b-a)/norm(b-a)
	try:
		lam, mu = solve([[b[0]-a[0],p[0]-q[0]],[b[1]-a[1],p[1]-q[1]]],p-a)
	except:
		return None

	S = a+lam*(b-a)
	n = np.array([(a-b)[1],(a-b)[0]*-1]) if np.dot(np.array([(a-b)[1],(a-b)[0]*-1]),(q-p)) < 0 else -1*np.array([(a-b)[1],(a-b)[0]*-1])
	n = n /norm(n)

	acc = 0.1

	if lam > 1+acc or lam < 0-acc or mu > 1+acc or mu < 0-acc:
		return None

	R = S-n*np.dot(q-S,n)+abn*np.dot(q-S,abn)
	return R

def reflectvel(a,b,v):
	a = np.array(a)
	v = np.array(v)
	v = np.array(v)

	abn = (b-a)/norm(b-a)

	n = np.array([(a-b)[1],(a-b)[0]*-1]) if np.dot(np.array([(a-b)[1],(a-b)[0]*-1]),v) < 0 else -1*np.array([(a-b)[1],(a-b)[0]*-1])
	n = n /norm(n)

	return abn *np.dot(v,abn)-n*np.dot(v,n)