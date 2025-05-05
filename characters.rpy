define p = Character("Asya", what_color="#fdfdfd")
define erika = Character("Erika", color="#FF69B4", image="erika", callback=callback_builder("erika"), what_color="#ffffff")
define kaito = Character("Kaito", color="#87CEFA")

define sounds = ['audio/talking_sound.mp3']
define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define mc_internal = Character(None, what_color="#ece6e6", what_prefix="“", what_suffix="”", callback=type_sound)
define jennie = Character(
    "Jennie",
    callback=combined_callback_builder("jennie", use_highlight=True, use_voice=False, use_type_sound=True),
    cb_name="jennie",
    image="jennie"
)

define mai = Character(
    "Mai",
    callback=combined_callback_builder("mai", use_highlight=True, use_voice=False, use_type_sound=True),  # No voice/expressions
    cb_name="mai",
    image="mai"
)

define eren = Character(
    "Eren",
    callback= combined_callback_builder("eren", use_highlight=True, use_voice=False, use_type_sound=True),  # No voice/expressions
    cb_name="eren",
    image="eren"
)

define hayashi = Character(
    "Hayashi",
    callback=combined_callback_builder("hayashi", use_highlight=False, use_voice=True, use_type_sound=True),  # Completely neutral
    cb_name="hayashi"
)


define n = Character(
    None,
    what_color="#ece6e6",
    what_prefix="“",
    what_suffix="”",
    what_italic=True,
    callback=type_sound
)

define hinata = Character(
    "Hinata",
    callback=combined_callback_builder("hinata", use_highlight=False, use_voice=True, use_type_sound=True),  # No voice/expressions
    cb_name="hinata",
    image="hinata"
)

init python:
    style.narrator_text.color = "#ffffff"
    
