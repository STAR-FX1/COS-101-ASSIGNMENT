p = float(input("enter the initial principal amount"))
r = float(input("enter the annual interest rate(in decimal form"))
t = float(input("enter the time period(in years"))
n = float(input("enter the number of times interest is applied per time period"))

# Calculate Simple Interest


SI = p * (1 + r * t)

# Calculate Compound Interest
CI = p * (1 + r/n)**(n*t)
print(f"simple interest:{SI}")
print(f"compound interest:{CI}")