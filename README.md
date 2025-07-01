

## Run Ping MCP Server SSE

```sh
FASTMCP_HOST="0.0.0.0" FASTMCP_PORT=1234 uv run ping-mcp-server
```

## Pytest

```sh
uv run pytest
```

## Pytest Coverage Test

```sh
uv run pytest --cov=src/ --cov-report=term-missing --cov-fail-under=70
```


# MCP Inspector

```sh
npx -y @modelcontextprotocol/inspector
```