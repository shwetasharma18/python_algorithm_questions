def prime3(num):
    lis = []
    num1 = str(num)
    num3 = []
    i = 0
    product = 1
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
            num3.append(num2)
        i = i + 1
    k = 0
    while k < len(num3):
        product = product * num3[k] 
        k= k + 1    
    if product > num:
        print "the product of numbers is greater"
    else:
        print "the number is greater"
    
    print product
    return(lis)
print prime3(input("enter a num :- "))