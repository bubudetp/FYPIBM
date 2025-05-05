init -10 python:
    class Character_Bo:
        def __init__(self, name, traits=None, relationships=None, objective=""):
            self.name = name
            self.traits = traits or {}  # Dictionary of trait_name: value (0-10)
            self.relationships = relationships or {}  # Dictionary of character_name: value (0-10)
            self.objective = objective
            self.image = "jennie neutral"
            
    # Create the character profiles
    characters = {
        "Jennie": Character_Bo(
            name="Jennie",
            traits={
                "Honest": 7,
                "Charitable": 6,
                "Funny": 4,
                "Brave": 5,
                "Romantic": 3,
                "Curious": 4
            },
            relationships={
                "Ashley": 5,
                "Chris": 6,
                "Emily": 4,
                "Jess": 6,
                "Josh": 7,
                "Matt": 5,
                "Mike": 6
            },
            objective="Follow Josh to get the boiler working"
        ),
        # Add more characters here
        "Josh": Character_Bo(
            name="Josh",
            traits={
                "Honest": 4,
                "Charitable": 5,
                "Funny": 8,
                "Brave": 6,
                "Romantic": 3,
                "Curious": 7
            },
            relationships={
                "Ashley": 6,
                "Chris": 8,
                "Emily": 5,
                "Jess": 6,
                "Matt": 5,
                "Mike": 7
            },
            objective="Set up the party at the lodge"
        ),
    }