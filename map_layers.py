import json
import dash_leaflet as dl
from config import GOOGLE_MAPS_TILE_URL  # Import the Google Maps URL

# ✅ Load India's GeoJSON Data
def load_geojson(file_path="maps/india_states.geojson"):
    """Load GeoJSON file and return data."""
    with open(file_path, "r") as f:
        return json.load(f)

# ✅ Function to Create the Google Maps Layer
def google_maps_layer():
    """Returns Google Maps tile layer."""
    return dl.TileLayer(url=GOOGLE_MAPS_TILE_URL, attribution="Google Maps")

# ✅ Function to Create India's Boundary Layer
def india_boundary_layer():
    """Returns India's boundary as a GeoJSON layer."""
    india_geojson = load_geojson()
    return dl.GeoJSON(
        id="india-boundary",
        data=india_geojson,
        style={"color": "blue", "weight": 1, "fillOpacity": 0}  # Blue border, transparent inside
    )

# ✅ Function to Create a Complete Map
def create_map():
    """Returns a complete Leaflet Map."""
    return dl.Map(
        id="map",
        style={'width': '100%', 'height': '600px'},  # Define map size
        center=[22.3511, 78.6677],  # Centered on India
        zoom=5,  # Default zoom level
        children=[
            google_maps_layer(),  # Add Google Maps
            india_boundary_layer()  # Add India GeoJSON Layer
        ]
    )
