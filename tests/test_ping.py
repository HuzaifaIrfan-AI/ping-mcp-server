
from unittest.mock import patch
from ping_mcp_server.ping import run_ping_command, ping_host, check_connectivity

import pytest

@pytest.mark.asyncio
async def test_run_ping_command_success():
    output = await run_ping_command("127.0.0.1", count=1)
    assert "1 packets transmitted" in output or "1 received" in output

@pytest.mark.asyncio
async def test_run_ping_command_failure():
    output = await run_ping_command("nonexistent.host.local", count=1)
    assert "Error" in output    


@pytest.mark.asyncio
async def test_run_ping_command_invalid_count():
    output = await run_ping_command("127.0.0.1", count=0)
    assert "Error" in output


@pytest.mark.asyncio
async def test_ping_host():
    output = await ping_host("127.0.0.1", count=1)
    assert "1 packets transmitted" in output or "1 received" in output

@pytest.mark.asyncio
async def test_ping_host_invalid_count():
    output = await ping_host("127.0.0.1", count=0)
    assert "Error" in output

@pytest.mark.asyncio
async def test_check_connectivity():
    output = await check_connectivity("8.8.8.8")
    assert "Internet connection is working!" in output