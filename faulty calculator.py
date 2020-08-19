print("enter the number")
num1 = int(input())
num2 = int(input())
print("what do u want *,+,-,/?")
oper = input()
if num1==43 and num2==3 and oper=='*':
    print("555")
elif num1 == 56 and num2==9 and oper=='+':
    print("77")
elif num1== 56 and num2==6 and oper=='/':
    print("4")
elif oper=='+':
    plus=num1+num2
    print(plus)
elif oper=='-':
    sub=num2-num1
    print(sub)
elif oper=='*':
    mult=num1*num2
    print(mult)
elif oper=='/':
    dev=num1/num2
    print(dev)
else:
    print("u were played")

