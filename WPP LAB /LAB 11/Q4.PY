import pandas as pd
import numpy as np

data = {
    'John': [True, False, True, False, True, True, False, False, True, False],
    'Judy': [True, False, False, False, True, False, True, False, True, True]
}

df = pd.DataFrame(data)
df['party'] = df['John'] & df['Judy']
party_days = df.index[df['party']].tolist()
days_til_party = []

for i in range(len(df)):
    future_parties = [day - i for day in party_days if day >= i]
    if future_parties:
        days_til_party.append(future_parties[0])
    else:
        days_til_party.append(-1)

df['days_til_party'] = days_til_party
df.drop(columns='party', inplace=True)
print(df)
