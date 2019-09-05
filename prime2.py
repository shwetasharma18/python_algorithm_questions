def prime2(num):
	lis = []
	num1 = str(num)
	i = 0
	while i < len(num1):
		num2 = int(num1[i])
		j = 2
		while j < num2:
			if num2 % j == 0:
				var = num2,"is not a prime number"
				lis.append(var)
				break
			j = j + 1
		else:
			var = num2,"is a prime number"
			lis.append(var)
		i = i + 1
	return(lis)
print prime2(input("enter a two digit num :- "))