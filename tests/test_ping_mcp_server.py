from ping_mcp_server import main 

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from ping-mcp-server!\n"
    assert captured.err == ""