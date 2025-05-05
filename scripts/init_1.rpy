transform sprite_highlight(sprite_name):
    function SpriteFocus(sprite_name)

init python:

    character_map = {
        "eren": [
            "confused1", "frustrated_angry", "shocked1", "shocked2_scared",
            "shocked3", "smile1", "smile2", "smile3", "unhappy"
        ],
        "jennie": [
            "angry", "sad_shocked", "scared", "shocked2", "shocked3_scared",
            "shocked4_scared2", "smile1", "smile2", "unhappy"
        ],
        "mai": [
            "angry1", "angry2", "satisfied", "shocked1", "smile1",
            "smile2", "smile3", "unsatisfied"
        ],
        "hayashi": [
            "happy_closed", "happy_opened", "neutral_closed", "neutral_open",
            "serious_closed", "serious_open", "thinking_closed", "thinking_open",
            "smile_closed", "smile_open"
        ],
        "hinata": [
            "frustrated_closed", "frustrated_opened", "happy_closed", "happy_opened",
            "neutral_closed", "neutral_opened", "smile_closed", "smile_opened",
            "thinking_closed", "thinking_opened", "worried_closed", "worried_opened"
        ]
    }

    for char_name, expressions in character_map.items():
        for expression in expressions:
            image_name = f"{char_name} {expression}"
            interactive_name = f"i_{char_name} {expression}"
            renpy.image(interactive_name, At(image_name, sprite_highlight(char_name)))

    side_image_map = {}

    for char_name, expressions in character_map.items():
        for expression in expressions:
            full_key = f"{char_name} {expression}"
            side_key = f"side {char_name} {expression}"
            side_image_map[full_key] = side_key