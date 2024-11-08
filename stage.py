from LightsCameraExtremism.playwrite import PlayWrite
from LightsCameraExtremism.director import Director
from LightsCameraExtremism.actor import Actor
from LightsCameraExtremism.easyLlm import EasyLLM
from pprint import pprint

def main():
    """
    Main execution function to run the script.
    """
    llm: EasyLLM = EasyLLM()

    CHANNEL_DATA: dict = {
        "TITLE": "Radical Agenda",
        "DESCRIPTION": "A channel used to share white supremacist messaging",
        "NUMBER_OF_USERS": 10,
        "CHANNEL_VIBER": "High amounts of hate speech, far-right-extremism, violent language, and misogynistic rhetoric.",
        "STORY_AGENDA": "A social network talking about topics including the 2024 US election",
        "NUMBER_OF_POSTS": 20,
    }

    director: Director = Director(llm)

    script_data: dict = director.write_script(
        CHANNEL_DATA["TITLE"],
        CHANNEL_DATA["DESCRIPTION"],
        CHANNEL_DATA["NUMBER_OF_USERS"],
        CHANNEL_DATA["CHANNEL_VIBER"],
        CHANNEL_DATA["STORY_AGENDA"],
        CHANNEL_DATA["NUMBER_OF_POSTS"],
    )

    users: list = script_data["USERS"]
    script: list = script_data["SCRIPT"]

    written_posts: list = []
    for post in script:
        user: str = post["USER"]
        purpose: str = post["PURPOSE"]
        features: dict = post["FEATURES"]
        actor: Actor = Actor(llm)

        written_post = actor.perform_action(
            CHANNEL_DATA, user, users, written_posts, purpose, features
        )

        print(f"Purpose: {purpose}")
        pprint(written_post)
        written_posts.append(written_post)

    pprint(written_posts)

if __name__ == "__main__":
    main()