import asyncio
import platform


async def run_ping_command(host: str, count: int = 4) -> str:
    """Run the ping command and return its output."""
    # Determine the correct ping command based on the OS
    current_os = platform.system().lower()
    
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
        return f"Failed to execute ping command: {str(e)}"

