import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

binary_cmap = ListedColormap(['#FF6B35','#2E8B8B'])
# Load data 
df =pd.read_csv('data/raw/scores.csv')
# Define KPI Columns

social_kpis=['gender_wage_pct', 'contract_safety', 
            'payable_days', 'human_rights_training']

governance_kpis=['data_breach', 'sia_conducted',
            'rehab_resettlement', 'tier2_wages_pct']

environmental_kpis=['water_discharge', 'waste_intensity', 
            'scope3_emission']

kpi_cols = social_kpis + governance_kpis+environmental_kpis


#Sort by sector so companies are grouped visually

df=df.sort_values('Sector')
# Set Comapany name as index
df=df.set_index('Company')
# Keep only KPI columns
heatmap_data=df[kpi_cols]
heatmap_data=heatmap_data.astype(float)


# Create mask for NA cells
mask=heatmap_data.isnull()

# Create  canvas
fig,ax=plt.subplots(figsize=(19,20))
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
annot_kws={"size":7},
cmap=binary_cmap,
vmin=0,
vmax=1,
linewidths=0.5,
linecolor='gray',
cbar=False,
ax=ax
)

# Add vertical lines to separate the three KPI categories
ax.axvline(x=4,color='white',linewidth=3)
ax.axvline(x=8,color='white',linewidth=3)

# Add category labels above the columns
ax.text(2,-1.5,'SOCIAL',ha='center',fontsize=10,
fontweight='bold',color='#2E8B8B')

ax.text(6,-1.5,'GOVERNANCE',ha='center',fontsize=10,
fontweight='bold',color='#2E8B8B')

ax.text(9.5,-1.5,'ENVIRONMENTAL',ha='center',fontsize=10,
fontweight='bold',color='#2E8B8B')


#Add manual two item legend
legend_items=[
Patch(facecolor='#2E8B8B',label='Authentic Disclosure'),
Patch(facecolor='#FF6B35',label='Evasion or Manipulated')
]

ax.legend(handles=legend_items,loc='center right',
bbox_to_anchor=(1.01,0.5),fontsize=10,title='Disclosure',framealpha=1.0)




# Add title and labels
plt.title('BRSR Disclosure Quality Heatmap - Nifty 50 Companies',
fontsize=14,pad=20)
plt.xlabel('KPI Indicators',fontsize=11)
plt.ylabel('Company',fontsize=11)
plt.xticks(rotation=45,ha='right')
plt.yticks(rotation=0)

#Add source credit at the bottom
fig.text(0.5,-0.01,
'Source:BRSR disclosures in Annual Reports,FY2023-24|Nifty 50 companies',
ha='center',fontsize=9,color='gray',style='italic')


plt.tight_layout()

# Save the figure
plt.savefig('figures/heatmap.png',dpi=150,bbox_inches='tight')
print("heatmap saved to figures/heatmap.png")



plt.savefig('figures/brsr_heatmap_final.png',dpi=300,bbox_inches='tight')
print("Final heatmap saved to figures/brsr_heatmap_final.png")
