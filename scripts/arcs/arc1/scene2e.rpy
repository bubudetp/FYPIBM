label scene2e_transition:
    scene bg home_night with fade

    $ chosen_character = get_text_var("relationship_key")  # "mai" or "eren"
    $ other_character = "eren" if chosen_character == "mai" else "mai"

    if chosen_character == "mai":
        if has_flag("mai_search_success"):
            play music "search_success.wav" fadein 0.5 fadeout 0.5
            show i_mai shocked1 at character_center_zoom_mai with dissolve
            "Mai stands frozen under the streetlight, her recovered sketchbook clutched so tightly her knuckles whiten."

            show i_mai smile1 at character_center_zoom_mai with dissolve
            mai "You didn't have to... why would you..." 
            "Her voice cracks as she struggles between gratitude and something sharper."

            python:
                mai_gratitude_choices = [
                    {
                        "prompt": "Why did you help her?",
                        "text": "Because it mattered to you",
                        "next_label": "gratitude_mai_reason",
                        "impact": {
                            "stats": {
                                "trust_level": 2,
                                "empathy": 2,
                                "remembering": 1,
                                "resilience": 1,
                                "reflection_score": 1
                            }
                        }
                    },
                    {
                        "prompt": "Why did you help her?",
                        "text": "Don't overthink it",
                        "next_label": "gratitude_mai_deflect",
                        "impact": {
                            "stats": {
                                "trust_level": 1,
                                "reflection_score": 2,
                                "comprehension": 1
                            }
                        }
                    }
                ]
                dynamic_choices = build_reflection_choices(mai_gratitude_choices)
                return_label = "gratitude_mai_post"
            jump handle_dynamic_choice

        else:
            play music "sad0.mp3" fadein 0.5 fadeout 0.5
            show i_mai angry2 at character_center_zoom_mai with dissolve
            "Mai sits on the curb, empty-handed. The disappointment in her eyes says everything."
            mai "We tried. I know we did."

            python:
                mai_fail_choices = [
                    {
                        "prompt": "How do you respond after failing to find it?",
                        "text": "I'm sorry we couldn't find it.",
                        "next_label": "mai_fail_apology",
                        "impact": {
                            "stats": {
                                "reflection_score": 1,
                                "empathy": 1,
                                "trust_level": 0.5
                            }
                        }
                    },
                    {
                        "prompt": "How do you respond after failing to find it?",
                        "text": "There's still time, maybe tomorrow.",
                        "next_label": "mai_fail_tomorrow",
                        "impact": {
                            "stats": {
                                "remembering": 1,
                                "resilience": 1,
                                "trust_level": 0.5
                            }
                        }
                    }
                ]
                dynamic_choices = build_reflection_choices(mai_fail_choices)
                return_label = "mai_fail_post_choice"
            jump handle_dynamic_choice

    elif chosen_character == "eren":
        if has_flag("eren_search_success"):
            play music "search_success.wav" fadein 0.5 fadeout 0.5
            show eren smile1 at character_center_zoom_eren with dissolve
            "Eren collapses dramatically against my fence post, grinning like he's won the lottery."

            show eren smile3 at character_center_zoom_eren with dissolve
            eren "Turns out the little menace was hiding in the bushes the whole damn time!"
            "He punches my shoulder with affectionate force."

            python:
                eren_success_choices = [
                    {
                        "prompt": "How do you respond to Eren?",
                        "text": "Told you he'd be fine.",
                        "next_label": "eren_success_reassure",
                        "impact": {
                            "stats": {
                                "reflection_score": 1,
                                "empathy": 1,
                                "trust_level": 1
                            },
                            "relationship": ("eren", 2)
                        }
                    },
                    {
                        "prompt": "How do you respond to Eren?",
                        "text": "You owe me one.",
                        "next_label": "eren_success_tease",
                        "impact": {
                            "stats": {
                                "remembering": 1,
                                "resilience": 1
                            },
                            "relationship": ("eren", 1)
                        }
                    }
                ]
                dynamic_choices = build_reflection_choices(eren_success_choices)
                return_label = "eren_success_post"
            jump handle_dynamic_choice

        else:
            play music "sad0.mp3" fadein 0.5 fadeout 0.5
            show eren frustrated_angry at character_center_zoom_eren with dissolve
            "Eren stares into the dark, phone in hand. Still no messages. No signs."
            eren "I really thought... I thought we'd be lucky."

            python:
                eren_fail_choices = [
                    {
                        "prompt": "How do you comfort Eren?",
                        "text": "We’ll try again in the morning.",
                        "next_label": "eren_fail_reassure",
                        "impact": {
                            "stats": {
                                "remembering": 1,
                                "resilience": 1
                            },
                            "relationship": ("eren", 1)
                        }
                    },
                    {
                        "prompt": "How do you comfort Eren?",
                        "text": "I’m staying up with you, just in case.",
                        "next_label": "eren_fail_stayup",
                        "impact": {
                            "stats": {
                                "empathy": 1,
                                "trust_level": 1
                            },
                            "relationship": ("eren", 2)
                        }
                    }
                ]
                dynamic_choices = build_reflection_choices(eren_fail_choices)
                return_label = "eren_fail_post"
            jump handle_dynamic_choice


label mai_fail_apology:
    show i_mai unsatisfied at character_center_zoom_mai with dissolve
    n "Some things just slip away."
    jump mai_fail_post_choice
    return

label mai_fail_tomorrow:
    show i_mai shocked1 at character_center_zoom_mai with dissolve
    mai "Tomorrow... right. Maybe."
    jump mai_fail_post_choice
    return

label mai_fail_post_choice:
    jump scene2e_outcome
    return


label eren_fail_reassure:
    show i_eren confused1 at character_center_zoom_eren with dissolve
    eren "Yeah. We have to."
    jump scene2e_outcome

    return

label eren_fail_stayup:
    show i_eren smile1 at character_center_zoom_eren with dissolve
    eren "Thanks, [player_name]. For not giving up."
    jump eren_fail_post
    return

label eren_fail_post:
    jump scene2e_outcome

    return

label eren_success_reassure:
    show i_eren smile2 at character_center_zoom_eren with dissolve
    n "Kids always turn up where you least expect."
    show i_eren smile3 at character_center_zoom_eren with dissolve
    eren "Yeah? Well you turned up right when I needed someone."
    jump scene2e_outcome

    return

label eren_success_tease:
    show i_eren unhappy at character_center_zoom_eren with dissolve
    n "This better count as a favor."
    show i_eren smile1 at character_center_zoom_eren with dissolve
    eren "Hah! You're stuck with me now, buddy."
    jump scene2e_outcome

    return

label eren_success_post:
    jump scene2e_outcome
    return

label gratitude_mai_reason:
    show i_mai smile1 at character_center_zoom_mai with dissolve
    n "I could see how much this meant."
    show i_mai satisfied at character_center_zoom_mai with dissolve
    "She looks at me like I've spoken in riddles, then quickly wipes her eyes."
    jump scene2e_outcome

    return

label gratitude_mai_deflect:
    show i_mai angry1 at character_center_zoom_mai with dissolve
    n "Just returning lost property."
    show i_mai unsatisfied at character_center_zoom_mai with dissolve
    mai "Of course you'd say that."
    jump scene2e_outcome

    return

label gratitude_mai_post:
    show i_mai smile3 at character_center_zoom_mai with dissolve
    "For a brief moment, the ghost of a real smile appears before she turns away."
    jump scene2e_outcome
    return

label scene2e_outcome:
    hide eren
    hide mai
    $ set_flag(f"{other_character}_absent_next_scenes", True)
    scene black with fade
    "The night air hums with unspoken words as I turn toward my own doorstep."

    return
    # jump scene2e
    
# label scene2e:
#     $ reset_stat("ml_skill")
#     $ set_outcome("lesson2e", "unset")

#     call update_flowchart_status("scene2e") from _call_update_flowchart_status_6

#     play music "lesson_theme.mp3"
#     scene bg classroom_board_no_desk with fade
#     show hinata neutral_closed at center with dissolve

#     $ chosen_character = get_text_var("relationship_key")  # pulled forward from scene2e_transition

#     n "The morning sun cuts across the desks. Hinata steps forward again, her IBM badge catching the light."

#     show hinata smile_closed
#     hinata "Let’s talk about artificial neural networks — or ANNs — the digital brains behind modern AI."
#     show hinata smile_closed at right with dissolve
#     show slide neuralnet_structure_slide at slide_pos2 with dissolve

#     show hinata thinking_closed
#     hinata "They mimic how biological neurons work. Each node receives signals, applies weights, checks if it passes a threshold — then fires or doesn’t."

#     if chosen_character == "mai":
#         mc_internal "Like how Mai held onto that sketchbook — she kept processing, evaluating, deciding what to let through."
#     elif chosen_character == "eren":
#         mc_internal "Like Eren scanning every bush until he hit the right signal. Then—activation."

#     python:
#         neural_fire_choices = [
#             {
#                 "prompt": "What causes a neuron in a neural network to activate?",
#                 "text": "Its weighted input exceeds a threshold.",
#                 "next_label": "neuron_activation_correct",
#                 "impact": {
#                     "stats": {
#                         "ml_skill": 1
#                     }
#                 }
#             },
#             {
#                 "prompt": "What causes a neuron in a neural network to activate?",
#                 "text": "It gets a signal from any other node.",
#                 "next_label": "neuron_activation_wrong",
#                 "impact": {
#                     "stats": {
#                         "glitches": 1
#                     }
#                 }
#             }
#         ]
#         dynamic_choices = build_reflection_choices(neural_fire_choices)
#         return_label = "neuron_activation_post"
#     jump handle_dynamic_choice


#     show hinata neutral_closed
#     hinata "Neural nets have layers: input, hidden, and output. Each layer transforms the signal slightly — learning patterns as it goes."

#     show slide sigmoid_operation_slide with dissolve

#     hinata "Inside each node, inputs are multiplied by weights, summed up, and passed through something called an activation function."

#     hinata "Most often, that’s the sigmoid function: a = 1 / (1 + e^-z). It squashes outputs between 0 and 1."

#     show hinata happy_closed
#     hinata "Why? To give the network control — like a neuron whispering instead of shouting."

#     if chosen_character == "mai":
#         mc_internal "Like how Mai goes quiet when something matters most — not silent, but focused. Filtered."
#     elif chosen_character == "eren":
#         mc_internal "Like Eren cracking a joke, even when he's stressed — regulating the output. Keeping things stable."

#     python:
#         sigmoid_choices = [
#             {
#                 "prompt": "What is the purpose of the sigmoid activation function?",
#                 "text": "To normalize the output between 0 and 1.",
#                 "next_label": "sigmoid_correct",
#                 "impact": {
#                     "stats": {
#                         "ml_skill": 1
#                     }
#                 }
#             },
#             {
#                 "prompt": "What is the purpose of the sigmoid activation function?",
#                 "text": "To make the output zero for wrong predictions.",
#                 "next_label": "sigmoid_wrong",
#                 "impact": {
#                     "stats": {
#                         "glitches": 1
#                     }
#                 }
#             }
#         ]
#         dynamic_choices = build_reflection_choices(sigmoid_choices)
#         return_label = "sigmoid_post"
#     jump handle_dynamic_choice


#     show slide cost_function_slide with dissolve

#     hinata "Now let’s say the network makes a guess — like predicting someone’s test score."

#     hinata "We compare it to the real result. That difference is the error, or loss."

#     show hinata thinking_closed
#     hinata "We calculate that using a cost function. One common version: J = ½(y - ŷ)²."

#     hinata "The lower the cost, the better our prediction."

#     if chosen_character == "mai":
#         mc_internal "She never said thank you. But I could feel it. The cost of saying it outright might’ve been too high."
#     elif chosen_character == "eren":
#         mc_internal "He laughed like nothing happened. But I knew the stress was there — just minimized."

#     python:
#         cost_function_choices = [
#             {
#                 "prompt": "What is the cost function trying to minimize?",
#                 "text": "The squared difference between prediction and actual value.",
#                 "next_label": "cost_function_correct",
#                 "impact": {
#                     "stats": {
#                         "ml_skill": 1,
#                         "remembering": 1
#                     }
#                 }
#             },
#             {
#                 "prompt": "What is the cost function trying to minimize?",
#                 "text": "The number of activated neurons.",
#                 "next_label": "cost_function_wrong",
#                 "impact": {
#                     "stats": {
#                         "glitches": 1
#                     }
#                 }
#             }
#         ]
#         dynamic_choices = build_reflection_choices(cost_function_choices)
#         return_label = "cost_function_post"
#     jump handle_dynamic_choice


#     show slide backpropagation_slide with dissolve

#     hinata "So how do we learn from mistakes? With backpropagation."

#     show hinata neutral_closed
#     hinata "It’s the backward flow of error — adjusting the network’s weights layer by layer using gradients."

#     hinata "This is where machines change. Grow. Get better."

#     if chosen_character == "mai":
#         mc_internal "Mai rewrites the same line in her sketchbook over and over. That’s backprop — quiet, determined correction."
#     elif chosen_character == "eren":
#         mc_internal "Eren says he wings it, but I’ve seen how he adjusts. His brain’s been running backprop for years."

#     python:
#         backpropagation_choices = [
#             {
#                 "prompt": "How does backpropagation work?",
#                 "text": "It adjusts weights using gradients of the cost function.",
#                 "next_label": "backpropagation_correct",
#                 "impact": {
#                     "stats": {
#                         "ml_skill": 1
#                     }
#                 }
#             },
#             {
#                 "prompt": "How does backpropagation work?",
#                 "text": "It deletes neurons that made mistakes.",
#                 "next_label": "backpropagation_wrong",
#                 "impact": {
#                     "stats": {
#                         "glitches": 1
#                     }
#                 }
#             }
#         ]
#         dynamic_choices = build_reflection_choices(backpropagation_choices)
#         return_label = "backpropagation_post"
#     jump handle_dynamic_choice


#     hinata "ANNs aren’t just theories. They power Google search, voice assistants, even self-driving cars."

#     hinata "Their strength? They learn from data — and they don’t forget."

#     play audio "bell_ring.mp3"

#     mc_internal "Funny. After everything last night, this lesson felt... personal."

#     scene black with fade
#     pause 2.5

#     python:
#         if has_stat_minimum("ml_skill", 3) and has_stat_minimum("remembering", 1):
#             set_outcome("lesson2e", "success")
#         elif has_stat_minimum("ml_skill", 2):
#             set_outcome("lesson2e", "partial")
#         else:
#             set_outcome("lesson2e", "fail")
#     return

# label neuron_activation_correct:
#     hinata "Exactly. The neuron only fires if the combined input — after weights — passes a threshold."
#     return

# label neuron_activation_wrong:
#     hinata "Not quite. A neuron doesn’t fire from a single input alone — it sums all weighted inputs and checks if it’s enough."
#     return

# label neuron_activation_post:
#     return

# label sigmoid_correct:
#     hinata "Correct. Sigmoid squashes values into a smooth curve between 0 and 1 — useful when treating outputs like probabilities."
#     return

# label sigmoid_wrong:
#     hinata "That's a common mix-up. Sigmoid doesn’t hit exact zero — it compresses values smoothly. Even 'wrong' outputs get some weight."
#     return

# label sigmoid_post:
#     return
# label cost_function_correct:
#     hinata "Yes — that's our error. The cost function tells us how wrong the model’s guess was."
#     return

# label cost_function_wrong:
#     hinata "Ah, no — cost has nothing to do with how many neurons activate. It’s purely about how far off the prediction is."
#     return

# label cost_function_post:
#     return

# label backpropagation_correct:
#     hinata "Exactly. Gradients help us know which weights caused the error — and how to fix them, step by step."
#     return

# label backpropagation_wrong:
#     hinata "Nope — neural networks don’t delete parts of themselves. They learn by fine-tuning weights, not pruning structure."
#     return

# label backpropagation_post:
#     return
