# define sounds = ['audio/talking_sound.mp3']

init python:
    side_image_only_mode = False

    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return
    def callback_builder(character_sprite_basename):
        def char_callback(event, **kwargs):
            # Get the current attributes

            global side_image_only_mode

            if side_image_only_mode: return
            
            current_attributes = list(renpy.get_attributes(character_sprite_basename))
            print("Raw attributes:", current_attributes)  # Debugging output

            # Define allowed expressions
            valid_expressions = ["neutral", "happy", "worried", "thinking", "frustrated", "serious", "smile"]
            chosen_emotion = "neutral"  # Default emotion

            # Extract the dominant emotion (ignoring _closed/_opened)
            for attr in current_attributes:
                base_attr = attr.replace("_closed", "").replace("_opened", "").replace("_talk", "")
                if base_attr in valid_expressions:
                    chosen_emotion = base_attr
                    break  # Use the first valid expression
            if event == "show":
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
            
            # Determine talking or resting state
            if event == "show_done":
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_talk"
            elif event == "slow_done":
                renpy.sound.stop()
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_closed"
                renpy.restart_interaction()  # Ensure smooth transition
            elif event == "end":
                renpy.sound.stop()
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_closed"  # Provide a fallback
            else:
                sprite_variant = f"{character_sprite_basename} {chosen_emotion}_opened"

            # Ensure previous attributes are cleared before applying the new one
            renpy.show(character_sprite_basename, what=None)

            # Print debug info for tracking
            print("Filtered emotion:", chosen_emotion)  
            print(f"Final sprite: {sprite_variant}")

            # Show the correct sprite with talking animation
            renpy.show(sprite_variant, layer="master")

        return char_callback


    def combined_callback_builder(char_name, use_highlight=True, use_voice=True, use_type_sound=True):
        def master_callback(event, interact=True, name=None, **kwargs):
            if use_highlight:
                name_callback(event, interact, name or char_name)
            if use_voice:
                callback = callback_builder(char_name)
                callback(event=event, interact=interact, name=name, **kwargs)
            if use_type_sound:
                type_sound(event, interact, name=name, **kwargs)
        return master_callback



# define sounds = ['audio/text_typing.ogg']

##regular taps, medium intervals
# define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

##light taps, smaller intervals
define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init:
    define config.layers = [
        'background',  
        'master',      
        'transient',   
        'screens',     
        'overlay',     
        'mask_layer',  
        'character_layer'
    ]
