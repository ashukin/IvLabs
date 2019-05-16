largest = -1
smallest = None
while True:
    num = input("Enter a number:")
    try:
        num = int(num)
        if num >largest:
            largest = num
        if smallest is None:
            smallest = num
        elif num<smallest:
            smallest = num
    except:
        if num == "done":
            break
        else:
            print("Invalid input") 
print("Maximum is", largest)
print("Minimum is", smallest)