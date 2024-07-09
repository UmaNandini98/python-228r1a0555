n = int(input("Enter number of elements : "))
print("Enter elements : ")
ans = []
for i in range(n):
    p = int(input())
    tup = (p, p * p * p)
    ans.append(tup)

print(ans)


'''QUESTION :
The Inventor's Workshop

In a small workshop tucked away in a bustling city, 
Inventor Jones tinkered with gears and levers, fascinated by 
the power of cubes. He meticulously crafted a device that 
would calculate the cubes of any number fed into it. With each turn of the handle,
 the machine hummed and whirred, producing tuples that sparkled with the promise of mathematical discovery.

Your task is to find the tuples where each tuple consists of a number and its corresponding cube. 
Sample Input:               sample output
5                           [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]

1
2
3
4
5


'''