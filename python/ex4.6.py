def computepay(h,r):
    if(h>40.0) :
        gpay = 40*r + (h-40)*1.5*r
    else :
        gpay = h*r
    return gpay

hrs = input("Enter hours:")
rate = input("Enter rate per hour:")
print(computepay(float(hrs),float(rate)))