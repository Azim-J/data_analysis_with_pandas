import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('world_population.csv')
#print(df.describe())
#print(df.info())
heatmap_data = df.set_index('World Population Percentage').sort_values(by='World Population Percentage', ascending=False).set_index('Country')
#print(df.info())
heatmap_data=heatmap_data.iloc[0:20, 5:10]
plt.title("Populations of Top 5 most populous countries")
plt.ylabel("Countries")
plt.xlabel("Population")
sns.heatmap(data=heatmap_data, annot=True)
plt.show()
bar_data=df.set_index("CCA3").iloc[0:14]
plt.title("Area of countries")
plt.ylabel("Area")
plt.xlabel("Countries")
sns.barplot(x=bar_data.index, y=bar_data['Area (km²)'])
plt.show()
scatter_data_1 = df.sort_values(by='Area (km²)', ascending=False).iloc[0:99]
plt.title("Relation of Countries's with the Top Area (km²) to their World Population Percentage")
plt.xlabel("Area")
plt.ylabel("World Population Percentage")
sns.regplot(scatter_data_1, y="World Population Percentage", x='Area (km²)')
plt.show()
scatter_data_2=df.iloc[0:99]
plt.title("Relation between Area and density for each continent")
plt.xlabel("Density")
plt.ylabel("Area")
sns.lmplot(data=scatter_data_2, y="Density (per km²)", x='Area (km²)', hue="Continent")
plt.show()