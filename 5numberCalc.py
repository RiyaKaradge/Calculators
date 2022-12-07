import module_1

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice: 1 or 2 or 3 or 4:\n")

if choice not in ['1', '2', '3', '4']:
    print("INVALID INPUT :(")

print('_____________________________________________________________________________________')
print("Remember: Only up till 5 numbers!")
print(" ")
print("Tip: If you don't want 5 numbers in multiplication, then type 1 in the spots that you don't need.")
print(" ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    num4 = float(input("Enter fourth number: "))
    num5 = float(input("Enter fifth number: "))

    if choice == '1':
        print(module_1.add(num1, num2, num3, num4, num5))

    elif choice == '2':
        print(module_1.subtract(num1, num2, num3, num4, num5))

    elif choice == '3':
        print(module_1.multiply(num1, num2, num3, num4, num5))

    elif choice == '4':
        print(module_1.divide(num1, num2, num3, num4, num5))

print("Thank You for choosing Riya's Calculator")
