
import pandas as pd
from scipy.stats import poisson

df = pd.read_csv('datosSeleccionados.csv')

# Assuming you have a DataFrame named 'df' with a column named 'your_column'

# Create a new column to store the poisson distribution of each value
df['poisson_distribution'] = df['Dens-med'].apply(lambda x: poisson.pmf(k=range(0, int(x)+1), mu=x))

# Print the DataFrame
print(df)

# Flatten the list of probabilities into separate columns
df = pd.concat([df.drop('poisson_distribution', axis=1), df['poisson_distribution'].apply(pd.Series)], axis=1)

