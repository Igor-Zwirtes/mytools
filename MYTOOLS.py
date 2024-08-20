import math

PI_INT = int((math.pi-3) * 10**100)
E_INT = int((math.e-2)* 10**100)

def pi_real(n):
    if n <= 0 or n >= 100:
        return
    return f"3,{str(int(PI_INT / 10**(100-n)))}"

def e_real(n):
    if n <= 0 or n >= 100:
        return
    return f"2,{str(int(E_INT / 10**(100-n)))}"