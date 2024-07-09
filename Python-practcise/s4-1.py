
def fact(num):
    ans = 1
    if num < 0:
        print("Error Factorial is not defined for negative numbers.")
    elif num == 0:
        print("Factorial is 1")
    else:
        for i in range(1, num + 1):
            ans *= i
        print("Factorial is : ",ans)


num = int(input("Enter a number : "))
fact(num)
