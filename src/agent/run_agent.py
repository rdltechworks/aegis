
from google.adk.agents import Agent
from .cognitive_core import CAMA
from .memory_systems import SemanticMemory, ProceduralMemory, WorkingMemory, EpisodicMemory

class GuardianAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.semantic_memory = SemanticMemory()
        self.procedural_memory = ProceduralMemory()
        self.working_memory = WorkingMemory()
        self.episodic_memory = EpisodicMemory()
        self.cognitive_core = CAMA(self)

    def run(self):
        while True:
            raw_data = self.procedural_memory.get_new_data()
            if raw_data:
                self.cognitive_core.run_loop(raw_data)

if __name__ == "__main__":
    agent = GuardianAgent(model=ollama_client, name="guardian_agent")
    agent.run()
