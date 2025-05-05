label scene3_2:
    scene bg classroom_day_left with fade
    play music "stress_theme.wav" fadein 1.0 fadeout 0.5 loop

    n """
    The classroom is… still.

    No voices. No footsteps. No idle chatter.

    Just the quiet hum of fluorescent lights.
    """

    mc_internal """
    Maybe I’m early.

    Maybe today’s just... quiet.
    """

    scene bg classroom_board_no_desk with fade

    show hayashi neutral_closed at center with dissolve
    n "Hayashi stands at the board — calm, composed."

    hayashi "Today we scale."

    hayashi "These are frameworks. They enable the construction, training, and deployment of deep learning models."

    mc_internal "The words sound familiar. But I can’t focus."

    scene bg classroom_day_right with fade

    n "I glance around. Empty chairs."

    if flag("helped_eren_search") and not flag("mai_search_success"):
        mc_internal "She left the group chat. No message. No goodbye. Just gone."
        mc_internal "I don’t even know if she’s okay."
    elif flag("helped_mai_sketchbook") and not flag("eren_search_success"):
        mc_internal "Eren hasn’t spoken since that day. Left the chat. Won’t reply."
        mc_internal "I keep checking. Still nothing."
    elif not flag("helped_eren_search") and not flag("helped_mai_sketchbook"):
        mc_internal "Neither of them talks to me anymore."
        mc_internal "Not mad. Just... done."
    else:
        mc_internal "It’s quieter now. Fewer people. Fewer messages."
        mc_internal "Maybe that’s just how things go."

    scene bg classroom_board_no_desk with fade
    show hayashi neutral_closed at center with dissolve
    n "Slide flickers. Hayashi keeps speaking."

    "TensorFlow uses static graphs. PyTorch is dynamic. Abstraction is the goal."

    scene black with fade
    n "I open my notebook. The lines blur."

    mc_internal "I should’ve done more. Or said something. But maybe it was already too late."

    play sound "pen_drop.ogg"
    n "My pen drops. The sound echoes in the empty room."
    scene bg classroom_day_right with dissolve
    pause 0.2
    scene bg classroom_board_no_desk with fade
    show hayashi neutral_closed at center
    python:
        isolation_choices = [
            {
                "prompt": "What do you do?",
                "text": "Keep taking notes",
                "next_label": "isolation_choice_notes",
                "impact": {
                    "stats": {
                        "glitches": 1,
                        "resilience": 1  
                    }
                }
            },
            {
                "prompt": "What do you do?",
                "text": "Look around again",
                "next_label": "isolation_choice_look",
                "impact": {
                    "stats": {
                        "remembering": 1,
                        "curiosity": 1
                    }
                }
            },
            {
                "prompt": "What do you do?",
                "text": "Text them anyway",
                "next_label": "isolation_choice_text",
                "impact": {
                    "stats": {
                        "reflection_score": 1,
                        "empathy": 1
                    }
                }
            }
        ]

        dynamic_choices = build_reflection_choices(isolation_choices)
        return_label = "isolation_post_choice"
    jump handle_dynamic_choice


    return
label system_root_accept:
    mc_internal "I tap it. Instinct, maybe. Or maybe I just need to know if there's still a path back."

    play sound "glitch_rise.ogg"
    n "The screen flashes. And suddenly, I’m in a hallway I don’t recognize. Cold. Stark. Office-like."

    n "Doors with numbers. Some are lit. Some aren’t."

    mc_internal "No labels. Just… choices."

    jump secret_path_intro


label system_root_ignore:
    mc_internal "It’s probably just static. Nothing real."

    return


label system_root_post_choice:
    n "Hayashi turns slightly. A faint smile."

    n "But it doesn’t quite reach his eyes."

    $ time_display = "09:43 AM"
    call show_time() from _call_show_time_12

    mc_internal """
    They’re not gone.

    They just... left.

    And the system? It didn’t crash. It didn’t pause. It just kept going — without them. Without us.
    """

    scene black with fade
    pause 2.0
    return


label isolation_choice_notes:
    mc_internal "The pen glides over the blank page. No ink. Just movement."

    mc_internal "Maybe it’s better to pretend nothing’s wrong."

    return


label isolation_choice_look:
    mc_internal "Desks in perfect rows. Not a bag. Not a pencil out of place."

    mc_internal "Like no one ever planned to show up today."

    return


label isolation_choice_speak:
    n "Is... anyone here?"

    n "Silence. No footsteps. No reaction. Not even from Hayashi."

    mc_internal "Maybe I am early. Maybe I’m just alone."

    return


label isolation_post_choice:
    "System design is about simplification. You keep what works. Let go of what doesn’t."

    if glitches >= 4 or glitch_memory_trigger:
        python:
            system_root_choices = [
                {
                    "prompt": "A message flickers at the corner of your screen:",
                    "text": "OPEN SYSTEM SETTINGS?",
                    "next_label": "system_root_accept",
                    "impact": {
                        "flags": ["saw_system_prompt"]
                    }
                },
                {
                    "prompt": "A message flickers at the corner of your screen:",
                    "text": "Close the prompt",
                    "next_label": "system_root_ignore",
                    "impact": {}
                }
            ]

            dynamic_choices = build_reflection_choices(system_root_choices)
            return_label = "system_root_post_choice"
        jump handle_dynamic_choice

    return

label isolation_choice_text:
    n "I type a message. Just something simple: 'Hey, are you okay?'"
    n "It sends. Then nothing. No reply. Not even a read receipt."

    if flag("helped_eren_search") and not flag("mai_search_success"):
        mc_internal "She saw it. I know she did. But she’s done with me."
    elif flag("helped_mai_sketchbook") and not flag("eren_search_success"):
        mc_internal "Eren used to reply instantly. Now? Nothing. Not even a ghost."
    else:
        mc_internal "Maybe they all moved on. Or maybe… they just don’t want to talk."

    return
