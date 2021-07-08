try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

# it's better to use code below:

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

