# 🌦️ Saige Weather MCP Server

[![PyPI version](https://img.shields.io/pypi/v/saige-weather-mcp.svg?color=blue)](https://pypi.org/project/saige-weather-mcp/)
[![Python versions](https://img.shields.io/pypi/pyversions/saige-weather-mcp.svg)](https://pypi.org/project/saige-weather-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, production-ready **Model Context Protocol (MCP)** server that delivers real-time weather information for any city or country worldwide using the free **Open-Meteo** API.

Compatible with **Claude Desktop**, **Cursor**, **Windsurf**, and custom AI agent workflows (LangChain, Groq, AutoGen).

---

## ✨ Features

- 🌍 **Worldwide Coverage:** Query weather for any city, country, or location worldwide (e.g., *Tokyo*, *London*, *Paris*, *Mumbai*, *New York*).
- 🔑 **Zero API Keys Required:** Uses Open-Meteo’s public geocoding and forecast APIs out of the box.
- ⚡ **Instant Execution with `uvx`:** Run immediately from PyPI without manual dependency installation or virtual environment clutter.
- 🔌 **Multiple Transports Supported:** Supports standard input/output (`stdio`) for desktop AI clients and Server-Sent Events (`SSE`) for network deployments.

---

## 🚀 Quick Start

### 1. Using directly with `uvx` (No installation needed)

You can launch and test the server immediately with Astral's `uvx`:

```bash
uvx saige-weather-mcp
```

Or test it interactively with the **MCP Inspector**:

```bash
npx @modelcontextprotocol/inspector uvx saige-weather-mcp
```

---

### 2. Adding to Claude Desktop

Add the following to your `claude_desktop_config.json`:

* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "weather": {
      "command": "uvx",
      "args": ["saige-weather-mcp"]
    }
  }
}
```

Restart Claude Desktop, and the hammer icon (🛠️) will appear with the `get_weather` tool available in your chat!

---

### 3. Using in Custom AI Assistants (e.g. LangChain / Groq)

In your MCP configuration file (e.g. `browser_mcp.json`):

```json
{
  "mcpServers": {
    "weather": {
      "command": "uvx",
      "args": ["saige-weather-mcp"]
    }
  }
}
```

Then run your assistant (`app.py`):

```python
from mcp_use import MCPClient, MCPAgent
from langchain_groq import ChatGroq

client = MCPClient("browser_mcp.json")
agent = MCPAgent(llm=ChatGroq(model_name="openai/gpt-oss-120b"), client=client)
```

---

## 🛠️ Tools Provided

### `get_weather`

Fetch live atmospheric conditions for any location.

* **Parameter:**
  * `location` *(string, required)*: The city, country, or landmark name. (e.g. `"London"`, `"Tokyo"`, `"Paris"`).

* **Example Output:**
  ```text
  Weather for London, United Kingdom:
  - Temperature: 10.2 °C
  - Humidity: 88%
  - Wind Speed: 12.4 km/h
  ```

---

## 💻 Local Development

If you want to contribute or modify this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hackershanmukha/mcp-weather.git
   cd mcp-weather
   ```

2. **Install dependencies using `uv`:**
   ```bash
   uv sync
   ```

3. **Run the development server with Inspector:**
   ```bash
   uv run mcp dev --with "mcp[cli]" server/wheater.py
   ```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
