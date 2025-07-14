import platform
import psutil

class SystemInfoTool:
    """
    A tool to provide system information, such as OS, CPU, and memory usage.
    """
    def get_os_info(self) -> dict:
        """Returns basic operating system information."""
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
        }

    def get_cpu_usage(self) -> dict:
        """Returns CPU usage statistics."""
        return {
            "percent": psutil.cpu_percent(interval=1),
            "cores": psutil.cpu_count(logical=True),
        }

    def get_memory_info(self) -> dict:
        """Returns memory usage statistics."""
        mem = psutil.virtual_memory()
        return {
            "total_gb": round(mem.total / (1024**3), 2),
            "available_gb": round(mem.available / (1024**3), 2),
            "percent_used": mem.percent,
        }
