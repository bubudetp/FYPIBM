label scene2e5:

    $ time_display =  "04:35 PM"
    call show_time from _call_show_time_1

    scene bg library_day with fade

    n """
    The library’s quieter than usual.

    No Hayashi today. Just a note on the app:
    """

    n """
    “Professor Hayashi is unwell.

    Please review the final sections of Chapter 2 in Library Room 2.

    Next week’s lesson will be essential.”
    """

    if remembering >= 2.0:
        mc_internal "Wait… wasn’t this supposed to be taught *in class*? Hayashi skipped this once before."
    else:
        mc_internal "Doesn’t feel strange… until I realize I can’t remember the last part of Chapter 2 at all."

    mc_internal """
    Strange, but... not alarming.

    He warned us last time. Something important is coming.
    """

    n """
    A few of us gather — not all, but enough to feel like a class.

    Printouts are waiting on the desk. Marked:
    “Chapter 2 – Sections 6 & 7. Final Concepts.”
    """

    mai "Okay, I’ll start reading. Section six… Backpropagation and Gradient Descent."

    jennie """
    Backpropagation is the process of calculating the error from a neural network’s output…

    and distributing it backward to update the weights.
    """

    "Boy A" "So like… the model makes a mistake, and it uses that mistake to figure out what part of it was responsible."

    mai "Exactly. The error gets traced through the network — each connection, each node, contributes differently."

    mc_internal """
    The deeper the layer, the less direct influence it has.

    But the feedback still flows. Like guilt passed along a chain.
    """

    # 🧠 Micro-recap
    n "Backpropagation lets the network *learn from its own failure* — assigning responsibility backward through the layers."

    mai "And gradient descent is how it adjusts those weights, right?"

    jennie "Yep. It uses a partial derivative — basically, a small slice of the error — to decide how much each weight should change."

    jennie """
    Gradient descent is an optimization algorithm.

    It adjusts the network step by step in the direction that reduces the cost function — that is, the error.
    """

    "Girl C (murmuring, almost to herself)"
    "Maybe learning isn’t about truth. Just... trying again. Softer."

    python:
        reflection_choices_jennie = [
            {
                "prompt": "How do you respond?",
                "text": "It’s painful. But it’s growth.",
                "next_label": "jennie_response_growth",
                "impact": {
                    "relationship": ("jennie", 1.0)
                }
            },
            {
                "prompt": "How do you respond?",
                "text": "Trying over and over doesn’t mean it’s working.",
                "next_label": "jennie_response_trapped",
                "impact": {
                    "relationship": ("jennie", -1.0)
                }
            },
            {
                "prompt": "How do you respond?",
                "text": "You okay?",
                "next_label": "jennie_response_concern",
                "impact": {
                    "relationship": ("jennie", 0.5)
                }
            }
        ]
        dynamic_choices = build_reflection_choices(reflection_choices_jennie)
        return_label = "jennie_response_post"
    jump handle_dynamic_choice


    "Boy B" "So it’s like hiking downhill blindfolded. You feel around for where the ground slopes down, and you step in that direction."

    mai "Unless you fall in a valley and get stuck there forever."

    play sound "light_laughter.ogg"
    pause 1.0


    mc_internal """
    The bottom of the curve is where the system is “best.”

    Where its guesses are closest to the truth.

    But it never knows if it reached the bottom.

    It just… trusts the slope.
    """

    n "Gradient descent doesn’t find the perfect answer — just *a better one than before*."

    n "Cost = ½ Σ (y - ŷ)²"

    mai "So this is how the error is measured — sum of the differences between expected and predicted values. Squared, so mistakes don’t cancel each other out."

    mc_internal """
    This isn’t just math.

    It’s philosophy.

    Failure becomes feedback.

    Error becomes direction.
    """
    

    
    call scene2e5_part2 from _call_scene2e5_part2
    return


label scene2e5_part2:

    mai "Ohhh, I love this one. Here’s the story:"

    """
    A statistician shoots ten arrows at a target.

    Every arrow misses — but they average out to hit the bullseye.

    He shrugs and says: ‘We got it!’
    """

    "Boy B" "That’s stats. Precision without meaning."

    jennie "And ML is the opposite. It tolerates being a little wrong, if it means being useful."

    mai """
    Machine learning generalizes.

    It doesn’t care if one prediction is off — as long as the overall performance is good.
    """

    n "Generalization is the goal — not perfection on every point, but consistency across patterns."

    python:
        system_identity_choices = [
            {
                "prompt": "What kind of system are you?",
                "text": "I want to hit the target, no matter what.",
                "next_label": "system_choice_precision",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "What kind of system are you?",
                "text": "I’d rather miss a few and still help someone.",
                "next_label": "system_choice_empathy",
                "impact": {
                    "stats": {
                        "reflection_score": 1.0
                    }
                }
            },
            {
                "prompt": "What kind of system are you?",
                "text": "I’d like to understand why I keep missing.",
                "next_label": "system_choice_selfawareness",
                "impact": {
                    "stats": {
                        "reflection_score": 1.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(system_identity_choices)
        return_label = "system_choice_post"
    jump handle_dynamic_choice

    # sdsd
    call walk_response_event from _call_walk_response_event

    scene bg library_sunset with dissolve
    pause 1.0

    n """
    The sun shifts. The laughter fades into quiet page-turning.

    Someone adds “Chapter 2 – Done” to the whiteboard.
    """

    mc_internal """
    We learned everything.

    But I’m still thinking about Hayashi.

    Why skip this part?

    Why make us finish it?
    """

    mc_internal """
    Maybe he wanted to see if we could learn without him.

    Or maybe he wanted to know which of us would keep adjusting… even when the guidance stopped.
    """

    $ time_display = "05:17 PM"
    
    call show_time from _call_show_time_2

    jennie "Whatever’s coming next… He wants us ready."
    
    call trust_event from _call_trust_event

    return


label walk_response_event:
    python:
        if walk_response == "training" or walk_response == "silent":
        # "Girl C (quietly, later)"
            renpy.say(n, "Thanks for not laughing at me that day. When I said maybe we were just data.")

            renpy.say(mc_internal, "She remembered. Even if the system didn’t.")
            rel_girl_c += 1.0

label trust_event:
    python:
        if rel_girl_c >= 3.0:
            girl_c_trusts_you = True
        else:
            girl_c_trusts_you = False
label jennie_response_growth:
    n "Learning hurts. But the cost means something."
    return

label jennie_response_trapped:
    n "Some loops just trap you."
    return

label jennie_response_concern:
    n "You sound like you're talking about more than models."
    return

label jennie_response_post:
    return
label system_choice_precision:
    mc_internal "Precision matters. I want to get it right."
    return

label system_choice_empathy:
    mc_internal "Maybe usefulness matters more than perfection."
    return

label system_choice_selfawareness:
    mc_internal "The system can adjust — but only if it sees the pattern."
    return

label system_choice_post:
    return
