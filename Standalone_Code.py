# c = root(a2 + b2)

import math

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = (a ** 2) + (b ** 2)
circ_rt_tgl = math.sqrt(c)
print(f"c of Right AAngled triangle is: {round(circ_rt_tgl, 2)}")
