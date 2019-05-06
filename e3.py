def prime(i):
	c = 0
	for k in range(1,i+1):
		if i % k == 0:
			c = c + 1
	if c == 2:
		return 1
	
n = 13195
max = 1
for i in range(1,n+1):
	if n % i == 0:
		if prime(i) == 1:
			if max < i:
				max = i
print(max)

