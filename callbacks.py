from dash.dependencies import Input, Output

# ✅ Function to Register Callbacks
def register_callbacks(app):
    """Registers Dash callbacks to enable interactivity."""
    
    @app.callback(
        Output("india-boundary", "style"),  # Update the style of the GeoJSON layer
        Input("toggle-layer", "value")  # Get value from toggle switch
    )
    def toggle_layer(is_checked):
        """Show/Hide the India boundary based on toggle switch state."""
        if is_checked:  # If True, show the boundary
            return {"color": "blue", "weight": 1, "fillOpacity": 0}
        else:  # If False, hide the boundary
            return {"color": "blue", "weight": 0, "fillOpacity": 0}
