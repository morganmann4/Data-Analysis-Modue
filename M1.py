#%%
import pandas as pd
import altair as alt

# Read data into pandas data frame
file = pd.read_csv('output.csv')

#%%
# Print Data Frame
file.head()

# Print end of data 
file.tail()

#%%
# Which region is happiest?

dat1 = file.filter([
    'Country', 'Region','Happiness Score']).groupby(
        'Region').mean().sort_values(by='Happiness Score', ascending=False)

# Output
dat1.head(7)

#%%
# Is economy correlated with happiness?

dat2 = file.groupby(
    'Country').mean().filter([
        'Country','Happiness Score', 'Economy (GDP per Capita)'
                ]).sort_values(by='Economy (GDP per Capita)', ascending=False)

# Output
dat2.head(7)

#%%
# Chart
chart = alt.Chart(file).mark_point().encode(
    x=alt.X('Economy (GDP per Capita)'),
    y='Happiness Score',
    color='Region')

chart



# %%
