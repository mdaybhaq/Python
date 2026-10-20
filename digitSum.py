a=int(input("Enter a 3 digit number : "))
h=a//100
print(h)
temp1=a-100*h
t=temp1//10
print(t)
o=temp1%10
print(o)
sum=h+t+o
print("Sum is : ", sum)