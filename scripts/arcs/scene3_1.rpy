label scene3_1:

    scene bg classroom_day_left with fade
    n "09:00 AM"

    n """
    The air feels heavier than it did last week.

    Not tense. Not loud. Just... expectant.

    Like the room is holding its breath.
    """

    mc_internal """
    It’s Monday. Again.

    Same seat. Same view.

    But something’s wrong.

    I don’t know what.

    Just... wrong.
    """

    scene bg classroom_board_no_desk with dissolve
    # hayashi enters
    show hayashi at center with dissolve

    hayashi "Today, we build systems that make decisions."

    n "DECISION TREE CLASSIFIERS"

    hayashi "You’re at a traffic light. It’s red. You're late. Do you wait, or do you go?"

    mc_internal "Simple choice. But with consequences."

    hayashi """
    That’s the idea behind a decision tree.

    Each node asks a question.

    Each answer leads you to a new question.

    Eventually, you arrive at a decision.
    """

    # 🧠 Micro-recap
    n "A decision tree breaks problems down into binary choices — branching with every condition."

    n """
    Nemra travels to work. She has five features to consider:

    1. Weather  
    2. Time  
    3. Distance  
    4. Traffic  
    5. Public transport reliability
    """

    "Girl A" "Can I just tell Nemra to call in sick?"

    play sound "light_laughter.ogg"
    pause 1.0

    hayashi "She may, but our model cannot."

    hayashi "To build a tree, we ask: Which feature splits the data best? That’s where entropy comes in."

    # 🧠 Micro-recap
    n "Entropy measures how mixed or uncertain your data is after a split."

    hayashi """
    The more mixed your data after a split — the higher the entropy.

    Our goal is to find the feature that produces the lowest entropy — the cleanest split.
    """

    hayashi "In Nemra’s case, time of day gave the most consistent decision. Low entropy. High information gain."

    mc_internal """
    The tree learns where to branch.

    Where to split.

    What to discard.

    How many times have I done the same?
    """

    python:
        nemra_split_choices = [
            {
                "prompt": "You’re training a model to predict if Nemra takes the bus or not.\nWhich feature most likely gives a clean split?",
                "text": "Time of day",
                "next_label": "nemra_choice_time",
                "impact": {
                    "branches": {
                        "reflection_score": 1,
                        "remembering": 1
                    }
                }
            },
            {
                "prompt": "You’re training a model to predict if Nemra takes the bus or not.\nWhich feature most likely gives a clean split?",
                "text": "Distance to work",
                "next_label": "nemra_choice_distance",
                "impact": {
                    "branches": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "You’re training a model to predict if Nemra takes the bus or not.\nWhich feature most likely gives a clean split?",
                "text": "Weather",
                "next_label": "nemra_choice_weather",
                "impact": {
                    "branches": {
                        "glitches": 1
                    }
                }
            },
            {
                "prompt": "You’re training a model to predict if Nemra takes the bus or not.\nWhich feature most likely gives a clean split?",
                "text": "Reliability score of buses",
                "next_label": "nemra_choice_reliability",
                "impact": {
                    "branches": {
                        "reflection_score": 1,
                        "glitches": -0.5
                    },
                    "flags": ["bonus_inference"]
                }
            },
        ]

        dynamic_choices = build_reflection_choices(nemra_split_choices)
        return_label = "nemra_split_post_choice"
    jump handle_dynamic_choice
    return

label nemra_choice_time:
    mc_internal "Time's reliable. Predictable."
    return

label nemra_choice_distance:
    mc_internal "Maybe... but it's not always the deciding factor."
    return

label nemra_choice_weather:
    mc_internal "Too inconsistent. Too noisy."
    return

label nemra_choice_reliability:
    mc_internal "Sometimes reliability matters more than distance."
    return

label nemra_split_post_choice:
    if correct_choice == "bonus":
        $ reflection_score += 1
    elif correct_choice == True:
        $ reflection_score += 0.5

    n "The cleaner the split, the more confident the decision. That’s how trees grow — not just with data, but with certainty."

    eren "So what happens if two features give similar splits?"

    hayashi """
    You compare their information gain.

    But if the gain is equal, the model can choose arbitrarily — or based on heuristics.
    """

    pause 0.5

    mc_internal "It’s subtle. Like the projector screen hiccupped."


    n "Hey, where’s—"

    "Girl C" "Where’s who?"

    if girl_c_trusts_you:
        "Girl C (frowning, softer this time)"  
        "Wait… you mean Boy A?"

        mc_internal "She... she remembers?"

        "Girl C" "I don’t know why I said I didn’t. I saw him yesterday. I know I did."

        $ remembering += 1
        $ rel_girl_c += 1
    else:
        "Girl C" "Where’s who?"

        mc_internal """
        No one reacts. No one asks.

        It’s like he was never there.

        But I remember his voice.

        Just now. Asking about feature choice.
        """


    n "Sometimes the model picks. Sometimes it forgets."

    hayashi "Pruning prevents overfitting. We remove unnecessary branches — simplify the model."

    hayashi "You want decisions that generalize — not memorize. Precision at the cost of usefulness is wasted computation."

    mc_internal """
    But what if the pruning removes too much?

    What if what we cut… matters?

    What if that wasn’t noise?
    """

    python:
        prune_tree_choices = [
            {
                "prompt": "If you were pruning your own tree…",
                "text": "Bad memories.",
                "next_label": "prune_choice_memories",
                "impact": {
                    "branches": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "If you were pruning your own tree…",
                "text": "Doubt.",
                "next_label": "prune_choice_doubt",
                "impact": {
                    "branches": {
                        "reflection_score": 1.0
                    }
                }
            },
            {
                "prompt": "If you were pruning your own tree…",
                "text": "Connections I didn’t trust.",
                "next_label": "prune_choice_connections",
                "impact": {
                    "branches": {
                        "reflection_score": 1.5
                    }
                }
            }
        ]

        dynamic_choices = build_reflection_choices(prune_tree_choices)
        return_label = "prune_tree_post_choice"
    jump handle_dynamic_choice
    return

label prune_choice_memories:
    mc_internal "Some branches shouldn’t be revisited."
    jump prune_tree_post_choice
    return

label prune_choice_doubt:
    mc_internal "Overfitting on fear. That’s my real loss function."
    jump prune_tree_post_choice

    return

label prune_choice_connections:
    mc_internal "Sometimes I think I misclassified people too early."
    jump prune_tree_post_choice

    return

label prune_tree_post_choice:
    
    $ time_display = "09:43 AM"
    call show_time from _call_show_time_9
    
    if rel_girl_c >= 3.0:
        "Girl C (quietly, before leaving the room)"  
        "If the system’s pruning us… then remembering might be rebellion."

        mc_internal "She doesn’t wait for a reply. Just walks out."

        $ glitches += 1

    n "Only I see it. Then... it's gone."

    pause 2.0
    return
