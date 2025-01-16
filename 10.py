# Calculate Compound Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))
compound_interest = principal * ((1 + rate / 100) ** time) - principal
print(f"Compound Interest: {compound_interest:.2f}")