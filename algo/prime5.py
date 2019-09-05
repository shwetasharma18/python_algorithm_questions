def prime1(num):
	num1 = []
	num2 = []
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
			num2.append(num[i])
		i = i + 1
	k = 0
	lis = []
	count = 0
	while k < len(num2):
		count = count + num2[k]
		k = k + 1
		l = 2
		while l < count:
			if count % l == 0:
				abc = count, "is not a prime number"
				break
			l = l + 1
		else:
			abc = count,"is a prime number"
	return abc
print prime1([11,28,37,41,61,15,51])