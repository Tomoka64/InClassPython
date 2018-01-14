def f(c1, c2, c3, c4, x):
    return c1*x**3+c2*x**2+c3*x+c4

def f1(c1, c2, c3, c4, x):
    return 3*c1*x**2+2*c2*x+c3

def f2(c1, c2, c3, c4, x):
    return 6*c1*x+2*c2

def newton(a,b,epsilon):
    if (f(c1,c2,c3,c4,a)*f(c1,c2,c3,c4,b)>0):
        print ("there are no zeros")
        return False
    interval = abs(a-b)
    zero = False
    if (f2(c1,c2,c3,c4,a)*f(c1,c2,c3,c4,b)<0):
        x0=a
    else:
        x0=b
    while(interval> epsilon):
        print("interval", interval)
        x1 = x0 - (f(c1,c2,c3,c4,x0) / f1(c1,c2,c3,c4,x0))
        interval = abs(x1- x0)
        x0 = x1
        zero = x0
        print("x0", x0)
    return zero

c1=1
c2=2
c3=-3
c4=-2
a=0
b=2
epsilon=0.001
print("Zero:", newton(a,b,epsilon))
