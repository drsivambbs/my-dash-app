import dash
from dash import html, dcc
from dash_daq import ToggleSwitch

import map_layers
import callbacks
import header
import tabs

# ✅ Initialize Dash App
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# ✅ Define Layout
app.layout = html.Div([
    html.Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap"),
    html.Link(rel="stylesheet", href="https://fonts.googleapis.com/icon?family=Material+Icons"),

    header.create_header(),

    # ✅ Floating Sidebar Toggle Button
    html.Button(html.I("menu", className="material-icons"), id="sidebar-toggle", className="sidebar-floating-btn"),

    html.Div([
        # ✅ Sidebar (Collapsible)
        html.Div([
            html.Div(tabs.create_tabs(), id="sidebar-content", className="sidebar-content"),  
        ], id="sidebar", className="sidebar expanded"),  

        # ✅ Main Content (Ensure `id="main-content"` Exists)
        html.Div([
            # ✅ Toggle Inside the Map (Top-Right)
            html.Div([
                html.Label("Add Layers", className="toggle-label"),
                ToggleSwitch(id="toggle-layer", value=True, color="#007bff", size=35)
            ], className="map-layer-control"),  

            map_layers.create_map()
        ], id="main-content", className="main-content expanded")  # ✅ Ensure `id="main-content"` is included
    ], className="main-container")
])

# ✅ Register Callbacks After App Initialization
callbacks.register_callbacks(app)

# ✅ Run Dash Server
if __name__ == '__main__':
    app.run_server(debug=True)
