from math import * #including lib (module?) for more mathemitical operations

a,b = 0,1
while a<10:
    print(a)
    a,b=b,a+b

print(3*(4+5))
print(10%3)
my_num = 5
print(str(my_num) + " it's fun") #it's impossible to print (int + "string")
my_num = -5
print(abs(my_num))
print(pow(3,2))
print(max(4,6)) #min
print(round(3.7))
print(floor(3.7)) #ceil
print(sqrt(9))

#-----------------------------
num1 = input("Enter a number: ")
num2 = input("Enter another number: ") #by default it's string
result = float(num1) + float(num2)
print(result)
#-----------------------------

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,3))