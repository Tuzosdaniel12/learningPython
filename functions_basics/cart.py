#packing
def cal_total(*args):
    total = sum(args)
    print(args)
    
cal_total(25,25,20,100)

#unpacking
def unpacking():    
    return 1,2,3

var1, var2, var3 = unpacking()

print(var1)
print(var2)
print(var3)

first, last = input('Enter your full name: \n').split(" ")

print(first + " " + last)