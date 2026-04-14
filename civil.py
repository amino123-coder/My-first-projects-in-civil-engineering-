from math import cos,sin,sqrt,log,exp,pi
k=int(input("enter 1 or 2 or 3 for k value:"))
if k<1 or k>3:
    print("k must be 1 or 2 or 3...")
    exit()
x=float(input("enter x value :\n"))
if k==1:
    y=cos(x)+sin(x)
elif k==2:
    if x<0:
        print("x must be positive")
        exit()
    else: 
     y=sqrt(x)+exp(x) 
else:
   if x<0:
      print("x must be greater than 0...")
      exit() 
   else:
      y=log(x)+pi
print("y value is :",y)


            
