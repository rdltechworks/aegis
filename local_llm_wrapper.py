import requests
import json
from google.adk.models import LlmResponse
from google.genai import types

class LocalLlmWrapper:
    """A wrapper for interacting with a local LLM server (e.g., Ollama)."""

    def __init__(self, model: str, api_base: str = "http://localhost:11434/api"):
        """Initialize the wrapper with the model name and API base URL."""
        self.model = model
        self.api_base = api_base

    def generate_content(self, contents: list[types.Content], **kwargs) -> LlmResponse:
        """Generate content using the local LLM."""
        prompt = "\n".join([part.text for part in contents[-1].parts])
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(f"{self.api_base}/generate", json=payload)
            response.raise_for_status()
            response_json = response.json()
            generated_text = response_json.get("response", "")
            
            return LlmResponse(
                content=types.Content(parts=[types.Part(text=generated_text)])
            )
        except requests.exceptions.RequestException as e:
            error_message = f"Error connecting to local LLM: {e}"
            print(error_message)
            return LlmResponse(
                content=types.Content(parts=[types.Part(text=error_message)])
            )

