from abc import ABC
from LightsCameraExtremism.easyLlm import EasyLLM

class Agent(ABC):
    """
    Abstract base class for agents.
    """

    def __init__(self, llm: EasyLLM):
        """
        Initialize the Agent.

        Args:
            llm (EasyLLM): An instance of the EasyLLM class.
        """
        self.llm = llm