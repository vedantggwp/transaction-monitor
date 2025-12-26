from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('en_GB') # UK locale for UK data

def generate_transactions(num_transactions=100):
    """Generate fake banking transactions"""
    
    categories = ['Groceries', 'Transport', 'Entertainment', 'Bills', 'Shopping', 'Dining']
    transactions = []
    
    print(f"Generating {num_transactions} transactions...\n")
    
    for i in range(num_transactions):
        transaction = {
            'id' : i+1,
            'date' : fake.date_between(start_date='-30d', end_date='today'),
            'merchant' : fake.company(),
            'category' : random.choice(categories),
            'amount' : round(random.uniform(5.0, 500.0), 2),
            'account_holder' : fake.name()
            }
        transactions.append(transaction)
        
    return transactions
        

def display_transactions(transactions):
    """Display transactions in readable format"""
    
    print(f"{'ID':<5} {'Date':<12} {'Merchant':<25} {'Category':<15} {'Amount':>10}")
    print("-" * 75)
    
    for t in transactions:
        print(f"{t['id']:<5} {str(t['date']):<12} {t['merchant']:<25} {t['category']:<15} £{t['amount']:>8.2f}")
    
    print("\n" + "=" * 75)
    print(f"Total transactions: {len(transactions)}")
    print(f"Total amount: £{sum(t['amount'] for t in transactions):.2f}")

def flag_suspicious(transactions):
    """Flag potentially suspicious transactions"""
    
    suspicious = []
    
    for t in transactions:
        # Flag large transactions
        if t['amount'] > 300:
            suspicious.append((t, "Large transaction"))
    
    if suspicious:
        print("\n⚠️  SUSPICIOUS TRANSACTIONS DETECTED:")
        print("-" * 75)
        for trans, reason in suspicious:
            print(f"ID {trans['id']}: £{trans['amount']:.2f} at {trans['merchant']} - {reason}")
    else:
        print("\n✅ No suspicious transactions detected")

if __name__ == "__main__":
    # Generate transactions
    transactions = generate_transactions(100)
    
    # Display them
    display_transactions(transactions)
    
    # Flag suspicious ones
    flag_suspicious(transactions)
