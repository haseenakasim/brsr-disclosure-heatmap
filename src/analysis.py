import pandas as pd
# Load the data
df = pd.read_csv('data/raw/scores.csv')
# Define KPI Columns
kpi_cols =['gender_wage_pct','contract_safety','payable_days', 'human_rights_training','data_breach','sia_conducted','rehab_resettlement','tier2_wages_pct','water_discharge','waste_intensity','scope3_emission']
# Calculate average score per company
# na ignored means NA cells are excluded from average
df['average_score'] =df[kpi_cols].mean(axis=1)
# show company scores
print("\nAverage score per company:")
print(df[['Company','average_score']].to_string())
# show first few rows
print("first 5 rows:")
print(df.head())
# show shape
print("\nNumber of companies and columns:")
print(df.shape)
#show column names
print("\nColum names:")
print(df.columns.tolist())
# check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())
# Average score per sector
print("\nAverage score per sector:")
sector_scores=df.groupby('Sector') ['average_score'].mean()
print(sector_scores.to_string())
