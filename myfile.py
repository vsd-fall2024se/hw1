prices = [1,2,3,4,6,8,4,6,8]
L = 0
R = 1
max_p = 0
for i in range(len(prices)):
	if prices[L]- prices[R]>0:
		prof = prices[L]- prices[R]
		max_p = max(prof,max_p)
	else:
		L = R
		R = L+1
	return max_p 