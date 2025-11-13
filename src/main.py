from transaction import Transaction
from database import initialise_database, add_transaction_to_db, update_transaction_to_db, delete_transaction_in_db, clear_transactions, get_all_transactions


def add_transaction():
    amount = float(input("Enter amount: "))
    currency = input("Enter currency (e.g., USD, EUR): ")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (e.g., Food, Rent): ")

    transaction = Transaction(amount, currency, date, category)
    add_transaction_to_db(transaction)
    print(f"Added: {transaction}\n")


def edit_transaction():
    display_transactions()
    transaction_id = int(input("Enter transaction ID to edit: "))

    for t in get_all_transactions():
        if t[0] == transaction_id:
            transaction = Transaction(t[1], t[2], t[3], t[4], t[0])
            break

    else:
        print("Transaction not found.\n")
        return

    amount_input = input("Enter new amount (or leave blank to keep current): ")
    amount = float(amount_input) if amount_input.strip() else None
    currency = input("Enter new currency (or leave blank to keep current): ").strip() or None
    date = input("Enter new date (DD-MM-YYYY) (or leave blank to keep current): ").strip() or None
    category = input("Enter new category (or leave blank to keep current): ").strip() or None

    if amount is not None:
        transaction.amount = amount
    if currency is not None:
        transaction.currency = currency
    if date is not None:
        transaction.date = date
    if category is not None:
        transaction.category = category

    print(f"\nTransaction before update: {transaction}")

    update_transaction_to_db(transaction)
    print(f"Updated transaction: {transaction}\n")


def delete_transaction():
    display_transactions()
    transaction_id = int(input("Enter transaction ID to edit: "))

    for t in get_all_transactions():
        if t[0] == transaction_id:
            transaction = Transaction(t[1], t[2], float(t[3]), t[4], t[0])
            break

    else:
        print("Transaction not found.\n")
        return

    print(f"Deleting transaction: {transaction}\n")
    delete_transaction_in_db(transaction)

    print(f"Deleted transaction successfully.\n")


def display_transactions():
    transactions = get_all_transactions()
    
    if not transactions:
        print("No transactions found.\n")
        return

    print("\n")
    print("ID | Date       | Category    | Amount  | Currency")
    print("---|------------|-------------|---------|---------")
    for t in transactions:
        id, date, category, amount, currency = t
        print(f"{id:^2} | {date} | {category:11} | {amount:7.2f} | {currency}")
    print("\n")


def main():
    initialise_database()
    running = True

    print("=======================================\n" +
          "      Welcome to Finance Tracker      \n" +
          "=======================================\n")
    
    while running:
        print ("Select an option:\n" +
            "1. Add Transaction\n" +
            "2. Edit Transaction\n" +
            "3. Delete Transaction\n" +
            "4. View Transactions\n" +
            "5. Clear All Transactions\n" +
            "6. Visualise Transactions\n" +
            "7. Analyse Spending\n" +
            "8. Exit\n")
        
        choice = input()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            edit_transaction()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            display_transactions()
        elif choice == "5":
            clear_transactions()
            print("All transactions cleared.\n")
        elif choice == "6":
            pass  # Placeholder for visualisation feature
        elif choice == "7":
            pass  # Placeholder for analysis feature
        elif choice == "8":
            running = False
            print("Exiting Finance Tracker. Goodbye!")
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
