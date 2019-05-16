hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter the rate per hour:")
r = float(rate)
if h>40.0 :
   gpay = 40*r + (h-40)*1.5*r
else :
   gpay = h*r
print(gpay)