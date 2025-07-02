
from unittest.mock import patch
from ping_mcp_server.ping import run_ping_command

import pytest

@pytest.mark.asyncio
async def test_run_ping_command_success():
    output = await run_ping_command("127.0.0.1", count=1)
    assert "1 packets transmitted" in output or "1 received" in output

@pytest.mark.asyncio
async def test_run_ping_command_failure():
    output = await run_ping_command("nonexistent.host.local", count=1)
    assert "Error" in output    