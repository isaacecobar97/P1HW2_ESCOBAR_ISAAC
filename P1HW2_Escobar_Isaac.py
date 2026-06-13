# Isaac Escobar
# 13 June 2026
# P1HW2_EscobarIsaac.py
# Upcoming trip expenses

# Pseudocode:
# Display program title
# Input budget
# Input travel destination
# Input gas expense
# Input accommodation expense
# Input food expense
# Calculate total expenses
# Calculate remaining balance
# Display destination
# Display budget
# Display expenses
# Display remaining balance

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

expenses = gas + accommodation + food
remaining_balance = budget - expenses

print("\n------------Travel Expenses------------")
print("Location:", destination)
print()
print("Initial Budget:", int(budget))
print("Fuel:", int(gas))
print("Accomodation:", int(accommodation))
print("Food:", int(food))
print()
print("Remaining Balance:", int(remaining_balance))