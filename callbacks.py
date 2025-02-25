from dash.dependencies import Input, Output

# ✅ Function to Register Callbacks
def register_callbacks(app):
    """Registers Dash callbacks to enable interactivity."""
    
    @app.callback(
        Output("india-boundary", "style"),  # Update the style of the GeoJSON layer
        Input("toggle-layer", "value")  # Get value from dropdown
    )
    def toggle_layer(selected_value):
        """Show/Hide the India boundary based on dropdown selection."""
        if selected_value == "show":
            return {"color": "blue", "weight": 1, "fillOpacity": 0}  # Show
        else:
            return {"color": "blue", "weight": 0, "fillOpacity": 0}  # Show
