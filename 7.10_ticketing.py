tickets = ("High", "Medium", "Low", "High")

open_tickets = 3

print("Reviewing tickets...")

for ticket in tickets:
    if ticket == "High":
        print("This is a high priority ticket.")
    elif ticket == "Medium":
        print("This is a medium priority ticket.")
    elif ticket == "Low":
        print("This is a low priority ticket.")
    else:
        print("Unknown ticket priority.")

print("\nProcessing Open tickets...")

while open_tickets > 0:
    print("Resolving ticket...")
    open_tickets = open_tickets - 1

print("\nAll tickets have been resolved.")

