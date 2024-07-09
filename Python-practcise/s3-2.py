def nand_gate(a, b):
    return not (a and b)

def nor_gate(a, b):
    return not (a or b)

# Example usage
print("NAND GATE :")
print(" If A=true or B=true output : ",nand_gate(1,1))
print(" If A=true or B=false output : ",nand_gate(1,0))
print(" If A=false or B=true output : ",nand_gate(0,1))
print(" If A=false or B=false output : ",nand_gate(0,0))

print("NOR GATE :")
print(" If A=true and B=true output : ",nor_gate(1,1))
print(" If A=true and B=false output : ",nor_gate(1,0))
print(" If A=false and B=true output : ",nor_gate(0,1))
print(" If A=false and B=false output : ",nor_gate(0,0))