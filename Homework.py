# Program to calculate n powers of a given number

print("Welcome to Vrisha's Power Calculator!")

# Take inputs from the user
number = float(input("Enter the number: "))
n = int(input("Enter how many powers you want to calculate: "))

print(f"\nThe first {n} powers of {number} are:")

# Loop to calculate powers from 1 to n
for i in range(1, n + 1):
    result = number ** i
    print(f"{number}^{i} = {result}")