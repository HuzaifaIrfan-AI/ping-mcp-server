<div align="center">
  <h1>ping mcp server</h1>
  <p><h3 align="center">MCP Server to Ping Other hosts 🚀</h3></p>
</div>


# 🚀 Usage
## Run Ping MCP Server SSE

```sh
FASTMCP_HOST="0.0.0.0" FASTMCP_PORT=1234 uv run ping-mcp-server
```

## Test

```sh
uv run pytest
```

### MCP Inspector

```sh
npx -y @modelcontextprotocol/inspector
```

## Claude Configuration

```json
{
    "mcpServers": {
        "ping": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "http://localhost:1234/sse",
                "--allow-http"
            ]
        }
    }
}
```

![claude](claude.jpg)

# 📝 Documentation

# 📚 References


# 🤝🏻 Connect with Me

## Huzaifa Irfan

- 💬 Just want to say hi?
- 🚀 Have a project to discuss?
- 📧 Email me @: [hi@huzaifairfan.com](mailto:hi@huzaifairfan.com)
- 📞 Visit my Profile for other channels:

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)
<hr />

Last Updated on 2025-07-13
