import matplotlib.pyplot as plt
import pandas as pd
from database import get_all_transactions

# Fetch transactions
transactions = get_all_transactions()

# Create DataFrame
df = pd.DataFrame(transactions, columns=["id", "date", "category", "amount", "currency"])

# Convert 'date' column to datetime for plotting
df['date'] = pd.to_datetime(df['date'])

