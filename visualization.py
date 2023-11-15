import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations'
    colorscale = 'Purples',
    colorbar_title = "Number of visits",
))

fig.update_layout(
    title_text = 'Map of the USA based on the number of times states have been visited by students',
    geo_scope='usa', # limite map scope to USA
)

fig.show()