
import os
from dotenv import load_dotenv
from llm_agent import LlmAgent
from tools.system_info_tool import SystemInfoTool
from tools.calculator_tool import CalculatorTool

# Load environment variables
load_dotenv()

def main():
    """
    Initializes and runs the Digital Guardian agent.
    """
    # System prompt defining the agent's persona and mission
    with open("system_prompt.txt", "r") as f:
        system_prompt = f.read()

    # Initialize the agent
    agent = LlmAgent(
        model=os.getenv("DEFAULT_MODEL", "gemma:2b"),
        system_prompt=system_prompt,
        ollama_host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        max_tokens=int(os.getenv("MAX_TOKENS", 2048)),
        timeout=int(os.getenv("TIMEOUT", 60)),
    )

    # Register tools
    agent.add_tool(SystemInfoTool())
    agent.add_tool(CalculatorTool())

    print("Digital Guardian is active. How can I assist you?")

    # Main conversation loop
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            response = agent.process_input(user_input)
            print(response)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
