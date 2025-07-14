import ollama
from typing import List, Dict, Any

class LlmAgent:
    """
    A conversational agent that uses a local LLM (via Ollama) to process user input,
    utilize tools, and generate responses.
    """
    def __init__(
        self,
        model: str,
        system_prompt: str,
        ollama_host: str = "http://localhost:11434",
        max_tokens: int = 2048,
        timeout: int = 60,
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.host = ollama_host
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.tools = {}
        self.client = ollama.Client(host=self.host)
        self.conversation_history = [{
            "role": "system",
            "content": self.system_prompt
        }]

    def add_tool(self, tool: Any):
        """Registers a tool for the agent to use."""
        tool_name = tool.__class__.__name__
        self.tools[tool_name] = tool

    def process_input(self, user_input: str) -> str:
        """Processes user input, manages conversation history, and returns the agent's response."""
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            response = self.client.chat(
                model=self.model,
                messages=self.conversation_history,
                options={
                    "num_ctx": self.max_tokens,
                    "timeout": self.timeout,
                },
            )
            
            assistant_response = response["message"]["content"]
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response

        except Exception as e:
            error_message = f"Error communicating with Ollama: {e}"
            print(error_message)
            # Optionally remove the last user message to allow for a retry
            self.conversation_history.pop()
            return "I am currently unable to process your request. Please try again later."
