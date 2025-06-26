from mcp.server.fastmcp import FastMCP
import wikipedia
import os
import json

# -----------------------------
# Initialize the MCP Server
# -----------------------------
# This line initializes the MCP server instance with the name "DefenseTech".
mcp = FastMCP("DefenseTech")

# -----------------------------
# Static Weapon/Tech Database
# -----------------------------
# This dictionary contains manually defined information about specific defense weapons.
WEAPON_DATABASE = {
    "BrahMos": {
        "type": "Cruise Missile",
        "origin": "India-Russia",
        "range_km": 500,
        "speed": "Mach 3",
        "used_by": ["India", "Philippines"]
    },
    "Agni-V": {
        "type": "Ballistic Missile",
        "origin": "India",
        "range_km": 5000,
        "speed": "Mach 24",
        "used_by": ["India"]
    },
    "MQ-9 Reaper": {
        "type": "Drone",
        "origin": "USA",
        "range_km": 1850,
        "speed": "482 km/h",
        "used_by": ["USA", "UK", "Italy"]
    },
    "T-90": {
        "type": "Tank",
        "origin": "Russia",
        "range_km": 550,
        "speed": "60 km/h",
        "used_by": ["Russia", "India", "Algeria"]
    },
    "Green Pine": {
        "type": "Radar",
        "origin": "Israel",
        "range_km": 500,
        "speed": "N/A",
        "used_by": ["Israel", "India", "South Korea"]
    }
}

# -----------------------------
# Category Map for Resource Access
# -----------------------------
# This dictionary maps categories to a list of weapons belonging to that category.
CATEGORY_MAP = {
    "missile": ["BrahMos", "Agni-V"],
    "drone": ["MQ-9 Reaper"],
    "tank": ["T-90"],
    "radar": ["Green Pine"]
}

# -----------------------------
# File-based Cache for Wikipedia Results
# -----------------------------
CACHE_FILE = "cache.json"

def load_cache():
    """
    Load cached weapon data from cache.json file.

    Returns:
        dict: A dictionary containing cached Wikipedia results.
    """
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache_data):
    """
    Save updated cache data to the cache.json file.

    Args:
        cache_data (dict): The cache data to save.
    """
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, indent=4, ensure_ascii=False)

# -----------------------------
# TOOL: tech_info
# -----------------------------
@mcp.tool()
def tech_info(weapon: str) -> dict:
    """
    Returns technical information about a defense weapon.

    This tool first checks the local static database (WEAPON_DATABASE),
    then checks previously saved Wikipedia results (cache.json),
    and finally queries Wikipedia for a short summary if no local data is found.

    Args:
        weapon (str): The name of the weapon to look up (e.g., "BrahMos").

    Returns:
        dict: A dictionary containing the source and available weapon data, or an error message.
              Possible sources: "local", "cache", "wikipedia".
    """
    weapon = weapon.strip()

    # 1. Check static local DB
    local_data = WEAPON_DATABASE.get(weapon)
    if local_data:
        return {"source": "local", "weapon": weapon, **local_data}

    # 2. Check cache.json
    cache = load_cache()
    cached_data = cache.get(weapon)
    if cached_data:
        return {"source": "cache", "weapon": weapon, **cached_data}

    # 3. Fetch from Wikipedia if not in cache
    try:
        summary = wikipedia.summary(weapon, sentences=3)
        url = wikipedia.page(weapon).url
        wiki_data = {
            "summary": summary,
            "url": url
        }

        # Save result to cache.json for next time
        cache[weapon] = wiki_data
        save_cache(cache)

        return {"source": "wikipedia", "weapon": weapon, **wiki_data}

    except wikipedia.exceptions.DisambiguationError as e:
        return {
            "error": f"Too many results for '{weapon}'. Try one of: {e.options[:5]}"
        }
    except wikipedia.exceptions.PageError:
        return {
            "error": f"No Wikipedia page found for: {weapon}"
        }
    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)}"
        }

# -----------------------------
# RESOURCE: equipment://{category}
# -----------------------------
@mcp.resource("equipment://{category}")
def get_category_equipment(category: str) -> dict:
    """
    Returns all weapons or equipment under a given category.

    This MCP resource allows dynamic access by category name.

    Args:
        category (str): The equipment category name (e.g., "missile", "drone", "tank", "radar").

    Returns:
        dict: A dictionary containing the category and a list of weapons under it,
              or an error message if the category is not found.
    """
    category = category.strip().lower()
    items = CATEGORY_MAP.get(category)

    if items:
        return {"category": category, "items": items}
    else:
        return {"error": f"No equipment found for category: {category}"}
