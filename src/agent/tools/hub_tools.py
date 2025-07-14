import requests
from typing import List

class HubTool:
    """
    A tool for interacting with the Digital Guardian Hub API.
    This allows the agent to query device status, network logs, and system events.
    """
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def get_all_devices(self) -> List[dict]:
        """Retrieves a list of all connected devices."""
        try:
            response = requests.get(f"{self.base_url}/devices")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to retrieve devices: {e}"

    def get_network_logs(self, limit: int = 100) -> List[dict]:
        """Fetches the latest network traffic logs."""
        try:
            response = requests.get(f"{self.base_url}/network/logs?limit={limit}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to retrieve network logs: {e}"
