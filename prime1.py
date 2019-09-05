def prime1(num):
	num1 = []
	i = 0
	while i < len(num):
		j = 2
		while j < num[i]:
			if num[i] % j == 0:
				var = num[i],"is not a prime number"
				num1.append(var)
				break
			j = j + 1	
		else:
			var = num[i],"is a prime number"
			num1.append(var)
		i = i + 1
	return num1
print prime1([12,3,15,31,6,9,5])