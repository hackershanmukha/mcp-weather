from typing import Any
import httpx
try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("weather")
except ImportError:
    from mcp.server.mcpserver import MCPServer
    mcp = MCPServer("weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get current weather for any city or country worldwide.

    Args:
        location: City or country name (e.g. London, Tokyo, Paris, Mumbai, New York)
    """
    async with httpx.AsyncClient() as client:
        # 1. Geocode the location name into latitude & longitude
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
        geo_res = await client.get(geo_url, timeout=15.0)
        geo_data = geo_res.json()

        if not geo_data.get("results"):
            return f"Could not find location: '{location}'. Please check the spelling."

        result = geo_data["results"][0]
        name = result.get("name")
        country = result.get("country", "")
        lat = result.get("latitude")
        lon = result.get("longitude")

        # 2. Fetch current weather from Open-Meteo (Global, Free)
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        )
        weather_res = await client.get(weather_url, timeout=15.0)
        weather_data = weather_res.json()

        current = weather_data.get("current", {})
        temp = current.get("temperature_2m")
        humidity = current.get("relative_humidity_2m")
        wind = current.get("wind_speed_10m")

        return f"""Weather for {name}, {country}:
- Temperature: {temp} °C
- Humidity: {humidity}%
- Wind Speed: {wind} km/h"""

def main():
    mcp.run()

if __name__ == "__main__":
    main()
