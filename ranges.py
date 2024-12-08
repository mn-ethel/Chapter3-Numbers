from math import (sin,cos,pi)
for i in range(0,346,15):
    R=(i*pi)/180
    S=sin(R)
    C=cos(R)
    print(i,"---",round(S,4),round(C,4))
