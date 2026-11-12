# client.py - starts the WeatherDemo server, discovers what it offers and uses it

import asyncio  # lets us run async code (code that waits for replies)

from mcp import ClientSession, StdioServerParameters  # the session (conversation) and the server start settings
from mcp.client.stdio import stdio_client  # opens the STDIO connection to the server

server_params = StdioServerParameters(  # how to launch the server
    command="mcp",  # run the mcp command line tool...
    args=["run", "server.py"],  # ...with these arguments, so it runs: mcp run server.py
    env=None,  # no extra environment variables
)


async def run():  # async function, because we wait for the server's answers
    async with stdio_client(server_params) as (read, write):  # start the server and open the read/write pipes
        async with ClientSession(read, write) as session:  # create a session on top of the pipes
            await session.initialize()  # handshake: client and server say hello

            resources = await session.list_resources()  # ask which resources exist
            print("Resources:", [str(r.uri) for r in resources.resources])  # print their addresses

            tools = await session.list_tools()  # ask which tools exist
            print("Tools:", [t.name for t in tools.tools])  # print their names

            cities = await session.read_resource("cities://list")  # read the cities resource
            print("cities://list ->")  # label for the output
            print(cities.contents[0].text)  # print the list of cities

            weather = await session.call_tool("get_weather", {"city": "Paris"})  # call the tool with city="Paris"
            print("get_weather(Paris) ->", weather.content[0].text)  # print the weather dictionary (as text)


if __name__ == "__main__":  # run only when the file is started directly
    asyncio.run(run())  # start the async function
