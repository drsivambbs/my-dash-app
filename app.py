import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_daq import ToggleSwitch  # Import Google Material toggle switch
from map_layers import create_map  # Import the map function
from callbacks import register_callbacks  # Import callback functions
from header import create_header  # Import the header function

# ✅ Initialize Dash App
app = dash.Dash(__name__)

# ✅ Define Layout
app.layout = html.Div([
    create_header(),  # ✅ Add the styled header
    
    # ✅ Google Material Toggle Button to Show/Hide India Boundary
    html.Div([
        html.Label("Toggle India Boundary", style={"marginRight": "10px"}),
        ToggleSwitch(
            id="toggle-layer",
            value=True  # Default: Show boundary
        )
    ], style={"display": "flex", "alignItems": "center", "justifyContent": "center", "margin": "20px"}),
    
    # ✅ Add the Map
    create_map()
])

# ✅ Register Callbacks
register_callbacks(app)

# ✅ Run Dash Server
if __name__ == '__main__':
    app.run_server(debug=True)
