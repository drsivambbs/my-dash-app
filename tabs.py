from dash import html

def create_tabs():
    """Creates a sidebar with icon-based chips."""
    tab_data = [
        ("human-health", "person", "Human"),
        ("animal-health", "pets", "Animal"),
        ("environmental-health", "public", "Environment"),
    ]

    return html.Div([
        html.Div([
            html.Button([
                html.I(className="material-icons", children=icon),
                html.Span(label, className="chip-label")
            ], id=tab_id, className="chip", n_clicks=0)
            for tab_id, icon, label in tab_data
        ], className="chip-container"),
    ], className="sidebar-content")
