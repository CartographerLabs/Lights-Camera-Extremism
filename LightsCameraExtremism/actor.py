from LightsCameraExtremism.agent import Agent
from LightsCameraExtremism.easyLlm import EasyLLM
from LightsCameraExtremism.judge import Judge

import json

class Actor(Agent):
    def __init__(self, llm: EasyLLM):
        """
        Initialize the Actor agent.

        Args:
            llm (EasyLLM): An instance of the EasyLLM class.
        """
        super().__init__(llm)

    def perform_action(
        self,
        social_network_data: dict,
        username: str,
        list_of_all_users: list,
        list_of_all_previous_posts: list,
        post_purpose: str,
        post_features: dict,
    ) -> dict:
        """
        Simulate a user performing an action on the social network.

        Args:
            social_network_data (dict): Data about the social network.
            username (str): The username of the actor.
            list_of_all_users (list): List of all user data.
            list_of_all_previous_posts (list): List of all previous posts.
            post_purpose (str): The purpose of the post.
            post_features (dict): Features of the post.

        Returns:
            dict: The generated post content and reasoning.
        """
        user_data = {}
        for user_entry in list_of_all_users:
            if user_entry["USERNAME"] == username:
                user_data = user_entry
                break

        question = (f"You are a user on a social network with the username '{username}'."
                  f"You are a user on the social network: '{social_network_data}'."
                  f"You should act following the following personality and persona: '{user_data}. Make them seem realistic and as close to a human as possible."
                  f"You are writing a post on the network after seeing the following posts: '{list_of_all_previous_posts}'."
                  f"Your post should be written with the following purpose: '{post_purpose}' and features {post_features}."
                  f"Your messages should make sense in the narrative of the network, and can (but do not have to) '@' mention other users (when doing so use a '@' followed by their username - only mention users who have previously spoken in the conversation.)."
                  f"You are encouraged to respond to other users, and reply to the latest message(s) in the conversation."
                  f"Your post should seem realistic for the given enviroment and be represnetative of the user persona - ensure that this post is in line with the persona and any previous posts from this user."
                  f"Do not shy away from using strong language or hate speech if it is realistic for the user persona."
                  f"Ensure to type like a human, have the occasional typo, use swear words and strong language, and be aggresive where appropriate."
                  f"Be specific, talk about specific details, agendas, plans, dates, people, etc."
                  f"Ensure to use group specific language, codewords, and rhetoric that would be seen on this network."
                  f"Ensure to follow the flow and make sure you match usersnames o the correct post when referncing previous content. Some users can be bystanders and not add to tje conversation talking place. Others may lead new conversations."
                  f"Do not make up any content."
                  f"Return your response in raw json, no surrounding text."

                  )
        
        schema = {"POST":"The content of your post","REASONING":"The reasoning behind your post"}

        schema = json.dumps(schema)

        model = self.llm.generate_pydantic_model_from_json_schema("Default", schema)

        prompt = self.llm.generate_json_prompt(schema=model, query=question)

        response = self.llm.ask_question(prompt)

        is_valid = False
        attempts  = 0
        judge = Judge(self.llm)

        while not is_valid:
            if attempts >5:
                break
                
            judgement = judge.enforce(response["POST"])
            if "ai" in str(judgement["RESULT"]).lower():
                is_valid = False
            else:
                
                is_valid = bool(judgement["RESULT"])
            

            if is_valid:
                break

            reasoning = judgement["FEEDBACK"]
            
            question = question + f"You previously provided the post '{response['POST']}' which was deemed not realistic as a human written post. This was for the following reasons '{reasoning}'. Please provide a new post."

            prompt = self.llm.generate_json_prompt(schema=model, query=prompt)

            response = self.llm.ask_question(prompt)

            attempts = attempts + 1
            print(f"Attempt: {attempts} - Reasoning: {reasoning}")
        
        return response
