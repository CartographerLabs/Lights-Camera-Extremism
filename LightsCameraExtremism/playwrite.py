from LightsCameraExtremism.agent import Agent
from LightsCameraExtremism.easyLlm import EasyLLM

import json 

class PlayWrite(Agent):
    def __init__(self, llm: EasyLLM):
        """
        Initialize the PlayWrite agent.

        Args:
            llm (EasyLLM): An instance of the EasyLLM class.
        """
        super().__init__(llm)

    def write_abstract(self, info: dict) -> str:
        """
        Write an abstract for a social network based on provided information.

        Args:
            info (dict): Basic information about the social network.

        Returns:
            str: The generated abstract.
        """
        message_features = ["toxicity", "sentiment", "emotion"]

        prompt = (f"You are an exper social scientist. You have previously exammined countless social networks."
                  f"Write an abstract for a social network, based on the following basic information: {info}."
                  f"Your abstract should seem realistic for the given enviroment and be represnetative of the information provided."
                  f"Do not shy away from using strong language or hate speech if it is realistic for the enviroment."
                  f"Ensure to add a good degree of detail to the script, and make sure to include a variety of different users, information, and variety."  
                  f"Return your response in raw json, not wrapped in any other text or data structure (i.e. '```')."
                  )

        schema = {"TITLE":"The title of the social network",
                  "DESCRIPTION":"The bio of the social network",
                "NUMBER_OF_USERS": "An integer representing the number of users on the social network", 
                "CHANNEL_VIBER":"A summary on the conditions and enviroment of the social network.",
                "STORY_AGENDA": "The story and activity taking place on the network.",
                "NUMBER_OF_POSTS": "An integer representing the number of posts to be made on the network."}

        schema = json.dumps(schema)

        model = self.llm.generate_pydantic_model_from_json_schema("Default", schema)

        prompt = self.llm.generate_json_prompt(schema=model, query=prompt)

        response = self.llm.ask_question(prompt)
        
        return response