import pandas as pd

user_accounts = pd.DataFrame({
    'vehicle_id': [1, 2],
    'balance': [100, 100]
})

def deduct_toll(vehicle_id, toll):
    global user_accounts
    user_accounts.loc[user_accounts['vehicle_id'] == vehicle_id, 'balance'] -= toll
    print(f"Vehicle {vehicle_id} charged {toll}, new balance: {user_accounts.loc[user_accounts['vehicle_id'] == vehicle_id, 'balance'].values[0]}")

