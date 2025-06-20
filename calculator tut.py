# This is a tutorial for a basic calculator in python 
# This does not include a GUI
# I will be doing this in Sublime and python terminal
# Instructions in the description on how to run python code with proper input support 
# This calculator will have 5 functions
# Addition
# Subtraction
# Multiplication
# Division
# Exponents

def main():
	print("* * * Calculator * * *")
	print("Choose an option.")
	print("1: Addition")
	print("2: Subtraction")
	print("3: Multiplication")
	print("4: Division")
	print("5: Exponential input")
	print("6: End program")
	choice = int(input("Enter: "))
	while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
		print("Invalid input. Please enter 1, 2, 3, 4, 5, or 6.")
		choice = int(input("Enter: "))

	if choice == 1:
		calc1()
		restartorend()
	elif choice == 2:
		calc2()
		restartorend()
	elif choice == 3:
		calc3()
		restartorend()
	elif choice == 4:
		calc4()
		restartorend()
	elif choice == 5:
		calc5()
		restartorend()
	else:
		print("\nEnd of program.\nThank you for using this calculator.")
		exit()

def calc1():
	num1 = float(input("Enter the first number you want to add: "))
	num2 = float(input("Enter the second number you want to add: "))
	sum1 = num1 + num2
	print("The sum of {0} and {1} is: {2}.".format(num1, num2, sum1))

def calc2():
	num1 = float(input("Enter the number you will be subtracting from: "))
	num2 = float(input("Enter the numbe you will be subtracting by: "))
	sum1 = num1 - num2
	print("After the subtraction of {1} from {0} is: {2}.".format(num1, num2, sum1))

def calc3():
	num1 = float(input("Enter the first number you want to mutiply: "))
	num2 = float(input("Enter the second number you want to mutiply: "))
	product1 = num1 * num2
	print("The product of {0} times {1} is: {2}.".format(num1, num2, product1))

def calc4():
	num1 = float(input("Enter the number you want to divide: "))
	num2 = float(input("Enter the number you want to divide by: "))
	product1 = num1 / num2
	print("The product of {0} divided by {1} is: {2}.".format(num1, num2, product1))

def calc5():
	num1 = float(input("Enter the number you want to take to the power of: "))
	num2 = float(input("Enter the number you want to use as the exponent, or the power of: "))
	result = pow(num1, num2)
	print("The number {0} taken to the power of {1} is: {2}.".format(num1, num2, result))

def calc6():
	print("\nEnd of program.\nThank you for using this calculator.")
	exit()

def restartorend():
	print("Would you like to try again?")
	decide = int(input("1: Exit the program.\n2: Restart the program.\nEnter decision: "))
	while decide != 1 and decide != 2:
		print("Invalid decision. Please select 1 or 2.")
		decide = int(input("1: Exit the program.\n2: Restart the program.\nEnter decision: "))
	if decide == 1:
		print("\nEnd of program.\nThank you for using this calculator.")
		exit()
	else:
		main()


main()