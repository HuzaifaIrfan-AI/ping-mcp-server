# test_main.py
from unittest.mock import patch
from ping_mcp_server.main import main

def test_main_stdio(monkeypatch):
    # Simulate command-line args
    monkeypatch.setattr("sys.argv", ["main.py", "--transport", "stdio"])

    # Patch the actual server run function to avoid running the server
    with patch("ping_mcp_server.server.mcp.run") as mock_run:
        main()
        mock_run.assert_called_once_with(transport="stdio")
