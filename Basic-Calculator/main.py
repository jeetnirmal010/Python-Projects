def input_data1():
    n1 = int(input("Enter first number: "))
    return n1
def input_data2():
    n2 = int(input("Enter first number: "))
    return n2

print("====== CALCULATOR ======")
print()
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
print()
print()
choose = input("Choose a option: ")
if choose =='1':
    a = input_data1()
    b = input_data2()
    print("Answer = ",a + b)
elif choose=='2':
    a = input_data1()
    b = input_data2()
    print("Answer = ",a - b)
elif choose=='3':
    a = input_data1()
    b = input_data2()
    print("Answer = ",a * b)
elif choose=='4':
    a = input_data1()
    b = input_data2()
    if b ==0:
        print("Denominator can't be zero")
    else:
        print("Answer = ",a / b)
elif choose=='5':
    print("Good Bye!")
else:
    print("Invalid Input")