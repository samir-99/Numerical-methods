def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)




n,m=input().split()
n=int(n)
m=int(m)
al=n+m
fib=_fib(al)
fb=fib[0]

if (abs(m-n)>1):
        print(0)
else:
        print(fib+al-1)
        
          


