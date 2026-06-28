import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load data 
df =pd.read_csv('data/raw/scores.csv')
# Define KPI Columns
kpi_cols=kpi_cols = ['gender_wage_pct', 'contract_safety', 
            'payable_days', 'human_rights_training',
            'data_breach', 'sia_conducted', 
            'rehab_resettlement', 'tier2_wages_pct',
            'water_discharge', 'waste_intensity', 
            'scope3_emission']
#Set Company name as index
df=df.set_index('Company')
# Keep only KPI columns
heatmap_data=df[kpi_cols]
heatmap_data=heatmap_data.astype(float)


# Create mask for NA cells
mask=heatmap_data.isnull()

# Create  canvas
fig,ax=plt.subplots(figsize=(16,20))
ax.set_facecolor('#d3d3d3')

# Layer 1 - draw gray on NA cells
sns.heatmap(
heatmap_data,
mask=~mask,
cmap='Greys',
vmin=0,
vmax=1,
alpha=0.8,
cbar=False,
ax=ax
)

# Layer 2 - draw coloured heatmap on scored cells

sns.heatmap(
heatmap_data,
mask=mask,
annot=True,
fmt='g',
cmap='RdYlGn',
vmin=0,
vmax=1,
linewidths=0.5,
linecolor='gray',
ax=ax
)


# Add title and labels

plt.title('BRSR Disclosure Quality Heatmap - Nifty 50 Companies',
fontsize=14,pad=20)
plt.xlabel('KPI Indicators',fontsize=11)
plt.ylabel('Company',fontsize=11)
plt.xticks(rotation=45,ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Save the figure
plt.savefig('figures/heatmap.png',dpi=150,bbox_inches='tight')
print("heatmap saved to figures/heatmap.png")
