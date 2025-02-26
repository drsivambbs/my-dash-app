from dash.dependencies import Input, Output, State
from dash import html

def register_callbacks(app):
    """Registers Dash callbacks to enable interactivity."""

    # ✅ Toggle Sidebar Using Floating Button
    @app.callback(
        [Output("sidebar", "className"),
         Output("main-content", "className")],  # ✅ Ensure "main-content" exists in the layout
        [Input("sidebar-toggle", "n_clicks")],
        [State("sidebar", "className")],  # ✅ Get the current state of sidebar
        prevent_initial_call=True
    )
    def toggle_sidebar(n_clicks, current_class):
        """Toggles sidebar collapse & expand."""
        if "collapsed" in current_class:
            return "sidebar expanded", "main-content reduced"
        return "sidebar collapsed", "main-content expanded"

    # ✅ Toggle India Boundary Layer Visibility
    @app.callback(
        Output("india-boundary", "style"),  # Update GeoJSON layer style
        Input("toggle-layer", "value")  # Get value from toggle switch
    )
    def toggle_layer(is_checked):
        """Show/Hide the India boundary based on toggle switch state."""
        return {
            "color": "blue",
            "weight": 1 if is_checked else 0,
            "fillOpacity": 0
        }

    # ✅ Chip Selection & Active State
    @app.callback(
        [Output("tabs-content", "children"),
         Output("human-health", "className"),
         Output("animal-health", "className"),
         Output("environmental-health", "className")],
        [Input("human-health", "n_clicks"),
         Input("animal-health", "n_clicks"),
         Input("environmental-health", "n_clicks")],
        prevent_initial_call=True
    )
    def update_tab_content(human_clicks, animal_clicks, environment_clicks):
        """Updates content & highlights selected chip."""
        ctx = dash.callback_context
        if not ctx.triggered:
            return html.Div("📌 Select a category", style={"padding": "10px"}), "chip", "chip", "chip"

        selected_id = ctx.triggered[0]["prop_id"].split(".")[0]

        tab_content = {
            "human-health": html.Div("📌 Content for Human", style={"padding": "10px"}),
            "animal-health": html.Div("🐾 Content for Animal", style={"padding": "10px"}),
            "environmental-health": html.Div("🌍 Content for Environment", style={"padding": "10px"})
        }

        return (
            tab_content.get(selected_id, html.Div("⚠️ No content available", style={"padding": "10px", "color": "red"})),
            "chip active" if selected_id == "human-health" else "chip",
            "chip active" if selected_id == "animal-health" else "chip",
            "chip active" if selected_id == "environmental-health" else "chip"
        )
