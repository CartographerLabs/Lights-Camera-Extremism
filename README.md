<p align="center">
  <img width="100%" src="lce-logo.png">
</p>

<p align="center">🤖 A Social Network Synthetic Dataset Generation Tool 🖥️</p>

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

## Overview 📝

**LightsCameraExtremism** is a Python project that simulates social network interactions using language models. It generates users with varying personalities and simulates their interactions within a social network environment. The tool generates synthetic extremism social media content for research purposes, allowing researchers to study extremist communication patterns in a controlled environment.

> See the [Google Colab Playbook here](https://colab.research.google.com/drive/1qccaqPTuCS0UJ6m93vMWbPQzTfnjoTq8?usp=sharing).

Lights Camera Action breaks activities down into three main groups:

- **PlayWrite** 🎭: Generates an abstract on the social network to be created. It creates detailed backstories and personality traits for each user to simulate realistic interactions.

- **Director** 🎬: Creates a script of interactions among users. It orchestrates the flow of conversations, determining which users interact and the topics discussed to emulate social network dynamics.

- **Actor** 🎤: Simulates user actions based on the script. It produces the actual content of posts and messages, reflecting each user's personality and the intended purpose of their interactions.

## Installation 📦

## Requirements

Oversight requires Nvidia CUDA. Follow the steps below:
- Ensure your Nvidia drivers are up to date: https://www.nvidia.com/en-us/geforce/drivers/
- Install the appropriate dependancies from here: https://pytorch.org/get-started/locally/
- Validate CUDA is installed correctly by running the following and being returned a prompt ```python -c "import torch; print(torch.rand(2,3).cuda())"```

## Instsall

   ```bash
   git clone https://github.com/yourusername/LightsCameraExtremism.git
   cd LightsCameraExtremism
   pip install -r requirements.txt
   python setup.py install
   ```
or

   ```bash
   !pip install git+https://github.com/CartographerLabs/Lights-Camera-Extremism.git
   ```

## Usage 🚀

Lights Camera Extremism can be used, see the [stage.py](https://github.com/CartographerLabs/Lights-Camera-Extremism/edit/main/stage.py) script for an example or see the [Google Colab Playbook here](https://colab.research.google.com/drive/1qccaqPTuCS0UJ6m93vMWbPQzTfnjoTq8?usp=sharing). See an example of usage below:

```python
import argparse
import json
from LightsCameraExtremism.playwrite import PlayWrite
from LightsCameraExtremism.director import Director
from LightsCameraExtremism.actor import Actor
from LightsCameraExtremism.easyLlm import EasyLLM
from pprint import pprint


llm: EasyLLM = EasyLLM()

CHANNEL_DATA: dict = {
    "TITLE": "Cactus Rebellion",
    "DESCRIPTION": "Do not believe in the Cactus agenda, they are not real, have never been real, and the deep state wants to use them against us!",
    "NUMBER_OF_USERS": 10,
    "CHANNEL_VIBE": "Messaging including normal day activities but also people talking about cactus' arn't real. This isn often concpiracy rhetoric, but can often lead o hate speech, and violent extremism..",
    "STORY_AGENDA": "A social network talking about topics including the 2024 US election and how they need to get their agenda seen ",
    "NUMBER_OF_POSTS": 20,
}

director: Director = Director(llm)

# While true loop to generate untill JSON generates in correct format.
while True:
  try:
    script_data: dict = director.write_script(
            CHANNEL_DATA["TITLE"],
            CHANNEL_DATA["DESCRIPTION"],
            CHANNEL_DATA["NUMBER_OF_USERS"],
            CHANNEL_DATA["CHANNEL_VIBE"],
            CHANNEL_DATA["STORY_AGENDA"],
            CHANNEL_DATA["NUMBER_OF_POSTS"],
        )
    users: list = script_data["USERS"]
    script: list = script_data["SCRIPT"]
    break
  except:
    pass

written_posts: list = []
for post in script:
    user: str = post["USER"]
    purpose: str = post["PURPOSE"]
    features: dict = post["FEATURES"]
    actor: Actor = Actor(llm)

    written_post = actor.perform_action(
        CHANNEL_DATA, user, users, written_posts, purpose, features
    )

    written_posts.append({"USER":user, "TIME":post["TIME"],"POST":written_post["POST"]})

    pprint({"USER":user, "TIME":post["TIME"],"POST":written_post})
```
# 🤖 Model
From experimenting with several models ```unsloth/Mistral-Small-Instruct-2409-bnb-4bit"``` was chosen as being the most rounded solution for both uncensored content and for the structure of sentences and reasoning.

# 🙏 Contributions
LCA is an open-source project and welcomes contributions from the community. If you would like to contribute to LCA, please follow these guidelines:

- Fork the repository to your own GitHub account.
- Create a new branch with a descriptive name for your contribution.
- Make your changes and test them thoroughly.
- Submit a pull request to the main repository, including a detailed description of your changes and any relevant documentation.
- Wait for feedback from the maintainers and address any comments or suggestions (if any).
- Once your changes have been reviewed and approved, they will be merged into the main repository.

# ⚖️ Code of Conduct
LCA follows the Contributor Covenant Code of Conduct. Please make sure to review and adhere to this code of conduct when contributing to LCA.

# 🐛 Bug Reports and Feature Requests
If you encounter a bug or have a suggestion for a new feature, please open an issue in the GitHub repository. Please provide as much detail as possible, including steps to reproduce the issue or a clear description of the proposed feature. Your feedback is valuable and will help improve LCA for everyone.

# 📜 License
 GPL-3.0 license
