input1 = int(input("Enter first number:"))
input2 = int(input("Enter second number:"))
input3 = input("what do you want to do add , subtract , divide and multiply:")

if input3.lower()=="add":
    if input1==53 and input2==63 :
        print("106")
    else:
        print(input1+input2)    
    
elif input3.lower()=="subtract":
    if input1==5678 and input2==1111:
        print("4211")
    else:
        print(input1-input2)
elif input3.lower()=="divide":
    if input1==100 and input2==20:
        print("4")
    else:
        print(input1/input2)
elif input3.lower()=="multiply":
    if input1==53 and input2==63:
        print("2222")
    else:
    
        print(input1*input2)
else:
    print("this calculator could only add, subtract, divide, multiply")
