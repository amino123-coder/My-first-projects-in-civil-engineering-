L=float(input('enter the length:\n'))
if L<=0:
    print("please enter a valid value:\n")
    exit()
p=float(input("enter the load:"))
x=float(input("enter the distance:\n"))
if x<0 or x>L:
    print("please enter another value:\n")
    exit() 
xc=float(input("enter the distance:\n"))
if xc<0 or xc>L:
    print("please enter another value:\n")
    exit()
if x<xc:
    M=(p*(1-xc)*(x/1))
else:
    M=p*(1-xc)*xc/1
print(M)    

