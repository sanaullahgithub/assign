
## Reading data and libraries
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("C:\\Users\\user\\Downloads\\gdpdata.csv", skiprows=4)
print(data.head())


## Line plot.
country_name = 'Aruba'
country_data = data[data['Country Name'] == country_name]
years = list(country_data.columns[4:])  # Assuming columns from 4 onwards are the years.
gdp_values = country_data.iloc[:, 4:].values.flatten()
plt.plot(years, gdp_values, marker='o', linestyle='-', markersize=8)
plt.xlabel('Year')
plt.ylabel('GDP per capita (current US$)')
plt.title(f'{country_name} GDP per capita Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


## Bar Chart
year_to_visualize = '2021'
N = 10  # Number of top countries to display.
 Filter the data for the specified year.
year_data = data[['Country Name', year_to_visualize]]
year_data_sorted = year_data.sort_values(by=year_to_visualize, ascending=False)
top_N_data = year_data_sorted.head(N)
plt.barh(top_N_data['Country Name'], top_N_data[year_to_visualize])
plt.xlabel('GDP per capita (current US$)')
plt.ylabel('Country')
plt.title(f'Top {N} Countries with the Highest GDP per capita in {year_to_visualize}')
plt.show()

## Pie Chart 
year_to_visualize = '2021'
N = 10  # Number of top countries to consider.
year_data = data[['Country Name', year_to_visualize]]
year_data_sorted = year_data.sort_values(by=year_to_visualize, ascending=False)

top_N_data = year_data_sorted.head(N)
plt.pie(top_N_data[year_to_visualize], labels=top_N_data['Country Name'], autopct='%1.1f%%')
plt.title(f'GDP Contribution of the Top {N} Countries in {year_to_visualize}')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.show()