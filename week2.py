total = 0

while True:

    expense = input("Enter expense amount or type quit: ")

    if expense.lower() == "quit":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative")
            continue

        total += expense

        print("Current Total:", total)

    except ValueError:
        print("Please enter a valid number")

print("\nFinal Total Spent:", total)