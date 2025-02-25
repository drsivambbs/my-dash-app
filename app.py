import dash
import dash_html_components as html
import dash_core_components as dcc
from map_layers import create_map  # Import the map function
from callbacks import register_callbacks  # Import callback functions

# ✅ Initialize Dash App
app = dash.Dash(__name__)

# ✅ Define Layout
app.layout = html.Div([
    # Dropdown to show/hide India boundary
    dcc.Dropdown(
        id="toggle-layer",
        options=[
            {"label": "Show India Boundary", "value": "show"},
            {"label": "Hide India Boundary", "value": "hide"}
        ],
        value="show",  # Default: Show boundary
        clearable=False  # Prevent clearing selection
    ),
    
    # ✅ Add the Map
    create_map()
])

# ✅ Register Callbacks
register_callbacks(app)

# ✅ Run Dash Server
if __name__ == '__main__':
    app.run_server(debug=True)
