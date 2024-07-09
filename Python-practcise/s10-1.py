import numpy as np
def half_adder(a,b):
    Sum=np.bitwise_xor(a,b)
    Carry=np.bitwise_and(a,b)
    return Sum,Carry


print(half_adder(0,0))
print(half_adder(0,1))
print(half_adder(1,0))
print(half_adder(1,1))