
<br />

<div align="center">
  <h1>ping mcp server</h1>
  <p><h3 align="center">MCP Server to Ping Other hosts 🚀</h3></p>
</div>

[Upwork Job]()
&nbsp;&nbsp;•&nbsp;&nbsp;


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


## 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.huzaifairfan.com"><img src="https://img.shields.io/badge/-huzaifairfan.com-1aa260?style=flat&logo=Google-Chrome&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/huzaifairfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-0072b1?style=flat&logo=Linkedin&logoColor=white"/></a>
<a href="https://github.com/HuzaifaIrfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-4078c0?style=flat&logo=Github&logoColor=white"/></a>
<a href="mailto:contact@huzaifairfan.com"><img src="https://img.shields.io/badge/-contact@huzaifairfan.com-c71610?style=flat&logo=Gmail&logoColor=white"/></a>
</p>

## License

Licensed under the MIT License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)