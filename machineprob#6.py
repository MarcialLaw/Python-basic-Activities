import math

C=50
H=30
value =[]
items=[D for D in input() .split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*C*H*float(d))))))
print (','.join(value))
