from adalflow.core import Generator
from pydantic import BaseModel, computed_field


from config.base_prompts.future_envision import (
    FUTURE_SOCRATIC_PROMPT,
    FUTURE_SCENARIO_DISTILL_PROMPT,
    DEFAULT_INITIAL_SCENARIOS,
)
from dystopic_investment_aigents.agents.base_agents.agent_base import Agent


class FutureScenario(BaseModel):
    name: str
    description: str


class FutureSocraticAgent(Agent):
    @property
    def name(self) -> str:
        return "FutureEnvisionAgent"

    @computed_field()  # type: ignore[misc]
    @property
    def _generator_brain(self) -> Generator:
        return Generator(
            model_client=self.seniority,
            model_kwargs=self.seniority_args,
            template=FUTURE_SOCRATIC_PROMPT,
            prompt_kwargs={
                "personality": f"I am {self.personality.mood.value} and I have a risk tolerance of {self.personality.risk_tolerance*100} %",
            },
        )

    def _default_initial_scenarios(self) -> list[dict[str, str]]:
        return DEFAULT_INITIAL_SCENARIOS

    def generate_initial_scenarios(self) -> list[dict[str, str]]:
        return self._default_initial_scenarios()

    def discuss(self, message: str) -> str:
        return super().discuss(message)


class FutureScenarioDistillerAgent(Agent):
    @property
    def name(self) -> str:
        return "FutureScenarioDistillerAgent"

    @computed_field()  # type: ignore[misc]
    @property
    def _generator_brain(self) -> Generator:
        return Generator(
            model_client=self.seniority,
            model_kwargs=self.seniority_args,
            template=FUTURE_SCENARIO_DISTILL_PROMPT,
            prompt_kwargs={
                "personality": f"I am {self.personality.mood.value} and I have a risk tolerance of {self.personality.risk_tolerance*100} %",
            },
        )

    def discuss(self, message: str) -> str:
        return super().discuss(message)

    def distill(self, message: str) -> str:
        prompt_kwargs = {"input_str": message}
        return self._generator_brain.call(prompt_kwargs=prompt_kwargs)
