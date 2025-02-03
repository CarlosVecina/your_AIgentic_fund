from dystopic_investment_aigents.agents.base_agents.agent_base import Agent


class SocraticFutureAgent(Agent):
    @property
    def name(self) -> str:
        return "SocraticFutureAgent"

    def discuss(self, message: str) -> str:
        return super().discuss(message)
