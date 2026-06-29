import pandas as pd
import matplotlib.pyplot as plt

# load sector summary
sector_summary = pd.read_csv('data/processed/sector_summary.csv',index_col='Sector')

#Create figure
fig,ax = plt.subplots(figsize=(10,7))

#Draw horizontal bar chart
sector_summary['disclosure_rate'].plot(
kind='barh',
color='#2E8B8B',
edgecolor='white',
label='_nolegend_',
ax=ax
)


#labels and title
ax.set_xlabel('Average Disclosure Rate',fontsize=11)
ax.set_title('BRSR Disclosure Rate by Sector - Nifty 50(FY2023-2024)', fontsize=13)
ax.axvline(x=0.8,color='#FF6B35',linestyle='--',linewidth=1.5)
ax.text(0.81,0.02,'0.8 threshold',color ='#FF6B35',fontsize=9,
transform=ax.get_xaxis_transform(),va='bottom')
plt.tight_layout()


plt.savefig('figures/sector_disclosure_rates.png',dpi=150,bbox_inches='tight')
print("saved sector_disclosure_rates.png")
