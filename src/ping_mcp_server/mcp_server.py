import json
import logging
from typing import Annotated, Any

from fastmcp import Context, FastMCP
from pydantic import Field


from ping_mcp_server.ping import run_ping_command

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


        async def ping_host(host: str, count: int = 4) -> str:
            """Ping a specified host.

            Args:
                host: The hostname or IP address to ping
                count: Number of ping packets to send (default: 4)
            """
            if count < 1 or count > 20:
                return "Error: Count must be between 1 and 20."
            
            result = await run_ping_command(host, count)
            return result


        async def check_connectivity(host: str = "8.8.8.8") -> str:
            """Check if the internet connection is working by pinging a reliable host.

            Args:
                host: The hostname or IP address to ping (default: 8.8.8.8, Google's DNS)
            """
            result = await run_ping_command(host, 1)
            
            # Simple analysis of the ping result
            if "time=" in result.lower() or "bytes from" in result.lower():
                return f"Internet connection is working! Successfully pinged {host}.\n\n{result}"
            else:
                return f"Internet connection seems to be down or there's an issue reaching {host}.\n\n{result}"


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
