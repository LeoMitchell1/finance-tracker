import sqlite3
from pathlib import Path

# Define the database path
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "finance.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)

    return conn


def initialise_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            currency TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()


def add_transaction_to_db(t):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (date, category, amount, currency)
        VALUES (?, ?, ?, ?)
    """, (t.date, t.category, t.amount, t.currency))

    conn.commit()
    conn.close()


def update_transaction_to_db(t):
    conn = get_connection()
    cursor = conn.cursor()

    # print(f"ID: {transaction_id}, date: {date}, category: {category}, amount: {amount}, currency: {currency}")

    fields = []
    values = []

    # Error checking for values
    if t.date is not None:
        fields.append("date = ?")
        values.append(t.date)
    if t.category is not None:
        fields.append("category = ?")
        values.append(t.category)
    if t.amount is not None:
        fields.append("amount = ?")
        values.append(float(t.amount))
    if t.currency is not None:
        fields.append("currency = ?")
        values.append(t.currency)

    if not fields:
        print("No fields to update.")
        return

    print(f"Updating transaction ID {t.id} with fields: {fields}")
    sql = f"UPDATE transactions SET {', '.join(fields)} WHERE id = ?"
    values.append(t.id)

    print(f"Executing SQL: {sql} with values: {values}")

    cursor.execute(sql, tuple(values))
    conn.commit()
    conn.close()


def delete_transaction_in_db(t):
    conn = get_connection()
    cursor = conn.cursor()

    print(f"Deleting transaction with ID: {t.id}")

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
        """, (t.id,))
    
    conn.commit()
    conn.close()


def clear_transactions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions")

    conn.commit()
    conn.close()


def get_all_transactions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        ORDER BY date DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows