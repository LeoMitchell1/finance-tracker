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


def update_transaction_to_db(transaction_id, date=None, category=None, amount=None, currency=None):
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    # Error checking for values
    if date is not None:
        fields.append("date = ?")
        values.append(date)
    if category is not None:
        fields.append("category = ?")
        values.append(category)
    if amount is not None:
        fields.append("amount = ?")
        values.append(amount)
    if currency is not None:
        fields.append("currency = ?")
        values.append(currency)

    sql = f"UPDATE transactions SET {', '.join(fields)} WHERE id = ?"
    values.append(transaction_id)

    cursor.execute(sql, tuple(values))
    conn.commit()
    conn.close()


def delete_transaction_in_db(t):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
        """, (t.id,))
    
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