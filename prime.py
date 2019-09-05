def prime(num):
	i = 2
	while i < num:
		if num % i == 0:
			return num ,"is  not a prime number"
			break
		i = i + 1
	else:
		return num , "is a prime number"
print prime(input("enter a num :- "))