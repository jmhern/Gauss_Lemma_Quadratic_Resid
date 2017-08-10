
from math import floor
from sys import argv, stderr

def fprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

def get_s(a,p):
	stop = floor((p-1)/2)
	s = 0
	coeffs = range(1, stop+1)
	for i in coeffs:
		#note that through gauss lemma 
		#there will be no repititions
		if (i*a) % p  > p/2:
			s+=1
	return s

def legendre_sym(a,p):
	if get_s(a,p) % 2 == 0:
		return 1
	return -1

if __name__=='__main__':
	a = int(argv[1])
	p = int(argv[2])
	if (p % 2 == 0) or (a % p == 0):
		fprint('a and p must be relatively prime and p must be an odd prime')
		exit(1)
	print('The value of the legendre symbol for a={} p={} is {}'.format(a,p,legendre_sym(a,p)))