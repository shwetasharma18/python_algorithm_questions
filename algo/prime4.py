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
	count = 0
	while k < len(num2):
		count = count + num2[k]
		k = k + 1
	print num2
	return count
print prime1([12,33,15,31,6,92,51])