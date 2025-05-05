label scene2c:
    play music "lesson_theme.mp3"
    scene bg classroom_board_no_desk with fade
    show hayashi happy_closed at right
    with dissolve
    call update_flowchart_status("scene2c") from _call_update_flowchart_status
    n "Hayashi begins before the room settles."
    hayashi "Last time, we introduced machine learning as a system that learns from data instead of rules."
    hayashi "Today: the *ways* machines learn. There are three major approaches."
    n "He writes three terms on the board in bold: {i}Supervised, Unsupervised, Reinforcement.{/i}"
    mc_internal "I've heard those before. But never explained like this."
    hayashi "Supervised learning: you feed the algorithm labeled data. It learns by example."
    hayashi "It's powerful — but labeling data is expensive. Humans still have to do that."
    eren "So basically... we babysit the AI till it figures stuff out?"
    hayashi "You could say that. The babysitter analogy holds — but only until it gets better than you."
    mai "What about when *I* get better than it?"
    hayashi "Then you're ready to switch sides."
    mc_internal "The class actually laughs at that. Hayashi cracks a smile."
    hayashi "Unsupervised learning is different. No labels. Just raw data. The system finds patterns on its own."
    jennie "Like giving it a box of puzzle pieces with no picture to match?"
    hayashi "Exactly. It clusters similar data, tries to find structure in the chaos."
    menu:
        "What's your reaction to unsupervised learning?"
        
        "That sounds harder than supervised.":
            $ increase_stat("reflection_score", 0.5)
            mc_internal "No labels, no direction? That's rough."
            
        "It's like how humans pick up habits.":
            $ increase_stat("reflection_score", 1)
            mc_internal "We don't always need instruction. Sometimes we just... notice patterns."
            
        "Kind of creepy, honestly.":
            $ increase_stat("glitches", 1)
            mc_internal "Machines teaching themselves makes my skin crawl a little."
            
    hayashi "Third, reinforcement learning."
    hayashi "Here, the system receives feedback — rewards for good actions, penalties for mistakes."
    hayashi "It learns by doing. Trial and error."
    mai "So... like life."
    eren "Or video games."
    hayashi "Both are accurate."
    mc_internal "I like this one. Feedback loops make sense. You act, the world reacts. Learn, adapt."
    
    menu:
        "Which type makes the most sense to you?"
        
        "Supervised — clear instructions, clear results.":
            $ increase_stat("physics_skill", 1)
            mc_internal "I like clarity. Examples help."
            
        "Unsupervised — finding patterns naturally.":
            $ increase_stat("reflection_score", 1)
            mc_internal "It mirrors how I make sense of people sometimes."
            
        "Reinforcement — learn by doing.":
            $ increase_stat("physics_skill", 0.5)
            $ increase_stat("reflection_score", 0.5)
            mc_internal "Mistakes are lessons. That hits."
            
    hayashi "That's enough for today. But the quiz? I'll leave that to someone else."
    
    python:
        # Using helper functions to check conditions and set outcome
        if has_stat_minimum("physics_skill", 4) and has_stat_minimum("remembering", 1):
            set_outcome("lesson2c", "success")
        elif has_stat_minimum("physics_skill", 2):
            set_outcome("lesson2c", "partial")
        else:
            set_outcome("lesson2c", "fail")
            
    scene black with fade
    return