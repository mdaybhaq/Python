def proper_division(num):
	a=num//2
	divisors=[]
	for i in range (1,a+1):
		if num%i==0:
			divisors.append(i)
	return divisors
num1=int(input("Enter a number : "))
answer=proper_division(num1)
print(answer)
