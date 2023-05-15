import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

# Load the data info a pandas DataFrame

data = {
    'Reactor_ID': [1, 2, 3, 4, 5],
    'Location': ['USA', 'France', 'China', 'Japan', 'Russia'],
    'Capacity (MW)': [1000, 1500, 1200, 2000, 1800],
    'Status': ['Operational', 'Operational', 'Under Construction', 'Operational', 'Decomissioned']
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1("Nuclear Reactor Dashboard"),
        
        # Bar chart of reactor capacities
        dcc.Graph(
            figure=px.bar(df, x='Reactor_ID', y='Capacity (MW)', title='Reactor Capacities')
        ),
        
        # Map of reactor locations
        dcc.Graph(
            figure=px.scatter_geo(df, locations='Location', title='Reactor Locations')
        ),
        
        # Dropdown for operational status
        html.Label("Filter by Operational Status:"),
        dcc.Dropdown(
            id='status-dropdown',
            options=[
                {'label': 'Operational', 'value': 'Operational'},
                {'label': 'Under Construction', 'value': 'Under Construction'},
                {'label': 'Decommissioned', 'value': 'Decommissioned'}
            ],
            value='Operational',
            clearable=False
        ),
        
        # Filtered bar chart based on operational status
        dcc.Graph(id='filtered-bar-chart')
    ]
)

# Callback to update the filtered bar chart based on the selected operational status
@app.callback(
    dash.dependencies.Output('filtered-bar-chart', 'figure'),
    [dash.dependencies.Input('status-dropdown', 'value')]
)
def update_filtered_chart(status):
    filtered_df = df[df['Status'] == status]
    fig = px.bar(filtered_df, x='Reactor_ID', y='Capacity (MW)', title=f"Reactor Capacities ({status})")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)