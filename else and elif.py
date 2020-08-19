#program for driving age
print("age of a person")
age = int(input())
for age in range(0,100):
    age = int(input())
     if age>18:
        print("can drive")
    elif age==18:
        print("cannot decide")
    else :
        print("cannot")
