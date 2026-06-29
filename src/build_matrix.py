import pandas as pd

# Load raw data
df=pd.read_csv('data/raw/scores.csv')

# Define KPI Columns

kpi_cols = ['gender_wage_pct','contract_safety','payable_days','human_rights_training','data_breach','sia_conducted','rehab_resettlement','tier2_wages_pct','water_discharge','waste_intensity','scope3_emission']


# Save disclosure matrix (wide format, sorted by sector)
matrix= df.sort_values('Sector').set_index('Company')
matrix[kpi_cols].to_csv('data/processed/disclosure_matrix.csv')
print('Saved disclosure_matrix.csv')


# Calculate disclosure rate per sector

df['disclosure_rate'] = df[kpi_cols].mean(axis=1)
sector_summary=df.groupby('Sector') ['disclosure_rate'].mean()
sector_summary=sector_summary.sort_values(ascending=True)
sector_summary.to_csv('data/processed/sector_summary.csv',header=True)
print("Saved sector_summary.csv")

#Print findings to screen

print("\nSector disclosure rates(worst to  best):")
print(sector_summary.round(2).to_string())
