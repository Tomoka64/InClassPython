def f(c1, c2, c3, c4, x):
    return c1*x**3+c2*x**2+c3*x+c4

def bisection(a,b,epsilon):
    interval = abs(a-b)
    ya = f(c1, c2, c3, c4, a)
    yb = f(c1, c2, c3, c4, b)
    zero = False
    c = (a+b)/2
    yc = f(c1, c2, c3, c4, c)
    print(c,yc)
    if (ya*yb)>0: # and (f2(c1,c2,c3,c4,a)*f2(c1,c2,c3,c4,b)<0):print
        print ("There are no zeros")
    else:
        while(interval > epsilon and yc != 0):
            print("interval", interval)
            c = (a+b)/2
            yc = f(c1, c2, c3, c4, c)
            if ya*yc < 0:
                b = c
                ya=yc
            else:
                a=c
                ya=yc
            interval /= 2
            zero = c
            print("c", c, "yc", yc)
        return zero

c1 = 1
c2 = 2
c3 = -3
c4 = -2
a = 0
b = 2
epsilon = 0.001

print("Zero:", bisection(a,b,epsilon))
