
class CAMA:
    def __init__(self, agent):
        self.agent = agent

    def refactor(self, raw_data):
        # Perception & Enrichment
        enriched_data = self.agent.semantic_memory.enrich(raw_data)
        return enriched_data

    def break_down(self, enriched_data):
        # Analysis & Investigation
        analysis_results = self.agent.procedural_memory.analyze(enriched_data)
        return analysis_results

    def compile(self, analysis_results):
        # Conclusion & Learning
        conclusion = self.agent.episodic_memory.learn(analysis_results)
        return conclusion

    def run_loop(self, raw_data):
        enriched_data = self.refactor(raw_data)
        analysis_results = self.break_down(enriched_data)
        conclusion = self.compile(analysis_results)
        self.agent.procedural_memory.output_insight(conclusion)
