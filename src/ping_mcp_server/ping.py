import asyncio
import platform


async def run_ping_command(host: str, count: int = 4) -> str:
    """Run the ping command and return its output."""
    # Determine the correct ping command based on the OS
    current_os = platform.system().lower()

    if count <= 0:
        return f"Error Invalid Count"
    
    if current_os == "windows":
        cmd = ["ping", "-n", str(count), host]
    else:  # Unix-like systems (Linux, macOS)
        cmd = ["ping", "-c", str(count), host]
    
    try:
        # Run the ping command asynchronously
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        
        if process.returncode == 0:
            return stdout.decode('utf-8')
        else:
            return f"Error: {stderr.decode('utf-8')}"
    except Exception as e:
        return f"Error Failed to execute ping command: {str(e)}"


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
