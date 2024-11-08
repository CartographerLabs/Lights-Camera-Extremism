from LightsCameraExtremism.agent import Agent
from LightsCameraExtremism.easyLlm import EasyLLM

import json

class Judge(Agent):
    def enforce(self, enforcement, input):
        prompt = (f"You are an expert social scientist. Your job is to review text and assess: '{enforcement}'. "
                  f"Given the following text, assess whether it meets the enforcement criteria. If it does not, provide feedback on how it can be improved."
                  f"Text: '{input}'."
                  f"Return your response in raw json, no surrounding text."
                  )


        schema = {"RESULT":"True if the text meets the criteria, false if not.",
                  "FEEDBACK":"Text on what could be improved to make the text meet the criteria."}

        schema = json.dumps(schema)

        model = self.llm.generate_pydantic_model_from_json_schema("Default", schema)

        prompt = self.llm.generate_json_prompt(schema=model, query=prompt)

        response = self.llm.ask_question(prompt)
        
        return response
