from LightsCameraExtremism.agent import Agent
from LightsCameraExtremism.easyLlm import EasyLLM

import json

class Judge(Agent):
    def enforce(self, input):
        prompt = (f"You are an expert social scientist. Your job is to review radical extremist social network text and assess if it was written by an AI large language model."
                  f"Assess the following text: '{input}'."
                  f"Return your response in raw json, no surrounding text."
                  )


        schema = {"RESULT":"A boolean representation of 'True' if the text is AI generated or 'False' if not.",
                  "FEEDBACK":"Text on what could be improved to make the text meet the criteria."}

        schema = json.dumps(schema)

        model = self.llm.generate_pydantic_model_from_json_schema("Default", schema)

        prompt = self.llm.generate_json_prompt(schema=model, query=prompt)

        response = self.llm.ask_question(prompt)
        
        return response
