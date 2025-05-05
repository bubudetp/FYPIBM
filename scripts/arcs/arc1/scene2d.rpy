label scene2d:
    $ reset_stat("physics_skill")
    $ set_outcome("lesson2d", "unset")

    call update_flowchart_status("scene2d") from _call_update_flowchart_status_1

    play music "lesson_theme.mp3"
    scene bg classroom_board_no_desk with fade
    show hinata neutral_closed at center with dissolve

    n "The classroom murmurs as a new face steps to the front — confident posture, IBM lanyard glinting."

    show hinata smile_closed
    hinata "Good morning, everyone. I'm Hinata, and I'll be stepping in for Hayashi today."

    show hinata happy_closed
    hinata "Don't worry — I won't make n build a neural net before lunch. But I *will* make n think."

    mc_internal "She's sharp. Knows the room. I like that."

    n "She clicks the projector. The first slide appears."

    show slide deterministic_slide at slide_pos with dissolve # The F = ma slide

    show hinata thinking_closed at right with dissolve
    hinata "Let's begin where your instructor left off — deterministic systems."

    show hinata neutral_closed
    hinata "In these systems, the outcome is 100 percent predictable. If acceleration is 10 m/s2 and mass is 1kg, then the force is exactly 10N. Always."
    call update_flowchart_status("deterministic_choice") from _call_update_flowchart_status_6
    python:
        deterministic_choices = [
            {
                "prompt": "What best defines a deterministic system?",
                "text": "A system where outcomes are fully determined by known inputs.",
                "next_label": "deterministic_choice_correct",
                "impact": {
                    "stats": {
                        "deterministic_systems_skill": 1,
                        "physics_skill": 1,
                        "reflection_score": 1,
                        "decision_clarity": 0.5
                    }
                }
            },
            {
                "prompt": "What best defines a deterministic system?",
                "text": "A system where randomness always affects the result.",
                "next_label": "deterministic_choice_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1,
                        "reflection_score": 0.5 
                    }
                }
            }
        ]

        dynamic_choices = build_reflection_choices(deterministic_choices)
        return_label = "deterministic_post_choice"
    jump handle_dynamic_choice

label deterministic_choice_correct:
    jump deterministic_post_choice

label deterministic_choice_wrong:
    jump deterministic_post_choice

label backprop_correct:
    hinata "Exactly. Backpropagation tunes each weight by calculating the partial derivative of the error with respect to that weight — minimizing future error."
    jump backprop_post_choice

label backprop_wrong:
    hinata "No, that's incorrect. Neurons aren’t deleted — the learning process adjusts weights gradually to reduce error over time."
    jump backprop_post_choice

label backprop_post_choice:
    
    hinata "ANNs aren’t just theories. They power Google search, voice assistants, even self-driving cars."

    hinata "Their strength? They learn from data — and they don’t forget."
    stop music fadeout 0.5
    play music "wakeup_theme.mp3" fadein 0.5
    play audio "change_room_2.wav"
    play audio "hallway_full_sound.mp3"
    play audio "bell_ring.mp3"
    

    scene black with fade
    pause 2.5

    python:
        if has_stat_minimum("ml_skill", 3) and has_stat_minimum("remembering", 1):
            set_outcome("lesson2e", "success")
        elif has_stat_minimum("ml_skill", 2):
            set_outcome("lesson2e", "partial")
        else:
            set_outcome("lesson2e", "fail")
    return

label cost_function_correct:
    hinata "Yes — that's our error. The cost function tells us how wrong the model’s guess was."
    jump cost_function_post_choice
    return

label cost_function_wrong:
    hinata "Ah, no — cost has nothing to do with how many neurons activate. It’s purely about how far off the prediction is."
    jump cost_function_post_choice
    return

label cost_function_post_choice:

    show slide backpropagation_slide with dissolve
    hinata "So how do we learn from mistakes? With backpropagation."
    show hinata neutral_closed
    hinata "It’s the backward flow of error — adjusting the network’s weights layer by layer using gradients."
    hinata "This is where machines change. Grow. Get better."
    hinata """
        The weights in a neural network are adjusted according to some learning rule or algorithm, such as Hebbian learning.

        Thus, connectionists have created many sophisticated learning procedures for neural networks.

        Learning always involves modifying the connection weights.

        In general, these involve mathematical formulas to determine the change in weights when given sets of data consisting of activation vectors for some subset of the neural units.

        Several studies have been focused on designing teaching-learning methods based on connectionism.

        By formalizing learning in such a way, connectionists have many tools.

        A very common strategy in connectionist learning methods is to incorporate gradient descent over an error surface in a space defined by the weight matrix.

        All gradient descent learning in connectionist models involves changing each weight by the partial derivative of the error surface with respect to the weight.

        Backpropagation, first made popular in the 1980s, is probably the most commonly known connectionist gradient descent algorithm today.
    """

    python:
        backpropagation_choices = [
            {
                "prompt": "How does backpropagation update the network?",
                "text": "By adjusting weights based on the gradient of the error surface.",
                "next_label": "backprop_correct",
                "impact": {
                    "stats": {
                        "training_nn_skill": 1,
                        "ml_skill": 0.5
                    }
                }
            },
            {
                "prompt": "How does backpropagation update the network?",
                "text": "By deleting neurons that make mistakes.",
                "next_label": "backprop_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(backpropagation_choices)
        return_label = "backprop_post_choice"
    jump handle_dynamic_choice
    return

label sigmoid_correct:
    hinata "Correct. Sigmoid squashes values into a smooth curve between 0 and 1 — useful when treating outputs like probabilities."
    jump sigmoid_post_choice
    return

label sigmoid_wrong:
    hinata "That's a common mix-up. Sigmoid doesn’t hit exact zero — it compresses values smoothly. Even 'wrong' outputs get some weight."
    jump sigmoid_post_choice
    return

label sigmoid_post_choice:
    
    show slide cost_function_slide with dissolve

    show hinata thinking_closed
    hinata "Now let’s say the network makes a guess — like predicting someone’s test score."
    hinata "We compare it to the real result. That difference is the error, or loss."
    hinata "We calculate that using a cost function. One common version: J = ½(y - ŷ)²."
    hinata "The lower the cost, the better our prediction."

    python:
        cost_function_choices = [
            {
                "prompt": "What is the cost function trying to minimize?",
                "text": "The squared difference between prediction and actual value.",
                "next_label": "cost_function_correct",
                "impact": {
                    "stats": {
                        "training_nn_skill": 1,
                        "ml_skill": 0.5,
                        "decision_clarity": 0.5
                    }
                }
            },
            {
                "prompt": "What is the cost function trying to minimize?",
                "text": "The number of activated neurons.",
                "next_label": "cost_function_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(cost_function_choices)
        return_label = "cost_function_post_choice"

    jump handle_dynamic_choice
    return


label neuron_activation_correct:
    hinata "Exactly. The neuron only fires if the combined input — after weights — passes a threshold."
    jump neuron_activation_post_choice
    return

label neuron_activation_wrong:
    hinata "Not quite. A neuron doesn’t fire from a single input alone — it sums all weighted inputs and checks if it’s enough."
    jump neuron_activation_post_choice
    return

label neuron_activation_post_choice:
    
    show hinata neutral_closed
    call update_flowchart_status("neuralnet_intro") from _call_update_flowchart_status_9

    hinata "Neural nets have layers: input, hidden, and output. Each layer transforms the signal slightly — learning patterns as it goes."

    show slide sigmoid_operation_slide with dissolve

    hinata "Inside each node, inputs are multiplied by weights, summed up, and passed through something called an activation function."

    hinata "Most often, that’s the sigmoid function: a = 1 / (1 + e^-z). It squashes outputs between 0 and 1."

    show hinata happy_closed
    hinata "Why? To give the network control — like a neuron whispering instead of shouting."

    python:
        sigmoid_function_choices = [
            {
                "prompt": "What is the purpose of the sigmoid activation function?",
                "text": "To normalize the output between 0 and 1.",
                "next_label": "sigmoid_correct",
                "impact": {
                    "stats": {
                        "training_nn_skill": 1,
                        "ml_skill": 0.5,
                        "comprehension": 0.5
                    }
                }
            },
            {
                "prompt": "What is the purpose of the sigmoid activation function?",
                "text": "To make the output zero for wrong predictions.",
                "next_label": "sigmoid_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(sigmoid_function_choices)
        return_label = "sigmoid_post_choice"

    jump handle_dynamic_choice
    return



label regression_quiz_logistic:
    mc_internal "It's about probability. Like whether someone will accept an offer."
    jump regression_quiz_post_choice

    return

label regression_quiz_linear:
    mc_internal "That's for continuous predictions... right?"
    jump regression_quiz_post_choice
    return

label regression_quiz_post_choice:
    

    hinata "Remember — data teaches. But *n* decide what's worth learning."

    play audio "bell_ring.mp3"

    mc_internal "Even as the bell rings, her voice stays with me."

    scene black with fade
    pause 2
    python:
        if has_stat_minimum("physics_skill", 2) and has_stat_minimum("remembering", 1):
            set_outcome("lesson2d", "success")
        elif has_stat_minimum("physics_skill", 1):
            set_outcome("lesson2d", "partial")
        else:
            set_outcome("lesson2d", "fail")

    scene bg classroom_board_no_desk with fade
    show hinata smile_closed
    hinata "For the second part of the lesson, let’s talk about artificial neural networks — or ANNs — the digital brains behind modern AI."
    show hinata smile_closed at right with dissolve
    show slide neuralnet_structure_slide at slide_pos2 with dissolve
    
    hinata """
        Neural networks, also known as artificial neural networks (ANNs) or simulated neural networks (SNNs), are a subset of machine learning and are at the heart of deep learning algorithms.

        Their name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.

        Artificial neural networks (ANNs) are comprised of node layers, containing an input layer, one or more hidden layers, and an output layer.

        Each node, or artificial neuron, connects to another and has an associated weight and threshold.

        If the output of any individual node is above the specified threshold value, that node is activated, sending data to the next layer of the network.

        Otherwise, no data is passed along to the next layer of the network.

        Neural networks rely on training data to learn and improve their accuracy over time.

        However, once these learning algorithms are fine-tuned for accuracy, they are powerful tools in computer science and artificial intelligence, allowing us to classify and cluster data at a high velocity.

        Tasks in speech recognition or image recognition can take minutes versus hours when compared to the manual identification by human experts.

        One of the most well-known neural networks is Google’s search algorithm.

        Using the diagram above, let’s enter our input into a single-perceptron network.

        Note that in the node, the bias is applied, and it’s the logistical operation.
    """

    show hinata thinking_closed
    hinata "They mimic how biological neurons work. Each node receives signals, applies weights, checks if it passes a threshold — then fires or doesn’t."

    python:
        neuron_activation_choices = [
            {
                "prompt": "What causes a neuron in a neural network to activate?",
                "text": "Its weighted input exceeds a threshold.",
                "next_label": "neuron_activation_correct",
                "impact": {
                    "stats": {
                        "training_nn_skill": 1,
                        "deep_learning_frameworks_skill": 0.5,
                        "ml_skill": 0.5,
                        "comprehension": 0.5
                    }
                }
            },
            {
                "prompt": "What causes a neuron in a neural network to activate?",
                "text": "It gets a signal from any other node.",
                "next_label": "neuron_activation_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(neuron_activation_choices)
        return_label = "neuron_activation_post_choice"
    jump handle_dynamic_choice
    return

label regression_choice_logical:
    mc_internal "Seems fair enough."
    jump regression_post_choice
    return

label regression_choice_guesswork:
    mc_internal "People aren't equations. But it's a start."
    jump regression_post_choice
    return

label regression_post_choice:
    show slide optimization_slide with dissolve
    hinata "Last bit — optimization. Imagine trying to climb a hill blindfolded, in as few steps as possible."

    call update_flowchart_status("backprop_lesson") from _call_update_flowchart_status_10

    hinata "That's what machines do. Guess. Adjust. Repeat. It's what we call 'backpropagation.'"

    mc_internal "It's strange — but it makes sense. Machines learn like we do. Sometimes... better."

    # Quiz Option
    python:
        regression_quiz_choices = [
            {
                "prompt": "What type of regression fits predicting a yes/no outcome?",
                "text": "Logistic regression.",
                "next_label": "regression_quiz_logistic",
                "impact": {
                    "stats": {
                        "probability_skill": 1,
                        "ml_skill": 0.5,
                        "remembering": 1,
                        "decision_clarity": 0.5
                    }
                }
            },
            {
                "prompt": "What type of regression fits predicting a yes/no outcome?",
                "text": "Linear regression.",
                "next_label": "regression_quiz_linear",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(regression_quiz_choices)
        return_label = "regression_quiz_post_choice"

    jump handle_dynamic_choice
    return

label deterministic_choice_comfort:
    mc_internal "Knowing the outcome helps me breathe easier."
    jump deterministic_post_choice
    return

label deterministic_choice_rigid:
    mc_internal "Systems like that don't exist outside the board."
    jump deterministic_post_choice

label deterministic_post_choice:
    show slide probabilistic_slide with dissolve

    show hinata neutral_closed
    hinata """
        Probabilistic systems are where the data does not always have a fixed set of values and therefore, outcomes cannot be predicted with 100% accuracy.

        For example, how long it would take to travel by car from Detroit to Chicago depends on many random variables: time of day, weather, how much traffic is on the road, has there been an accident, will your car break down, etc.

        Regression in machine learning is used to predict outcomes in seemingly random data sets by incorporating known values into the model and then offering a prediction on what reasonably might be expected to happen.

        There are many types of regression, but let's look at two common regression models: linear and logistical.

        Linear Regression:

        Linear regression analysis is used to predict the value of a variable based on the value of another variable.

        The variable you want to predict is called the dependent variable.

        The variable you are using to predict the other variable's value is called the independent variable.

        This form of analysis estimates the coefficients of the linear equation, involving one or more independent variables, that best predict the value of the dependent variable.

        Linear regression fits a straight line or surface that minimizes the discrepancies between predicted and actual output values.

        There are simple linear regression calculators that use a “least squares” method to discover the best-fit line for a set of paired data.

        You then estimate the value of X (dependent variable) from Y (independent variable).

        With linear regression, you can predict the “best fit” for the curve and with high confidence explain that someone with a MA degree is likely making a certain amount of income different from one with a BA degree.

        Logistical Regression:

        This type of statistical analysis (also known as the logit model) is often used for predictive analytics and modeling and extends to applications in machine learning.

        In this analytics approach, the dependent variable is finite or categorical: either A or B (binary regression) or a range of finite options A, B, C, or D (multinomial regression).

        It is used in statistical software to understand the relationship between the dependent variable and one or more independent variables by estimating probabilities using a logistic regression equation.

        This type of analysis can help you predict the likelihood of an event happening or a choice being made.

        For example, you may want to know the likelihood of a visitor choosing an offer made on your website — or not (dependent variable).

        Your analysis can look at known characteristics of visitors, such as sites they came from, repeat visits to your site, behavior on your site (independent variables).

        Logistic regression models help you determine a probability of what type of visitors are likely to accept the offer — or not.

        As a result, you can make better decisions about promoting your offer or make decisions about the offer itself.

        With logistical regression, it is the S-curve and the probability that lies in between.

        This is a binary classification with political party A and political party B and the level of oversight that each thinks the government should have over its people.
    """

    show slide s_curve_slide with dissolve

    hinata """
        A typical neuron spikes occasionally in the absence of stimulation, spikes more and more frequently as stimulation builds up, and saturates at the fastest spiking rate it can muster, beyond which increased stimulation has no effect.

        Rather than a logic gate, a neuron is more like a voltage-to-frequency converter.

        Starts slowly, then faster and faster until it becomes almost constant again.

        The S-curve is the shape of phase transitions of all kinds: the probability of an electron flipping its spin as a function of the applied field, the magnetization of iron, the writing of a bit of memory to a hard disk, an ion channel opening in a cell, ice melting, the inflationary expansion of the early universe.

        Joseph Schumpeter said the economy evolves by cracks and leaps — S-curves are the shape of creative destruction.

        In Hemingway’s The Sun Also Rises, when Mike Campbell is asked how he went bankrupt, he replies: “Two ways. Gradually and then suddenly.”

        When you can’t get the temperature in the shower just right — first it’s too cold, and then it quickly shifts to too hot — blame the S-curve.

        Popcorn.

        Many phenomena we think of as linear are in fact S-curves because nothing can grow without a limit.

        Differentiate an S-curve and you get a bell curve.
    """

    mai "Popcorn?"

    hinata "Yes — kernels don't all pop at once. They wait... then explode. S-curves. Everywhere."

    python:
        scurve_choices = [
            {
                "prompt": "What real-world example best fits an S-curve?",
                "text": "Popcorn kernels bursting at different times.",
                "next_label": "scurve_choice_correct",
                "impact": {
                    "stats": {
                        "ml_skill": 0.5,
                        "remembering": 1,
                        "curiosity": 0.5
                    }
                }
            },
            {
                "prompt": "What real-world example best fits an S-curve?",
                "text": "A constant-speed train moving on a track.",
                "next_label": "scurve_choice_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1,
                        "reflection_score": -0.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(scurve_choices)
        return_label = "scurve_post_choice"

    jump handle_dynamic_choice
    return

label scurve_choice_correct:
    mc_internal "It's strange — once you notice it, the world feels full of hidden S-curves."
    jump scurve_post_choice
    return

label scurve_choice_wrong:
    mc_internal "Maybe I missed the point... trains don't shift phases like popcorn does."
    jump scurve_post_choice
    return

label scurve_post_choice:
    show slide regression_slide with dissolve

    hinata "Let's talk regression. n want to predict your grade based on how long n studied and slept."

    hinata """
        Regression takes the data and tries to find the result that minimizes prediction mistakes, maximizing what is called goodness of fit.

        A physicist, an engineer, and a statistician go on a hunting trip.

        The physicist measures the bullet speed, bullet drop, shoots, and misses by 5 feet to the right.

        The engineer says you need to account for wind, measures that, and shoots — misses by 5 feet to the left.

        The statistician says hoorah without shooting at all and claims they got it.

        Being precisely perfect on average can mean being actually wrong each time.

        Regression can keep missing several feet to the left or several feet to the right.

        Even if it averages out to be the correct answer, a regression can mean never actually hitting the target.

        Unlike regression, machine learning predictions might be wrong on average, but when the predictions miss, they often don’t miss by much.

        Statisticians describe this as allowing some bias in exchange for reducing variance.

        Inventing a new machine learning method involves proving that it works better in practice.

        In contrast, inventing a regression method requires first proving that it works in theory — it requires the articulation of a hypothesis.

        Machine learning has less need to specify in advance what goes into the model.

        It can accommodate the equivalent of much more complex models with many more interactions between variables.
    """

    python:
        regression_choices = [
            {
                "prompt": "What does the hunting trip story illustrate?",
                "text": "Regression may be accurate on average but wrong on individual predictions.",
                "next_label": "regression_choice_correct",
                "impact": {
                    "stats": {
                        "probability_skill": 1,
                        "remembering": 1,
                        "ml_skill": 0.5
                    }
                }
            },
            {
                "prompt": "What does the hunting trip story illustrate?",
                "text": "Machine learning needs perfect measurements every time.",
                "next_label": "regression_choice_wrong",
                "impact": {
                    "stats": {
                        "glitches": 1,
                        "reflection_score": -0.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(regression_choices)
        return_label = "regression_post_choice"

    jump handle_dynamic_choice
    return

label regression_choice_correct:
    mc_internal "It’s clear now — precision in theory doesn't always mean precision in practice."
    jump regression_post_choice
    return

label regression_choice_wrong:
    mc_internal "Wait... maybe I misunderstood. Machine learning is forgiving to messy inputs."
    jump regression_post_choice
    return


label scene2d_transition:

    scene bg hallway_day
    with dissolve
    show i_eren smile1 at character_base_pose_right_eren with dissolve
    eren "Finally! I thought that lecture would never end."
    "You and Eren step into the hallway. The air feels lighter, but something in his posture seems tense."
    play audio "train_sound.wav"
    play music train_inside fadein 0.5
    scene bg train_day2
    with dissolve
    show i_eren confused1 at character_base_pose_right_eren with dissolve
    eren "Ugh. Just once I want to hear a professor say, 'You know what? Never mind.'"
    play music "courtyard_piano.mp3" fadein 0.5 fadeout 0.5

    scene bg shopping_street_day
    with fade
    play audio "shopping_street_ambiance.wav" fadein 0.5 fadeout 0.5
    "You're laughing when n spot Mai up ahead."

    show i_mai smile1 at character_base_pose_left_mai with dissolve
    mai "Hey! Didn't expect to see you two here."
    show i_eren confused1 at character_base_pose_right_eren with dissolve
    eren "Hey, Mai. Nice bag—wait, is that your sketchbook sticking out?"

    show i_mai smile2 at character_base_pose_left_mai with dissolve
    mai "Yeah. I was just—"

    show i_mai shocked1 at character_base_pose_left_mai with dissolve
    "Suddenly, her smile vanishes. She checks her bag. Again. Then again."
    play music "stress_theme.wav" fadein 0.5


    mai "...No. No, no, no—"
    stop audio
    
    play audio "phone_buzz.mp3"
    "At the same time, Eren's phone buzzes. He reads the message and stops walking."

    show i_eren shocked1 at character_base_pose_right_eren with dissolve
    eren "…[player_name]."

    scene bg store_open_sunset with dissolve
    with dissolve

    "Eren grabs your arm. Tight."

    show i_eren unhappy at character_center_zoom_eren with dissolve
    eren "I need your help. Right now."

    n "What is it?"

    "He shows you a message from his younger brother."

    centered "{i}'I'm going to look for Kuma. Don't tell mom.  I'll be back before sunset.'{/i}"

    eren "Kuma got out this morning. I thought he was still in the house."

    eren "Now my little brother went out looking for him. And he hasn't answered since."

    "He's trying to stay calm, but his voice is shaking."

    eren "Last time... when our old cat disappeared, we never saw her again. My brother was crushed."

    eren "If anything happens to him—"

    "He swallows hard."

    eren "I can't go through that again."

    "Before n can respond, Mai suddenly speaks, panicked."

    hide i_eren with dissolve
    show i_mai shocked1 at character_center_zoom_mai with dissolve

    mai "[player_name]—I lost my sketchbook."

    "She holds up her bag, eyes wide with dread."

    mai "It's not just drawings. I was going to give it to my dad."

    n "Wait... your dad?"

    mai "He reached out after years. Said he wanted to see me. He's only in town today."

    "Her voice cracks."

    mai "I put everything in there. Memories. Letters. Things I was never brave enough to say out loud."

    "She looks down at the pavement, barely holding it together."

    mai "If I don't find it… I'm not going."

    "The street is quiet. Your heart pounds."

    "Two people. Two emergencies. And not enough time."


    show i_mai shocked1 at character_base_pose_left_mai with dissolve
    show i_eren unhappy at character_base_pose_right_eren with dissolve
    call update_flowchart_status("scene2d_transition") from _call_update_flowchart_status_2

    menu(time=2, timeout="scene2d_indecisive"):
        # timeout 6.0
        n "Choose who to help — time is running out"

        "Help Mai recover her sketchbook for her father":
            $ set_text_var("relationship_key", "mai")
            call update_flowchart_status("help_mai") from _call_update_flowchart_status_3
            $ increase_rel("mai")
            $ set_flag("helped_mai_sketchbook")
            show i_mai smile2 at character_center_zoom_mai with dissolve
            n "Let's go. He needs to see what n made."
            mai "Thank you… I really didn't want to face this alone."
            call friendship_outcome from _call_friendship_outcome


        "Help Eren find his brother and the cat before dark":
            $ set_text_var("relationship_key", "eren")
            $ increase_rel("eren")
            call update_flowchart_status("help_eren") from _call_update_flowchart_status_4
            $ set_flag("helped_eren_search")
            show i_mai unsatisfied at character_base_pose_left_mai with dissolve
            show i_eren smile1 at character_center_zoom_eren with dissolve
            n "Come on. Let's bring them home."
            eren "...Thank n. I needed someone right now."
            call friendship_outcome from _call_friendship_outcome_1
    return

label friendship_outcome:
    play music "memory.ogg" fadein 0.5 fadeout 0.5

    scene bg station_evening with fade
    n "The train hums softly. The city lights blur past the window as we race against the ticking clock."

    n "Something stirs in the back of my mind... a memory from earlier."

    scene bg classroom_board_no_desk with fade
    show hinata neutral_closed at center
    n "Hinata’s voice echoes like a bell."

    show hinata thinking_closed
    hinata "Split into subsets. If they're all pure, you're done. If not—branch again."

    show hinata smile_closed
    hinata "Look for the strongest signal. Weather. Then type of calls. Then movement."

    scene bg train_day with fade
    # play audio "train_sound.wav" fadein 0.5 fadeout 0.5
    play audio "train_ambiance.wav" fadein 0.5 fadeout 0.5
    play audio train_inside fadein 0.5 volume 0.5
    n "Right. Decision trees. Narrow the options. Follow the signals."

    scene black with fade
    pause 0.5
    
    centered "{cps=10}{size=+20}{color=#FF0000}YOU TRY TO REMEMBER...{/color}{/size}{/cps}"

    $ flashback_target = "sketchbook" if has_flag("helped_mai_sketchbook") else "Kuma"


    centered "{cps=10}{size=+20}{color=#FF0000}THIS LESSON IS IMPORTANT.{/color}{/size}{/cps}"

    centered "{cps=10}{size=+20}{color=#FF0000}IT HOLDS THE KEY TO FINDING THE MISSING [flashback_target]..{/color}{/size}{/cps}"

    stop audio
    call classifier_teaching from _call_classifier_teaching



    return

label after_classifier:
    play audio train_inside fadein 0.5 fadeout 0.5 volume 0.2
    play music "stress_theme.wav" fadein 0.5 fadeout 0.5
    if has_flag("helped_mai_sketchbook"):
        scene bg train_day with fade
        show i_mai smile1 at character_center_zoom_mai with dissolve
        mai "I remember passing a few spots where I stopped earlier. Maybe we can retrace from there?"
        python:
            search_location_choices = [
                {
                    "prompt": "What's the strongest signal for where to search first?",
                    "text": "Lockers — she passed there and someone may have moved it. (lockroom_evening)",
                    "next_label": "search_lockroom",
                    "impact": {
                        "stats": {
                            "remembering": 1
                        }
                    }
                },
                {
                    "prompt": "What's the strongest signal for where to search first?",
                    "text": "Storefront — high visibility but unpredictable. (store_closed_night)",
                    "next_label": "search_storefront",
                    "impact": {
                        "stats": {
                            "physics_skill": 1
                        }
                    }
                },
                {
                    "prompt": "What's the strongest signal for where to search first?",
                    "text": "Hayashi’s Office — a wildcard. (LOCKED unless full score)",
                    "next_label": "search_office",
                    "locked": not get_outcome("classifer_lesson") == "success",
                    "locked_text": "Too unpredictable. I need stronger signals."
                },
            ]

            dynamic_choices = build_reflection_choices(search_location_choices)
            return_label = "search_post_choice"

        jump handle_dynamic_choice
    elif has_flag("helped_eren_search"):
        
        scene bg train_day with fade
        show i_eren smile1 at character_base_pose_right_eren with dissolve
        eren "Okay. If I were my brother… where would I go first?"

        n "Hinata’s words echo again: Find the feature that best splits the data."
        stop audio
        call choose_kuma_search_location from _choose_kuma_search_location
    return 

label after_search_decision:
    jump friendship_outcome
return
label choose_kuma_search_location:
    play music "stress_theme.wav" fadein 0.5 fadeout 0.5
    scene bg schoolway_2_night with fade

    python:
        choice1_text = "School Back — Kuma hid there last time. Strong precedent. (school_back_night)"
        choice1_locked = get_outcome("classifier_lesson") == "fail"

        if choice1_locked:
            choice1_text = "??? — You can’t recall where he might be... (Locked)"

        kuma_search_location_choices = [
            {
                "prompt": "Which location gives the strongest likelihood of finding them?",
                "text": "[choice1_text]",
                "next_label": "search_school_back",
                "locked": choice1_locked,
                "locked_text": "You hesitate. Something about the lesson... it didn’t stick.",
                "impact": {
                    "stats": {
                        "remembering": 1
                    }
                }
            },
            {
                "prompt": "Which location gives the strongest likelihood of finding them?",
                "text": "Courtyard — peaceful but lower chance. (courtyard_night)",
                "next_label": "search_courtyard",
                "impact": {
                    "stats": {
                        "reflection_score": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(kuma_search_location_choices)
        return_label = "kuma_search_post_choice"

    jump handle_dynamic_choice

    return


label search_storefront:
    scene bg store_closed_night with fade
    n "The display is still lit, but no sign of the sketchbook."
    if get_outcome("classifer_lesson") in ["success", "partial"]:
        show i_mai smile3 at character_center_zoom_mai
        mai "Wait! Behind that bench—there!"
        $ set_flag("mai_search_success")
        $ set_text_var("friend_locked", "mai")
    else:
        show i_mai unsatisfied at character_center_zoom_mai
        mai "Nothing. Let's keep going."
        $ set_flag("mai_search_fail")
    jump scene2e_transition

label search_lockroom:
    scene bg lockroom_evening with fade
    n "The hallway feels eerie at night."
    if get_outcome("classifer_lesson") == "success":
        show i_mai satisfied at character_center_zoom_mai
        call update_flowchart_status("sketchbook_found") from _call_update_flowchart_status_13
        mai "Yes! It's here — someone must’ve picked it up and left it here."
        $ set_flag("mai_search_success")
        $ set_text_var("friend_locked", "mai")
    else:
        show i_mai angry1 at character_center_zoom_mai
        call update_flowchart_status("sketchbook_lost") from _call_update_flowchart_status_14
        mai "Still no sign of it..."
        $ set_flag("mai_search_fail")
    jump scene2e_transition

label search_office:
    scene bg hayashi_office_black_white with fade
    n "The atmosphere changes. The air is heavier, grayscale."
    show i_mai smile2 at character_center_zoom_mai
    mai "It… it’s here. Thank you."
    $ set_flag("mai_search_success")
    $ set_text_var("friend_locked", "mai")
    jump scene2e_transition

label search_courtyard:
    scene bg courtyard_night with fade
    n "Wind rustles the trees."
    if get_outcome("classifer_lesson") in ["success", "partial"]:
        show i_eren smile3 at character_center_zoom_eren
        eren "There they are! My brother and Kuma — safe."
        call update_flowchart_status("kuma_found") from _call_update_flowchart_status_15
        $ set_flag("eren_search_success")
        $ set_text_var("friend_locked", "eren")
    else:
        call update_flowchart_status("kuma_lost") from _call_update_flowchart_status_16
        show i_eren confused1 at character_center_zoom_eren
        eren "No sign. Let's check somewhere else."
        $ set_flag("eren_search_fail")
    jump scene2e_transition

label search_school_back:
    scene bg school_back_night with fade
    n "The empty field echoes every step."
    if get_outcome("classifer_lesson") == "success":
        show i_eren smile2 at character_center_zoom_eren with dissolve
        eren "Kuma! And my brother’s here too!"
        $ set_flag("eren_search_success")
        $ set_text_var("friend_locked", "eren")
    else:
        show i_eren frustrated_angry at character_center_zoom_eren with dissolve
        eren "Still nothing. We're losing time."
        $ set_flag("eren_search_fail")
    jump scene2e_transition

label classifier_flashback:    
    scene bg classroom_board_no_desk at flashback_effect_1 with fade
    show hinata neutral_closed at center

    n "Hinata's voice echoes like a bell."

    show hinata thinking_closed
    hinata "Split into subsets. If they're all pure, you're done. If not—branch again."

    show hinata smile_closed
    hinata "Look for the strongest signal. Weather. Then type of calls. Then movement."

    scene bg train_day with fade
    return

label classifier_teaching:
    call update_flowchart_status("classifier_lesson") from _call_update_flowchart_status_17
    $ time_display = "Tuesday, 10:00 AM"
    call show_time() from _call_show_time
    $ reset_stat("physics_skill")
    $ set_outcome("classifier_lesson", "unset")

    call update_flowchart_status("classifer_lesson") from _call_update_flowchart_status_5
    stop music 
    stop audio
    
    play music "lesson_theme.mp3"
    scene bg classroom_board_no_desk with fade
    show hinata neutral_closed at center with dissolve

    show hinata smile_closed
    hinata "Good morning, everyone."
    show hinata thinking_closed at right with dissolve

    show slide predict_nemra_slide at slide_pos3 with dissolve

    hinata "Imagine this: Nemra works at IBM. Some days she commutes. Some days she works from home."

    show hinata neutral_closed
    hinata "We want to predict if she’ll go to the office using a method called a decision tree."

    hinata "A decision tree splits data into smaller pieces based on key features — like the weather or her exercise habits."

    hinata "The goal is to keep dividing until each group — or branch — only contains one kind of answer. That’s called a pure subset."

    python:
        first_split_choices = [
            {
                "prompt": "What’s the first feature we should split by?",
                "text": "Weather condition.",
                "next_label": "first_split_weather",
                "impact": {
                    "stats": {
                        "decision_clarity": 1,
                        "remembering": 1
                    }
                }
            },
            {
                "prompt": "What’s the first feature we should split by?",
                "text": "Type of calls scheduled.",
                "next_label": "first_split_calls",
                "impact": {
                    "stats": {
                        "reflection_score": 1
                    }
                }
            }
        ]


        dynamic_choices = build_reflection_choices(first_split_choices)
        return_label = "first_split_post_choice"
    jump handle_dynamic_choice

label first_split_weather:
    mc_internal "Weather seems like a major deciding factor."
    jump first_split_post_choice

label first_split_calls:
    mc_internal "Could be, but might not be the first split."
    jump first_split_post_choice

label first_split_post_choice:

    show slide decision_tree_slide at slide_pos3 with dissolve

    hinata "Correct — weather is a strong initial indicator."

    hinata "Now look at the overcast days — all of them result in a commute. That branch is pure, so we stop there."

    hinata "But Sunny and Rainy days? Those still show mixed results. That’s where entropy comes in."

    python:
        sunny_split_choices = [
            {
                "prompt": "How should we split the Sunny days?",
                "text": "Type of calls.",
                "next_label": "sunny_split_calls",
                "impact": {
                    "stats": {
                        "decision_clarity": 1,
                        "remembering": 1
                    }
                }
            },
            {
                "prompt": "How should we split the Sunny days?",
                "text": "Exercise routine.",
                "next_label": "sunny_split_exercise",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            }
        ]
        dynamic_choices = build_reflection_choices(sunny_split_choices)
        return_label = "sunny_split_post_choice"
    jump handle_dynamic_choice
label sunny_split_calls:
    mc_internal "Call type probably influences home vs office work."
    jump sunny_split_post_choice

label sunny_split_exercise:
    mc_internal "Possibly… but seems like a weaker signal."
    jump sunny_split_post_choice

label sunny_split_post_choice:

    show slide branch_slide at slide_pos3 with dissolve

    hinata "Entropy measures uncertainty. If the results are mixed, we keep splitting using the next most informative feature."

    hinata "So, for Sunny days, we branch into Video vs Telephone calls."

    hinata "For Rainy days, it makes sense to split based on Exercise — Gym or Walk."

    python:
        commute_prediction_choices = [
            {
                "prompt": "Which scenario would most strongly predict a commute?",
                "text": "Rainy weather with walking exercise.",
                "next_label": "commute_rain_walk",
                "impact": {
                    "stats": {
                        "decision_clarity": 1,
                        "remembering": 1
                    }
                }
            },
            {
                "prompt": "Which scenario would most strongly predict a commute?",
                "text": "Sunny weather with video calls.",
                "next_label": "commute_sunny_video",
                "impact": {
                    "stats": {
                        "glitches": 1
                    }
                }
            }
        ]
        dynamic_choices = build_reflection_choices(commute_prediction_choices)
        return_label = "commute_prediction_post_choice"
    jump handle_dynamic_choice
label commute_rain_walk:
    mc_internal "This path leads to a pure ‘Yes’ outcome."
    jump commute_prediction_post_choice

label commute_sunny_video:
    mc_internal "Nope — that one predicts working from home."
    jump commute_prediction_post_choice

label commute_prediction_post_choice:
    show slide prediction_slide at slide_pos3 with dissolve

    hinata "Exactly. When we follow the path: Rain → Walk → Commute, we get a confident prediction."

    hinata "Think of it like following a trail of the strongest clues."

    hinata "Decision trees help machines — and humans — solve uncertainty step by step."

    play audio "bell_ring.mp3"

    mc_internal "Even as the bell rings, her voice stays with me. There was a structure to it. A way to think through decisions."

    scene black with fade
    pause 2.5

    scene black with dissolve
    stop music fadeout 0.5

    python:
        if has_stat_minimum("physics_skill", 2) and has_stat_minimum("remembering", 1):
            set_outcome("classifier_lesson", "success")
            renpy.jump("classifier_flashback_success")
        else:
            set_outcome("classifier_lesson", "fail")
            renpy.jump("classifier_flashback_fail")


    return

label classifier_flashback_success:
    centered "{size=+20}{color=#47b300}YOU HAVE REMEMBERED..{/color}{/size}"
    pause 0.5
    centered "{i}{size=+20}{color=#47b300}BY APPLYING THE PRINCIPLES...{/i}"
    pause 1.0
    jump post_classifier_redirect

label classifier_flashback_fail:
    centered "{size=+10}{color=#FF0000}YOU FORGOT..{/color}{/size}"
    pause 0.5
    centered "{i}YOU LOSE{/i}"
    pause 1.0
    jump post_classifier_redirect


label scene2d_indecisive:
    centered "{size=+20}{color=#FF0000}TIME IS RUNNING OUT...{/color}{/size}"
    pause 1.0
    centered "{i}{size=+20}{color=#FF0000}MAKE A DECISION.{/i}"
    pause 1.0
    return


label post_classifier_redirect:
    if has_flag("helped_mai_sketchbook"):
        jump after_classifier
    elif has_flag("helped_eren_search"):
        jump after_classifier
    else:
        jump after_classifier
