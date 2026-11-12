# server.py - WeatherDemo: an MCP server with one tool and one resource (no AI model involved)

import logging  # logging lets us print messages so we can SEE when the server is used
import sys  # sys gives us access to stderr (the error/log output stream)

from mcp.server.fastmcp import FastMCP  # FastMCP is the easy way to build an MCP server

logging.basicConfig(level=logging.INFO, stream=sys.stderr)  # send log messages to stderr, so they don't mix with the MCP messages on stdout
log = logging.getLogger("WeatherDemo")  # create a logger with the server's name

mcp = FastMCP("WeatherDemo")  # create the server and name it "WeatherDemo"

WEATHER = {  # a small in-memory "database": city name -> fixed weather data
    "Paris": {"temp_c": 21, "condition": "sunny"},  # Paris weather
    "London": {"temp_c": 15, "condition": "cloudy"},  # London weather
    "NYC": {"temp_c": 24, "condition": "rainy"},  # New York weather
}


@mcp.tool()  # registers the function below as a TOOL the client can call
def get_weather(city: str) -> dict:  # takes a city name (text) and returns a dictionary
    """Return static weather data for a city."""  # description shown when the client lists the tools
    log.info("get_weather called with city=%s", city)  # log that the tool was called
    if city not in WEATHER:  # if we do not know this city...
        return {"error": f"Unknown city: {city}", "supported": list(WEATHER)}  # ...return an error dictionary
    data = WEATHER[city]  # look up the city's data
    return {"city": city, "temp_c": data["temp_c"], "condition": data["condition"]}  # return the weather as a dictionary


@mcp.resource("cities://list")  # registers a RESOURCE (read-only info) at the address cities://list
def list_cities() -> str:  # returns text
    """Newline-separated list of supported cities."""  # description
    log.info("cities://list read")  # log that the resource was read
    return "\n".join(WEATHER)  # join the city names with a new line between each one


if __name__ == "__main__":  # run only when the file is started directly
    mcp.run()  # start the server loop (STDIO by default)
