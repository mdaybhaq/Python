bill=int(input("Enter the bill : "))
tip_per=int(input("Enter tip Percent , 10 , 15 , 20 : "))
if (tip_per==10):
    billFinal=1.1*bill
    splitNo=int(input("How many people to split : "))
    perPerson=billFinal/splitNo
    print("Each person will have to pay", round(perPerson,2))
elif (tip_per==15):
    billFinal=1.15*bill
    splitNo=int(input("How many people to split : "))
    perPerson=billFinal/splitNo
    print("Each person will have to pay", round(perPerson,2))

elif (tip_per==20):
    billFinal=1.2*bill
    splitNo=int(input("How many people to split : "))
    perPerson=billFinal/splitNo
    print("Each person will have to pay", round(perPerson,2))

else:
    print("Wrong Value Entered")

 