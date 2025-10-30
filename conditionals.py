# Conditional Statements 
# This program checks a number and a grade system

print("=== Conditional Statement Demo ===")

# Ask the user for a number
num = float(input("Enter any number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Ask the user for a grade
marks = int(input("Enter your marks (0-100): "))

# Conditions
if marks >= 90:
    print("Grade: A+ (Excellent!)")
elif marks >= 80:
    print("Grade: A (Very Good)")
elif marks >= 70:
    print("Grade: B (Good)")
elif marks >= 60:
    print("Grade: C (Average)")
elif marks >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")

# Check if the number is even or odd
if num % 2 == 0:
    print(f"The number {num} is Even.")
else:
    print(f"The number {num} is Odd.")

print("\nThank you for using the program!")
