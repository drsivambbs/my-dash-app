from dash import html, dcc  # ✅ Fix deprecated imports

# ✅ Function to create a Material Design-styled header
def create_header():
    return html.Div([
        html.Div("One Health 360", className="header-title"),

        html.Div([
            dcc.Link(html.Button("Home", className="material-button"), href="#"),
            dcc.Link(html.Button("Dashboard", className="material-button"), href="#"),
            dcc.Link(html.Button("Resources", className="material-button"), href="#"),
            dcc.Link(html.Button("About", className="material-button"), href="#"),
        ], className="nav-links")

    ], className="navbar")
