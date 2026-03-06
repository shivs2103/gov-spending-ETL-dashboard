import pandas as pd

# Extract
df = pd.read_csv("../data/raw/gov_spending.csv")
print(df.columns)

# Transform
df.dropna(inplace=True)
df['amount_spent'] = df['amount_spent'].astype(float)
df['beneficiaries'] = df['beneficiaries'].astype(int)

# Create dimension tables
dim_state = df[['state']].drop_duplicates().reset_index(drop=True)
dim_state['state_id'] = dim_state.index + 1

dim_department = df[['department']].drop_duplicates().reset_index(drop=True)
dim_department['department_id'] = dim_department.index + 1

dim_scheme = df[['scheme']].drop_duplicates().reset_index(drop=True)
dim_scheme['scheme_id'] = dim_scheme.index + 1

dim_time = df[['year']].drop_duplicates().reset_index(drop=True)
dim_time['time_id'] = dim_time.index + 1

# Merge IDs into fact table
fact = df.merge(dim_state, on='state')
fact = fact.merge(dim_department, on='department')
fact = fact.merge(dim_scheme, on='scheme')
fact = fact.merge(dim_time, on='year')

fact_table = fact[['state_id','department_id','scheme_id','time_id','amount_spent','beneficiaries']]

# Save processed files
dim_state.to_csv("../data/processed/dim_state.csv", index=False)
dim_department.to_csv("../data/processed/dim_department.csv", index=False)
dim_scheme.to_csv("../data/processed/dim_scheme.csv", index=False)
dim_time.to_csv("../data/processed/dim_time.csv", index=False)
fact_table.to_csv("../data/processed/fact_spending.csv", index=False)

print("ETL Completed Successfully")