# Welcome to NOTEBOOK 2: Manual annotation verification

# This notebook is designed to manually verify the classification of notes based on their sources.

import pandas as pd

df = pd.read_csv(#input Notes dataset clean_3 sep=',', encoding='utf-8')

# Filter for rows with EFCSN or EDMO sources
filtered_df = df[(df['noteFromEFCSN'] == 1) | (df['noteFromEDMO'] == 1)]

# Sample rows for manual annotation
sample_df = filtered_df.sample(n=100, random_state=43)

# Add 'verificationSource' column if missing
if 'verificationSource' not in df.columns:
    df['verificationSource'] = None

# Manual annotation loop
for idx, row in sample_df.iterrows():
    print("\n---")
    print(f"Note ID: {row['noteId']}")
    print(f"Source URL: {row['sourceURL']}")
    print(f"Domain: {row['domainExtract']}")
    print(f"Note text:\n{row['summary']}")
    print(f"EFCSN: {row['noteFromEFCSN']} | EDMO: {row['noteFromEDMO']}")
    
    while True:
        response = input("Is this classification correct? (1 = Yes, 0 = No): ").strip()
        if response in ['1', '0']:
            df.at[idx, 'verificationSource'] = int(response)
            break
        else:
            print("Invalid input. Please enter 1 or 0.")

# Save the updated DataFrame if desired
df.to_csv(# File path Notes dataset clean_4, index=False)
