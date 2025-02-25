import dash_html_components as html

# ✅ Function to create a styled header component
def create_header():
    return html.Div([
        # Left-aligned title
        html.Div("One Health 360", style={
            "fontSize": "24px",
            "fontWeight": "bold",
            "color": "white",
            "display": "inline-block",
            "marginLeft": "20px"
        }),
        
        # Right-aligned navigation links
        html.Div([
            html.A("Home", href="#", style={"color": "white", "marginRight": "20px"}),
            html.A("Dashboard", href="#", style={"color": "white", "marginRight": "20px"}),
            html.A("Resources", href="#", style={"color": "white", "marginRight": "20px"}),
            html.A("About", href="#", style={"color": "white"})
        ], style={"float": "right", "marginRight": "20px"})
    ], style={
        "backgroundColor": "#1976D2",  # Blue background
        "padding": "10px",
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center"
    })
