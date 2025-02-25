import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get Google Maps API Key from .env file
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# ✅ Define the Google Maps Tile URL
GOOGLE_MAPS_TILE_URL = f"https://mt1.google.com/vt/lyrs=m&x={{x}}&y={{y}}&z={{z}}&key={GOOGLE_MAPS_API_KEY}"
