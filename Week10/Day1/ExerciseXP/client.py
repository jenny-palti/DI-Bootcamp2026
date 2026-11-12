# client.py - starts server.py, asks what it offers, then uses it

import asyncio  # asyncio lets us run "async" code (code that waits for answers)

from mcp import ClientSession, StdioServerParameters  # ClientSession = the conversation; StdioServerParameters = how to start the server
from mcp.client.stdio import stdio_client  # opens the STDIO connection to the server

server_params = StdioServerParameters(  # describes how to launch the server
    command="mcp",  # the program to run: the mcp command line tool
    args=["run", "server.py"],  # its arguments, so it runs: mcp run server.py
    env=None,  # no extra environment variables
)


async def run():  # an async function, because talking to the server means waiting for replies
    async with stdio_client(server_params) as (read, write):  # start the server and open the two pipes (read and write)
        async with ClientSession(read, write) as session:  # create a session on top of those pipes
            await session.initialize()  # the "hello" handshake between client and server

            resources = await session.list_resources()  # ask for the fixed resources
            templates = await session.list_resource_templates()  # ask for resources with a {placeholder} in the address
            print("Resources:", [str(r.uri) for r in resources.resources])  # print their addresses (empty here)
            print("Resource templates:", [t.uriTemplate for t in templates.resourceTemplates])  # print the template addresses

            tools = await session.list_tools()  # ask which tools the server has
            print("Tools:", [t.name for t in tools.tools])  # print the tool names

            greeting = await session.read_resource("greeting://hello")  # read the resource, using "hello" as the name
            print("greeting://hello ->", greeting.contents[0].text)  # print the text we got back

            result = await session.call_tool("add", {"a": 1, "b": 7})  # run the add tool with a=1 and b=7
            print("add(1, 7) ->", result.content[0].text)  # print the answer


if __name__ == "__main__":  # run only when the file is started directly
    asyncio.run(run())  # start the async function
