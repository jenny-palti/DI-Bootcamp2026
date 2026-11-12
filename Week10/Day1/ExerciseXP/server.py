# server.py - a tiny MCP server with one tool and one resource

from mcp.server.fastmcp import FastMCP  # FastMCP is the easy way to build an MCP server

mcp = FastMCP("Demo")  # create the server and give it the name "Demo"


@mcp.tool()  # the decorator registers this function as a TOOL (an action the client can run)
def add(a: int, b: int) -> int:  # the tool takes two whole numbers and returns a whole number
    """Add two numbers."""  # this description is shown to the client when it lists the tools
    return a + b  # give back the sum


@mcp.resource("greeting://{name}")  # registers a RESOURCE (read-only info); {name} is a placeholder in the address
def greet(name: str) -> str:  # whatever is written in place of {name} arrives here as the "name" argument
    """Return a greeting for the given name."""  # description of the resource
    return f"Hello, {name}!"  # build the greeting text (an f-string puts the name inside)


if __name__ == "__main__":  # this runs only when the file is started directly
    mcp.run()  # start the server loop; by default it talks over STDIO (standard input/output)
