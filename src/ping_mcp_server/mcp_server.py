import json
import logging
from typing import Annotated, Any

from fastmcp import Context, FastMCP
from pydantic import Field


from ping_mcp_server.ping import ping_host, check_connectivity

logger = logging.getLogger(__name__)


# FastMCP is an alternative interface for declaring the capabilities
# of the server. Its API is based on FastAPI.
class PingMCPServer(FastMCP):
    """
    A MCP server for pinging hosts.
    """

    def __init__(
        self,
        name: str = "ping-mcp-server",
        instructions: str | None = None,
        **settings: Any,
    ):

        super().__init__(name=name, instructions=instructions, **settings)

        self.setup_tools()


    def setup_tools(self):
        """
        Register the tools in the server.
        """

        self.tool(
            ping_host,
            name="ping-host",
            description="Ping a specified host.",
        )


        self.tool(
            check_connectivity,
            name="check-connectivity",
            description="Check if the internet connection is working.",
        )
