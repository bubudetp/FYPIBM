default quiz_score = 0
label scene3_3:
    scene bg classroom_board_with_desk with fade
    $ time_display = "09:00 AM"
    call show_time() from _call_show_time_13
    scene bg classroom_board_no_desk with fade
    play audio "school_bell.ogg" fadein 0.5 fadeout 0.5
    play music "lesson_theme_hinata.mp3" fadein 1.0 fadeout 0.5
    n "The final class before the quiz."

    # call scene_3_3_event from _call_scene_3_3_event

    show hayashi neutral_closed at right with dissolve
    hayashi "A framework is a structure."
    hayashi "It tells the system how to learn, without telling it what it’s learning."

    # === DEEP LEARNING ECOSYSTEM SLIDE ===
    show slide dl_ecosystem at slide_pos3 with dissolve 
    hayashi "Let’s begin with the big picture — the Deep Learning ecosystem."
    hayashi "This space is evolving rapidly, driven by innovation and increasing adoption in real-world industries."
    hayashi "Companies now use deep learning not just for research, but to generate business insights, automate systems, and serve clients better."
    hayashi "Thanks to high-performance GPUs and distributed computing, we can now train models once considered impossible — models that analyze language, vision, and behavior with astonishing accuracy."

    # === APACHE SYSTEMML ===
    show slide dl_apache with dissolve
    hayashi "One key movement is declarative machine learning — like Apache SystemML."
    hayashi "It lets data scientists express analytics tasks without needing to manually optimize for hardware or data format."
    hayashi "This kind of system enables flexibility, adaptability, and separation between what the model does and how it executes."
    hayashi "It means researchers can focus on ideas — the system handles the rest."

    # === TENSORFLOW ===
    show slide dl_tensorflow with dissolve
    hayashi "TensorFlow is Google’s answer to scalable, production-ready deep learning."
    hayashi "Built on lessons from their proprietary 'DistBelief' system, TensorFlow was designed for distributed computing from the start."
    hayashi "It runs on CPUs, GPUs, and TPUs — specialized chips built by Google for neural network acceleration."
    hayashi "Released under Apache 2.0 in 2015, it became one of the most widely adopted frameworks in the world — and still dominates open-source deep learning today."

    # === TORCH ===
    show slide dl_torch with dissolve
    hayashi "Torch is different — it puts scripting and speed first."
    hayashi "Built on LuaJIT and a C/CUDA core, it provides deep GPU control with a clean, flexible syntax."
    hayashi "You get powerful N-dimensional arrays, fast matrix operations, built-in neural net tools, and direct hooks into mobile platforms like iOS and Android."
    hayashi "Its design philosophy? Make advanced models easy to write, fast to run, and portable enough to embed."

    # === THEANO ===
    show slide dl_theano with dissolve
    hayashi "Theano is like symbolic NumPy with superpowers."
    hayashi "You write math expressions using multi-dimensional arrays, and Theano compiles them to optimized CPU or GPU code."
    hayashi "It supports automatic differentiation — so it handles your derivatives, even for complex composite functions."
    hayashi "It’s precise, efficient, and powerful — ideal for research, especially when speed and custom behavior matter."
    hayashi "Logarithmic tricks, symbolic gradients, dynamic C compilation — it was built to push math to its limits."

    # === CAFFE ===
    show slide dl_caffe with dissolve
    hayashi "Caffe is all about speed — especially in vision tasks."
    hayashi "Developed at Berkeley’s Vision and Learning Center, it ported the fast convolutional nets of MATLAB into optimized C/C++."
    hayashi "Its strength lies in how easy it is to define models and train them quickly."
    hayashi "It also offers a Python API, making it accessible to researchers and developers alike."
    hayashi "Caffe paved the way for early breakthroughs in image recognition and object detection."

    # === CNTK ===
    show slide dl_cntk with dissolve
    hayashi "CNTK — Microsoft’s Computational Network Toolkit — is built around computation graphs."
    hayashi "You define a network as a directed graph of operations — matrix multiplications, activations, layers."
    hayashi "It supports deep models like CNNs and RNNs, and parallelizes training across multiple GPUs and servers."
    hayashi "CNTK uses stochastic gradient descent with auto-differentiation and can scale from a laptop to a distributed system."
    hayashi "Its goal is to enable collaboration through shared open-source implementations, accelerating progress in the field."

    jump student_fadeout_post

label student_fadeout_post:
    
    # hayashi
    "You do not need to understand the model."
    "You only need to trust its results."
    jump scene3_3_quiz

    return

label scene3_3_event:
    python:
        if glitches >= 4:
            renpy.say(mc_internal, "There’s static at the edge of my hearing. Like the system’s trying to stabilize itself.")
        elif remembering >= 3:
            renpy.say(mc_internal, "Something’s off. Not just the air — the timeline. I know what happened. Even if they don’t.")
        elif reflection_score >= 7:
            renpy.say(mc_internal, "We’ve learned so much. But I still feel like I’m missing the *point*.")

label scene3_3_quiz:
    $ flowchart_manager.unlock_arc("act3_quiz")
    scene bg classroom_board_no_desk with fade
    show hayashi neutral_closed at center with dissolve
    play music "suspenful_music.mp3" volume 0.3 fadein 1.0 fadeout 0.5 loop
    hayashi "Let’s see how well you’ve absorbed the material."
    hayashi "This quiz will test your understanding of the deep learning ecosystem and its frameworks."

    python:
        ml_quiz_1 = [
            {
                "prompt": "1. Machine learning systems are good with making predictions, but which of the following is a shortcoming where humans excel?",
                "text": "Machines require lots of data, humans don’t",
                "next_label": "ml_quiz_1_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "1. Machine learning systems are good with making predictions, but which of the following is a shortcoming where humans excel?",
                "text": "Humans can obtain more data from smell, feel, and hearing",
                "next_label": "ml_quiz_1_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "1. Machine learning systems are good with making predictions, but which of the following is a shortcoming where humans excel?",
                "text": "Humans can judge and make decisions on preferences",
                "next_label": "ml_quiz_1_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "1. Machine learning systems are good with making predictions, but which of the following is a shortcoming where humans excel?",
                "text": "All the above",
                "next_label": "ml_quiz_1_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "remembering": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_1)
        return_label = "ml_quiz_2"
    jump handle_dynamic_choice


label ml_quiz_1_correct:
    $ quiz_score += 1
    show hayashi happy_closed at center with dissolve
    hayashi "Correct. Machines need data, but humans can make decisions from instinct or minimal cues."
    jump ml_quiz_2
    return

label ml_quiz_1_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve
    hayashi "That's partially true, but the most fundamental shortcoming of machines is their reliance on large datasets."
    jump ml_quiz_2
    return

# Question 2
label ml_quiz_2:
    python:
        ml_quiz_2 = [
            {
                "prompt": "2. Which of the following is an example of a deep learning framework?",
                "text": "Microsoft Azure",
                "next_label": "ml_quiz_2_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "2. Which of the following is an example of a deep learning framework?",
                "text": "Amazon AWS",
                "next_label": "ml_quiz_2_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "2. Which of the following is an example of a deep learning framework?",
                "text": "IBM Cloud",
                "next_label": "ml_quiz_2_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "2. Which of the following is an example of a deep learning framework?",
                "text": "Google TensorFlow",
                "next_label": "ml_quiz_2_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "ml_skill": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_2)
        return_label = "ml_quiz_3"
    jump handle_dynamic_choice


label ml_quiz_2_correct:
    $ quiz_score += 1
    show hayashi happy_closed at center with dissolve
    mc_internal "Yes. TensorFlow is a major open-source framework developed by Google."
    jump ml_quiz_3
    return

label ml_quiz_2_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve
    mc_internal "Those are cloud platforms. TensorFlow is the actual deep learning framework."
    jump ml_quiz_3
    return

# Question 3
label ml_quiz_3:
    python:
        ml_quiz_3 = [
            {
                "prompt": "3. Which of the following may be shortcomings of supervised learning?",
                "text": "Requires vast amounts of data",
                "next_label": "ml_quiz_3_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "supervised_learning_skill": 1
                    }
                }
            },
            {
                "prompt": "3. Which of the following may be shortcomings of supervised learning?",
                "text": "Labeling the data is arduous and expensive",
                "next_label": "ml_quiz_3_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "supervised_learning_skill": 1
                    }
                }
            },
            {
                "prompt": "3. Which of the following may be shortcomings of supervised learning?",
                "text": "They are not used much as of late",
                "next_label": "ml_quiz_3_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "3. Which of the following may be shortcomings of supervised learning?",
                "text": "Clustering is difficult in supervised learning",
                "next_label": "ml_quiz_3_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_3)
        return_label = "ml_quiz_4"
    jump handle_dynamic_choice


label ml_quiz_3_correct:
    show hayashi happy_closed at center with dissolve
    $ quiz_score += 1

    mc_internal "Correct — supervised learning is powerful, but costly in terms of data and labeling."
    jump ml_quiz_4
    return

label ml_quiz_3_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve
    mc_internal "That’s not a primary limitation. Let’s move on."
    jump ml_quiz_4
    return

# Question 4
label ml_quiz_4:
    python:
        ml_quiz_4 = [
            {
                "prompt": "4. Reinforcement learning is best suited for which task?",
                "text": "Identify faces for access to secure areas",
                "next_label": "ml_quiz_4_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "4. Reinforcement learning is best suited for which task?",
                "text": "Virtual agents and other chatbots",
                "next_label": "ml_quiz_4_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "4. Reinforcement learning is best suited for which task?",
                "text": "Discovery systems that can crawl the web",
                "next_label": "ml_quiz_4_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "4. Reinforcement learning is best suited for which task?",
                "text": "Stocking and retrieving products in a warehouse for optimizing space utilization and operations",
                "next_label": "ml_quiz_4_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "reinforcement_learning_skill": 1
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_4)
        return_label = "ml_quiz_5"
    jump handle_dynamic_choice


label ml_quiz_4_correct:
    $ quiz_score += 1
    show hayashi happy_closed at center with dissolve
    mc_internal "Perfect — reinforcement learning is all about optimizing behavior in an environment over time."
    jump ml_quiz_5
    return

label ml_quiz_4_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve

    mc_internal "Those tasks better fit other machine learning types. Reinforcement is more environment-interactive."
    jump ml_quiz_5
    return

# Question 5
label ml_quiz_5:
    python:
        ml_quiz_5 = [
            {
                "prompt": "5. In October 2015, AlphaGo, an AI-powered system, beat Mr. Fan Hui at the board game Go. What machine learning method did it use?",
                "text": "Unsupervised",
                "next_label": "ml_quiz_5_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "5. In October 2015, AlphaGo, an AI-powered system, beat Mr. Fan Hui at the board game Go. What machine learning method did it use?",
                "text": "Supervised",
                "next_label": "ml_quiz_5_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "5. In October 2015, AlphaGo, an AI-powered system, beat Mr. Fan Hui at the board game Go. What machine learning method did it use?",
                "text": "Reinforcement",
                "next_label": "ml_quiz_5_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "reinforcement_learning_skill": 1,
                        "ml_skill": 0.5
                    }
                }
            },
            {
                "prompt": "5. In October 2015, AlphaGo, an AI-powered system, beat Mr. Fan Hui at the board game Go. What machine learning method did it use?",
                "text": "Semi-supervised",
                "next_label": "ml_quiz_5_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_5)
        return_label = "ml_quiz_6"
    jump handle_dynamic_choice


label ml_quiz_5_correct:
    $ quiz_score += 1
    show hayashi happy_closed at center with dissolve
    mc_internal "Correct — AlphaGo used reinforcement learning to master the game of Go."
    jump ml_quiz_6
    return

label ml_quiz_5_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve
    mc_internal "Not quite — AlphaGo’s brilliance came from reinforcement learning."
    jump ml_quiz_6
    return

# Question 6
label ml_quiz_6:
    python:
        ml_quiz_6 = [
            {
                "prompt": "6. Which of the following best distinguishes artificial narrow intelligence (ANI) from artificial general intelligence (AGI)?",
                "text": "With ANI, robots must be told what to do; with AGI, robots don’t have to be programmed",
                "next_label": "ml_quiz_6_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "6. Which of the following best distinguishes artificial narrow intelligence (ANI) from artificial general intelligence (AGI)?",
                "text": "Siri and Alexa are examples of ANI; autonomous cars are examples of AGI",
                "next_label": "ml_quiz_6_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "6. Which of the following best distinguishes artificial narrow intelligence (ANI) from artificial general intelligence (AGI)?",
                "text": "ANI systems do one thing well; AGI systems have multi-domain expertise",
                "next_label": "ml_quiz_6_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "6. Which of the following best distinguishes artificial narrow intelligence (ANI) from artificial general intelligence (AGI)?",
                "text": "All the above",
                "next_label": "ml_quiz_6_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "ml_intro_skill": 1,
                        "remembering": 0.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_6)
        return_label = "ml_quiz_8"
    jump handle_dynamic_choice


label ml_quiz_6_correct:
    $ quiz_score += 1
    show hayashi happy_closed at center with dissolve
    mc_internal "Exactly — all three statements describe key differences between ANI and AGI."
    jump ml_quiz_8
    return

label ml_quiz_6_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve
    mc_internal "That’s only part of the picture. All three points help distinguish ANI from AGI."
    jump ml_quiz_8
    return

# Question 8
label ml_quiz_8:
    python:
        ml_quiz_8 = [
            {
                "prompt": "7. If you're building a deep learning ecosystem, which two concerns should be your starting points?",
                "text": "Purchase the appropriate hardware and software for deep learning",
                "next_label": "ml_quiz_8_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "7. If you're building a deep learning ecosystem, which two concerns should be your starting points?",
                "text": "Ensure that I have Python running plus all the necessary packages and libraries",
                "next_label": "ml_quiz_8_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
            {
                "prompt": "7. If you're building a deep learning ecosystem, which two concerns should be your starting points?",
                "text": "Ensure that I have access to robust platform as a service plus access to deep learning frameworks",
                "next_label": "ml_quiz_8_correct",
                "impact": {
                    "stats": {
                        "quiz_score": 1,
                        "deep_learning_frameworks_skill": 1,
                        "remembering": 0.5
                    }
                }
            },
            {
                "prompt": "7. If you're building a deep learning ecosystem, which two concerns should be your starting points?",
                "text": "Moved all my data to a cloud platform with robust deep learning algorithms and access to vast related databases",
                "next_label": "ml_quiz_8_wrong",
                "impact": {
                    "stats": {
                        "reflection_score": 0.5
                    }
                }
            },
        ]

        dynamic_choices = build_reflection_choices(ml_quiz_8)
        return_label = "ml_quiz_results"
    jump handle_dynamic_choice


label ml_quiz_8_correct:
    $ quiz_score += 1
    show hayashi happy_closed at center with dissolve
    mc_internal "Right — framework access and platform robustness come first."
    jump ml_quiz_results
    return

label ml_quiz_8_wrong:
    $ quiz_score -= 1
    show hayashi neutral_closed at center with dissolve
    mc_internal "Important, but not the most immediate starting point for ecosystem setup."
    jump ml_quiz_results
    return

# Results Screen
label ml_quiz_results:
    n "The quiz ends. The screen fades."
    scene bg classroom_day_left with fade
    pause 1.5
    python:
        if quiz_score >= 6:
            renpy.say(mc_internal, "Most of that felt… easy. Like I remembered it before he said it.")
        elif quiz_score >= 4:
            renpy.say(mc_internal, "Some answers were guesses. But they felt right.")
        else:
            renpy.say(mc_internal, "Was I even here for these lessons? My mind’s a scatterplot.")
    
    call screen butterfly_effect 
    return
