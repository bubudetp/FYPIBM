screen immersion_summary():
    frame:
        style_prefix "flowchart"
        xalign 0.5
        yalign 0.1
        padding (20, 20)

        vbox:
            spacing 15
            text "IMMERSION TRACKER SUMMARY" size 32

            for k, v in immersion_tracker.dimensions.items():
                text f"{k.title()}: {v:.2f}"

            text ""
            text "EMOTIONAL PROFILE SUMMARY" size 28

            text f"Transportation: {emotional_profile.transportation:.2f}"
            text f"Mental Imagery: {emotional_profile.mental_imagery:.2f}"

            text "Character Empathy:"
            for k, v in emotional_profile.character_empathy.items():
                text f"{k.title()}: {v:.2f}"

screen reflection_summary():
    tag menu
    modal True
    frame:
        style "menu_frame"
        vbox:
            label "Reflection Summary"

            text "Reflection Score: [stat('reflection_score')]"
            text "Memory Stability: [stat('remembering')]"
            text "System Glitches: [stat('glitches')]"

            label "Relationship Updates"
            for char, value in branch_data["relationships"].items():
                if value != 0:
                    text "[char.capitalize()]: [value]"

            label "Outcomes"
            for name, result in branch_data["outcomes"].items():
                if result != "unset":
                    text "[name.replace('_',' ').capitalize()]: [result]"

            textbutton "Continue" action Return()

screen arc_unlock_notification(title, thumbnail):
    frame:
        vbox:
            text "New Path Unlocked: [title]"
            if thumbnail:
                add thumbnail
            timer 3.0 action Hide("arc_unlock_notification")

screen act_summary_screen(node):
    tag menu
    frame:
        style "menu_frame"
        vbox:
            text "Act Summary" size 40
            text "Immersion Profile:"
            for k, v in node.__dict__.items():
                if k in ["curitosity", "concentration", "challenge", "control", "comprehension", "empathy", "familiarity"]:
                    text f"{k.capitalize()}: {v:.2f}"

            text "Emotional Influence:"
            for char, v in node.character_interactions.items():
                text f"{char.capitalize()}: {v:.2f}"

            text "Emotional Transport: [node.emotion.get('transport', 0.0):.2f]"
            text "Mental Imagery: [node.emotion.get('imagery', 0.0):.2f]"

        textbutton "Continue" action Return()

# Define styles for the character profile screen
style character_tab:
    background "#333A44"
    hover_background "#3D4F5C"
    selected_background "#2B3944"
    xminimum 120
    yminimum 40
    padding (10, 10)
    
style character_tab_text:
    size 20
    color "#FFFFFF"
    selected_color "#FFFFFF"
    outlines [(1, "#000000")]
    text_align 0.5
    xalign 0.5
    
style trait_label:
    size 16
    color "#FFFFFF"
    xalign 0.0
    yalign 0.5
    outlines [(1, "#000000")]
    
style relationship_label:
    size 16
    color "#FFFFFF"
    xalign 0.0
    yalign 0.5
    outlines [(1, "#000000")]
    
style character_name:
    size 42
    color "#FFFFFF"
    xalign 0.0
    bold True
    outlines [(2, "#000000")]
    
style section_header:
    size 24
    color "#FFFFFF"
    xalign 0.0
    bold True
    outlines [(1, "#000000")]
    
style menu_title:
    size 28
    color "#FFFFFF"
    xalign 0.5
    text_align 0.5
    bold True
    outlines [(2, "#000000")]
    
style summary_text:
    size 18
    color "#CCCCCC"
    outlines [(1, "#000000")]
    
style trait_bar:
    left_bar "#3E92CC"
    right_bar "#1E1E1E"
    xmaximum 120
    ymaximum 14
    background "#111111"
    
style relationship_bar:
    left_bar "#3E92CC" 
    right_bar "#1E1E1E"
    xmaximum 120
    ymaximum 14
    background "#111111"
    
style chapter_button:
    background "#333A44"
    hover_background "#3D4F5C"
    selected_background "#2B3944"
    xalign 0.5
    padding (20, 10)
    
style chapter_button_text:
    size 24
    color "#FFFFFF"
    outlines [(1, "#000000")]

# Define the character profile screen
screen character_profile():
    tag menu
    modal True
    
    style_prefix "default"
    
    default current_character = "Jennie"
    default current_tab = "Character"
    
    frame:
        style_prefix "default"
        background "#14171A"
        xfill True
        yfill True
        
        hbox:
            style_prefix "character_tab"
            xalign 0.5
            ypos 20
            spacing 10
            
            textbutton "BUTTERFLY EFFECT":
                style "character_tab"
                text_style "character_tab_text"
                action SetScreenVariable("current_tab", "Butterfly")
            
            textbutton "CHARACTER INFO":
                style "character_tab" 
                text_style "character_tab_text"
                selected current_tab == "Character"
                action SetScreenVariable("current_tab", "Character")
            
        if current_tab == "Character":
            
            # Character selection bar
            hbox:
                xalign 0.5
                ypos 80
                spacing 2
                
                for char_name in characters:
                    textbutton char_name:
                        style "character_tab"
                        text_style "character_tab_text"
                        xminimum 80
                        selected char_name == current_character
                        action SetScreenVariable("current_character", char_name)
            
            # Character name
            text characters[current_character].name.upper():
                style "character_name"
                xpos 50
                ypos 150
            
            # Main content area
            hbox:
                xpos 50
                ypos 200
                spacing 100
                
                # Left side - Character traits
                vbox:
                    spacing 10
                    
                    text "CHARACTER\nTRAITS":
                        style "section_header"
                        yoffset 20
                    
                    for trait, value in characters[current_character].traits.items():
                        hbox:
                            spacing 20
                            text trait.upper():
                                style "trait_label"
                                xminimum 100
                            bar value value range 10:
                                style "trait_bar"
                
                # Right side - Relationship status
                vbox:
                    spacing 10
                    
                    text "RELATIONSHIP\nSTATUS":
                        style "section_header"
                        yoffset 20
                    
                    for other_char, value in characters[current_character].relationships.items():
                        hbox:
                            spacing 20
                            text other_char.upper():
                                style "relationship_label"
                                xminimum 100
                            bar value value range 10:
                                style "relationship_bar"
            
            # Character image on the right side
            frame:
                xpos 850
                ypos 150
                background None
                
                # You would replace this with an actual image
                # add "images/characters/[characters[current_character].image].png"
                # Using a colored rectangle as placeholder
                frame:
                    background "#000000"
                    xsize 500
                    ysize 600
        
        elif current_tab == "Butterfly":
            # Display game stats and tracking information
            grid 2 3:
                xalign 0.5
                yalign 0.5
                spacing 40
                
                # IMMERSION
                vbox:
                    spacing 10
                    text "Immersion Profile" style "menu_title"
                    for dim in ["curiosity", "concentration", "challenge", "control", "comprehension", "empathy", "familiarity"]:
                        $ value = immersion_tracker.dimensions.get(dim, 0)
                        text f"{dim.capitalize()}: {int(value * 100)}%" style "summary_text"
                
                # EMOTION
                vbox:
                    spacing 10
                    text "Emotional Response" style "menu_title"
                    text f"Transportation: {int(emotional_profile.transportation)}" style "summary_text"
                    text f"Mental Imagery: {int(emotional_profile.mental_imagery)}" style "summary_text"
                    
                    # Character empathy if available
                    if emotional_profile.character_empathy:
                        text "Character Empathy:" style "summary_text"
                        for char, value in emotional_profile.character_empathy.items():
                            text f"  {char}: {int(value)}" style "summary_text"
                
                # RELATIONSHIPS
                vbox:
                    spacing 10
                    text "Character Relationships" style "menu_title"
                    for name, rel in persistent.relationships_stats.items():
                        hbox:
                            text f"{name}: " style "summary_text"
                            bar value rel range 100 style "relationship_bar"
                
                # FLOWCHART / NARRATIVE
                vbox:
                    spacing 10
                    $ flowchart = flowchart_manager.get_current_flowchart()
                    $ visited = len(flowchart.visited_nodes)
                    $ total = len(flowchart.nodes)
                    $ visited_paths = len(flowchart.visited_paths)
                    
                    text "Narrative Exploration" style "menu_title"
                    text f"Nodes Visited: {visited}/{total}" style "summary_text"
                    text f"Completion: {int(flowchart.calculate_completion())}%" style "summary_text"
                    text f"Branching Paths Taken: {visited_paths}" style "summary_text"
                
                # GLOBAL COMPLETION
                vbox:
                    spacing 10
                    text "Global Progress" style "menu_title"
                    text f"Overall Story Completion: {int(flowchart_manager.calculate_global_progress())}%" style "summary_text"
                    
                    # Acts completion if relevant
                    text "Acts Completion:" style "summary_text"
                    for arc_id, arc in flowchart_manager.arcs.items():
                        if arc.unlocked:
                            text f"  {arc.title}: {int(arc.completion)}%" style "summary_text"
        
        elif current_tab == "Twins":
            # Placeholder for Twins tab content
            text "Twins information would go here" style "menu_title":
                xalign 0.5
                yalign 0.5
        
        # Back button (always visible)
        hbox:
            xalign 0.95
            yalign 0.95
            spacing 10
            
            textbutton "BACK":
                style "chapter_button"
                text_style "chapter_button_text"
                action Return()

# Functions to cycle through characters with keyboard
init -5 python:
    def cycle_character(direction):
        # Get the current character from the screen
        current = renpy.get_screen_variable("current_character", "Jennie")
        char_list = list(characters.keys())
        
        # Find current index
        try:
            idx = char_list.index(current)
        except ValueError:
            idx = 0
            
        # Calculate new index with wraparound
        new_idx = (idx + direction) % len(char_list)
        
        # Set the new character
        renpy.set_screen_variable("current_character", char_list[new_idx])
    
    def cycle_tabs(direction):
        tabs = ["Butterfly", "Character", "Twins"]
        current = renpy.get_screen_variable("current_tab", "Character")
        
        try:
            idx = tabs.index(current)
        except ValueError:
            idx = 1  # Default to Character tab
            
        new_idx = (idx + direction) % len(tabs)
        renpy.set_screen_variable("current_tab", tabs[new_idx])

# Optional keyboard navigation
screen character_profile_keys():
    key "K_LEFT" action Function(cycle_tabs, -1)
    key "K_RIGHT" action Function(cycle_tabs, 1)
    key "K_UP" action Function(cycle_character, -1)
    key "K_DOWN" action Function(cycle_character, 1)