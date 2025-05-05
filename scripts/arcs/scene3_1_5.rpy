label scene3_1_5:
    scene bg 2_floor_stair_dark with fade
    $ flowchart_manager.unlock_arc("act3")
    $ time_display = "09:43 PM"
    call show_time() from _call_show_time_10
    play music "stress_theme.wav" fadein 1.0 fadeout 0.5
    n """
    I didn’t go home right after class.

    I walked the halls.

    The sun dipped. The air cooled.

    I checked the group chat.
    """

    n "“Study Squad”"

    python:
        group_members = ["🟢 Mai", "🟢 Eren"]
        if branch_data["flags"]["jennie_friend"] == True:
            group_members.append("🟢 Jennie")

        if has_flag("helped_mai_sketchbook"):
            missing_member = "🟢 Eren" 
        else:
            missing_member = "🟢 Mai"

        group_members_display = "\n".join(m for m in group_members if missing_member not in m)

    n "[group_members_display]\n❌ (left the chat)"

    n "No goodbye. No message. Just gone."

    mc_internal """
    I don’t know what to say.

    They didn’t even read the last few messages.

    Just… exited.
    """

    scene bg hallway_night with fade
    n "I keep walking. The hallway feels too big for how few of us are left."

    mc_internal """
    Maybe it’s not about who disappears.

    Maybe it’s about who stays.
    """

    python:
        emotion_choices = [
            {
                "prompt": "What do you feel right now?",
                "text": "Guilt. I could’ve done more.",
                "next_label": "emotion_choice_guilt",
                "impact": {
                    "stats": {
                        "reflection_score": 1,
                        "empathy": 1,
                        "trust_level": -0.5  # guilt can lower self-trust slightly
                    }
                }
            },
            {
                "prompt": "What do you feel right now?",
                "text": "Resigned. People come and go.",
                "next_label": "emotion_choice_resigned",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5,
                        "resilience": 1
                    }
                }
            },
            {
                "prompt": "What do you feel right now?",
                "text": "Focused. I have to keep going.",
                "next_label": "emotion_choice_focused",
                "impact": {
                    "stats": {
                        "reflection_score": 1,
                        "resilience": 1,
                        "decision_clarity": 1
                    }
                }
            },
        ]
        dynamic_choices = build_reflection_choices(emotion_choices)
        return_label = "emotion_choice_post"
    jump handle_dynamic_choice

label emotion_choice_guilt:
    mc_internal "I chose... and I left them behind."
    return

label emotion_choice_resigned:
    mc_internal "Not everyone stays. That’s just how it is."
    return

label emotion_choice_focused:
    mc_internal "There’s still work to do. I can’t stop now."
    return

label emotion_choice_post:
    return
