# Week 10, Day 1 – Daily Challenge: MCP Ping-Pong

A tiny MCP server (`server.py`, name `WeatherDemo`) and a client (`client.py`) that talk over STDIO. No LLM is used.

## Setup
```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install "mcp[cli]<2"       # <2 because mcp 2.x renamed FastMCP and changed other names
```

## Run
```
python client.py     # the client starts the server by itself
```
Two-terminal version for debugging: `mcp run server.py` in one terminal, `python client.py` in the other.

## Expected output
Resource list, tool list, the cities (Paris, London, NYC), and the weather dictionary for Paris.
Paste your own terminal capture below after running it.
