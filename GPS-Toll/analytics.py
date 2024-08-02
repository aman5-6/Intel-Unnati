import pandas as pd
def generate_report(vehicles, user_accounts):
    report = pd.merge(vehicles, user_accounts, on='vehicle_id')
    print(report)

