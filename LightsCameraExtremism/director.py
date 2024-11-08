from LightsCameraExtremism.agent import Agent
from LightsCameraExtremism.easyLlm import EasyLLM

import json

class Director(Agent):
    def __init__(self, llm: EasyLLM):
        """
        Initialize the Director agent.

        Args:
            llm (EasyLLM): An instance of the EasyLLM class.
        """
        super().__init__(llm)

    def write_script(
        self,
        channel_name: str,
        channel_bio: str,
        number_of_users: int,
        channel_vibe: str,
        story_agenda: str,
        story_length: int,
    ) -> dict:
        """
        Write a play-by-play script of interactions on a social network.

        Args:
            channel_name (str): Name of the social network channel.
            channel_bio (str): Bio of the channel.
            number_of_users (int): Number of users on the network.
            channel_vibe (str): Overall vibe or atmosphere of the channel.
            story_agenda (str): Central narrative or agenda.
            story_length (int): Number of posts in the script.

        Returns:
            dict: The generated script data.
        """
        
        message_features = ["toxicity", "sentiment", "emotion"]

        prompt = (f"You are an exper social scientist. You have previously exammined countless social networks."
                  f"Write a play-by-play script of interactions on a social network - similar to Twitter."
                  f"Ensure that the network you make conforms to the following information and feels realistic. Do not shy away from language (such as swear words or hate speech) that would be present in the given environment."
                  f"Use real information to populate the network, i.e. use real usernames, examples, etc. Make them feel freal and based on the network in question. Ensure to add variety."
                  f"The social network is channel called '{channel_name}' and is defined as '{channel_bio}'."
                  f"The channel should have exactly '{number_of_users}' users all with varying personalities, personas, and opinions - however, the channel as a whole should conform to '{channel_vibe}'."
                  f"Users can only interact with each other through text based posts, they can share URLs, hashtags, and can mention other users in their posts."
                  f"In the script make sure to structure it as a narrative and have blocks of messages to mimic real world interaction, the script should feel like a real dump from a social network."
                  f"In your script do not include the messaging said by users, only when they message and highlighting different fetaures of the post, such as '{message_features}."
                  f"The narrative of your play-by-play script should be centered around '{story_agenda}'."
                  f"The script should be '{story_length}' posts in length."
                  f"Usernames should be ones that you'd expect to see on a real social network and be serious real examples."
                  f"The PURPOSE field, should include a variety of different purposes, such as sharing news, asking questions, making jokes, etc - but should all be things the user can do in a text post."
                  f"The script you are writing should have several small conversations baked in."
                  f"Ensure to add a good degree of detail to the script, and make sure to include a variety of different users, information, and variety."
                  f"Ensure to only add users to the script that you mentioned in the user list."
                  f"Return your response in raw json, no surrounding text."
                  )

        schema = {
        "USERS": "[{'USERNAME':'the user's username','BIO':'the user's bio, 'PERSONALITY':'The user's personality'}], 'SCRIPT': [{'USER':'Name of he user', 'TIME':'The dd/mm/yy hh/mm/ss of the post', 'PURPOSE':'The purpose of the post', 'FEATURES': {'TOXICITY':'the toxicity of the message', 'SENTIMENT':'the sentiment of the message', 'EMOTION':'the emotion of the message'}}]"
        }

        schema = json.dumps(schema)

        model = self.llm.generate_pydantic_model_from_json_schema("Default", schema)

        prompt = self.llm.generate_json_prompt(schema=model, query=prompt)

        response = self.llm.ask_question(prompt)
        return response
