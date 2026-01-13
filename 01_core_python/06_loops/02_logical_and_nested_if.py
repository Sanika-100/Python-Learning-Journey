# LOGICAL OPERATORS & NESTED IF

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Not Allowed")

# Nested if
balance = 5000

if balance > 0:
    if balance >= 3000:
        print("Sufficient Balance")
    else:
        print("Low Balance")
else:
    print("No Balance")

# Output:
# Entry Allowed
# Sufficient Balance
