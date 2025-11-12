from transaction import Transaction
from database import initialise_database, add_transaction_to_db, update_transaction_to_db, delete_transaction_in_db, get_all_transactions


def add_transaction():
    amount = float(input("Enter amount: "))
    currency = input("Enter currency (e.g., USD, EUR): ")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent): ")

    transaction = Transaction(amount, currency, date, category)
    add_transaction_to_db(transaction)
    print(f"Added: {transaction}\n")


def edit_transaction():
    display_transactions()
    transaction_id = int(input("Enter transaction ID to edit: "))

    for t in get_all_transactions():
        if t[0] == transaction_id:
            transaction = Transaction(t[1], t[2], t[3], t[4])
            break

    amount = float(input("Enter new amount (or leave blank to keep current): ") or 0)
    currency = input("Enter new currency (or leave blank to keep current): ")
    date = input("Enter new date (YYYY-MM-DD) (or leave blank to keep current): ")
    category = input("Enter new category (or leave blank to keep current): ")

    if amount is not None:
        transaction.amount = amount
    if currency is not None:
        transaction.currency = currency
    if date is not None:
        transaction.date = date
    if category is not None:
        transaction.category = category

    update_transaction_to_db(transaction)
    print(f"Updated transaction: {transaction}\n", transaction)


def delete_transaction(transaction):
    delete_transaction_in_db(transaction)
    print(f"Deleted transaction successfully.\n")


def display_transactions():
    transactions = get_all_transactions()
    
    if not transactions:
        print("No transactions found.\n")
        return

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
            "5. Visualise Transactions\n" +
            "6. Analyse Spending\n" +
            "7. Exit\n")
        
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
            pass  # Placeholder for visualisation feature
        elif choice == "6":
            pass  # Placeholder for analysis feature
        elif choice == "7":
            running = False
            print("Exiting Finance Tracker. Goodbye!")


if __name__ == "__main__":
    main()
