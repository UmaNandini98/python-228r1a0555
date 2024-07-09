def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False

print("A=True|B=True|A AND B=True", AND(1, 1))
print("A=True|B=False|A AND B=False", AND(1, 0))
print("A=False|B=True|A AND B=False", AND(0, 1))
print("A=False|B=False|A AND B=False", AND(0, 0))