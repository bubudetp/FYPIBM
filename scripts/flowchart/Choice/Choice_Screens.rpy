# ------------------------------------------------------------------------ Choice Screens
screen choice_preview(choice_text, impact_data):
    frame:
        xalign 0.5 yalign 0.8
        vbox:
            text choice_text
            hbox:
                $ icon = {"knowledge":"📚","relationships":"💬","difficulty":"⚡"}[impact_data["impact_type"]]
                text f"{icon} {impact_data['feedback_text']}"
                if "requirements" in impact_data:
                    text " (Requires: " + ", ".join(impact_data["requirements"]) + ")"

screen choice_impact_feedback(type="RELATIONSHIP", direction="↑"):
    default symbol = "+" if direction == "↑" else "-"
    default impact_color = "#57ff57" if direction == "↑" else "#ff5e5e"  # green or red

    frame:
        at feedback_popup_anim
        xalign 0.95
        yalign 0.05
        padding (12, 10)
        background "#0008"

        hbox:
            spacing 10
            text get_impact_icon(type) style "choice_feedback_icon"
            text "[get_impact_text(type)] [symbol]":
                style "choice_feedback_text"
                color impact_color

    timer 1.2 action Hide("choice_impact_feedback")
screen butterfly_effect():
    tag menu
    modal True
    
    # Clean modern background
    add "#1A1F2B" # Dark blue-gray background for a professional look
    
    frame:
        background None
        xfill True
        yfill True
        
        vbox:
            spacing 30
            xfill True
            yfill True
            
            # Top navigation tabs
            frame:
                background "#242A38"
                padding (5, 0)
                xfill True
                
                hbox:
                    xalign 0.5
                    spacing 0
                    
                    textbutton "ARC SUMMARY":
                        style "modern_tab_button"
                        text_style "modern_tab_text"
                        action NullAction()
                        selected True
                    
                    textbutton "STATISTICS":
                        style "modern_tab_button"
                        text_style "modern_tab_text"
                        action Show("player_statistics")
            
            # Main content area - two panels
            frame:
                background None
                padding (40, 0)
                xfill True
                yfill True

                # Use the hbox layout from the new code
                hbox:
                    spacing 40
                    xfill True
                    yfill True
                    
                    # Left side - List of Choices (using Frame from new code but keeping modern styling)
                    frame:
                        background "#242A38"  # Modern styling
                        # Alternative: background Frame("gui/frame.png", 10, 10)
                        xsize 700  # Using width from new code
                        yfill True
                        padding (20, 20)
                        
                        vbox:
                            spacing 15
                            xfill True
                            yfill True
                            
                            text "LIST OF CHOICES" style "modern_panel_title" xalign 0.5
                            
                            # Scrollable viewport for choices
                            viewport:
                                id "choices_viewport"
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                xfill True
                                yfill True
                                
                                vbox:
                                    spacing 10
                                    xfill True
                                    
                                    for entry in format_outcome_history():
                                        frame:
                                            background "#303848"  # Modern styling
                                            hover_background "#3B4356" # Modern styling
                                            # Alternative: background Frame("gui/choice_idle.png", 20, 20)
                                            # Alternative: hover_background Frame("gui/choice_hover.png", 20, 20)
                                            xfill True
                                            padding (20, 15)
                                            margin (0, 5)
                                            
                                            text entry.get("choice_text", "Unknown choice") style "modern_choice_text"
                    
                    # Right side - Outcomes (now in paragraph form)
                    frame:
                        background "#242A38"  # Modern styling
                        # Alternative: background Frame("gui/frame.png", 10, 10)
                        xsize 1100  # Using width from new code
                        yfill True
                        padding (20, 20)
                        
                        vbox:
                            spacing 15
                            xfill True
                            yfill True
                            
                            text "OUTCOME" style "modern_panel_title" xalign 0.5
                            
                            # Scrollable viewport for outcomes
                            viewport:
                                id "outcome_viewport"
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                xfill True
                                yfill True
                                
                                vbox:
                                    spacing 30
                                    xfill True
                                    
                                    # Each outcome is a clean entry
                                    for entry in format_outcome_history():
                                        if "impacts" in entry and entry["impacts"]:
                                            frame:
                                                background "#303848"  # Modern styling
                                                # Alternative: background Frame("gui/textbox.png", 20, 20)
                                                xfill True
                                                padding (25, 20)
                                                
                                                vbox:
                                                    spacing 15
                                                    xfill True
                                                    
                                                    # Choice that led to this outcome
                                                    text "Choice: [entry.get('choice_text', 'Unknown choice')]" style "modern_outcome_choice"
                                                    
                                                    # Paragraph of impacts
                                                    text " ".join([impact for impact in entry["impacts"]]) style "modern_outcome_paragraph"
            
            # Bottom navigation
            frame:
                background "#242A38"
                padding (10, 5)
                xfill True
                
                hbox:
                    xfill True
                    spacing 10
                    
                    textbutton "Back":
                        style "modern_button"
                        text_style "modern_button_text"
                        xalign 0.0
                        action Return()
                        
                    # Add additional buttons to match the screenshot
                    textbutton "History":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Skip":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Auto":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Save":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Q.Save":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Q.Load":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Prefs":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Flowchart":
                        style "modern_button"
                        text_style "modern_button_text"
                        action NullAction()
                        
                    textbutton "Arc Selection":
                        style "modern_button"
                        text_style "modern_button_text"
                        xalign 1.0
                        action NullAction()
# New Statistics Screen with 4-panel layout
screen player_statistics():
    tag menu
    modal True
    
    # Clean modern background
    add "#1A1F2B" # Dark blue-gray background for a professional look
    
    frame:
        background None
        xfill True
        yfill True
        
        vbox:
            spacing 20
            xfill True
            yfill True
            
            # Top navigation tabs
            frame:
                background "#242A38"
                padding (5, 0)
                xfill True
                
                hbox:
                    xalign 0.5
                    spacing 0
                    
                    textbutton "Arc Summary":
                        style "modern_tab_button"
                        text_style "modern_tab_text"
                        action Show("butterfly_effect")
                    
                    textbutton "Statistics":
                        style "modern_tab_button"
                        text_style "modern_tab_text"
                        action NullAction()
                        selected True
            
            # Main content area with four panels in a grid
            frame:
                background None
                padding (20, 10)
                xfill True
                yfill True

                grid 2 2:
                    spacing 15
                    xfill True
                    yfill True
                    
                    # Panel 1 - Topic 1 (Relationships Part 1)
                    frame:
                        background "#242A38"
                        xfill True
                        yfill True
                        padding (15, 15)
                        
                        vbox:
                            spacing 10
                            xfill True
                            
                            text "RELATIONSHIPS" style "modern_panel_title" xalign 0.5
                            
                            viewport:
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                xfill True
                                yfill True
                                
                                vbox:
                                    spacing 8
                                    xfill True
                                    
                                    # First half of relationships
                                    $ rel_items = list(sorted(branch_data["relationships"].items()))
                                    $ first_half = rel_items[:len(rel_items)//2]
                                    
                                    for name, value in first_half:
                                        vbox:
                                            spacing 3
                                            xfill True
                                            
                                            # Character name and value
                                            hbox:
                                                xfill True
                                                text "• [name.capitalize()]" style "modern_stat_name"
                                                text "[value]" style "modern_stat_value" xalign 1.0
                                            
                                            # Progress bar
                                            bar:
                                                value value
                                                range 10
                                                xfill True
                                                ysize 12
                                                left_bar "#4C88F0"
                                                right_bar "#303848"
                    
                    # Panel 2 - Topic 2 (Relationships Part 2)
                    frame:
                        background "#242A38"
                        xfill True
                        yfill True
                        padding (15, 15)
                        
                        vbox:
                            spacing 10
                            xfill True
                            
                            text "RELATIONSHIPS" style "modern_panel_title" xalign 0.5
                            
                            viewport:
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                xfill True
                                yfill True
                                
                                vbox:
                                    spacing 8
                                    xfill True
                                    
                                    # Second half of relationships
                                    $ rel_items = list(sorted(branch_data["relationships"].items()))
                                    $ second_half = rel_items[len(rel_items)//2:]
                                    
                                    for name, value in second_half:
                                        vbox:
                                            spacing 3
                                            xfill True
                                            
                                            # Character name and value
                                            hbox:
                                                xfill True
                                                text "• [name.capitalize()]" style "modern_stat_name"
                                                text "[value]" style "modern_stat_value" xalign 1.0
                                            
                                            # Progress bar
                                            bar:
                                                value value
                                                range 10
                                                xfill True
                                                ysize 12
                                                left_bar "#4C88F0"
                                                right_bar "#303848"
                    
                    # Panel 3 - Topic 3 (Player Stats)
                    frame:
                        background "#242A38"
                        xfill True
                        yfill True
                        padding (15, 15)
                        
                        vbox:
                            spacing 10
                            xfill True
                            
                            text "PLAYER STATS" style "modern_panel_title" xalign 0.5
                            
                            viewport:
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                xfill True
                                yfill True
                                
                                vbox:
                                    spacing 8
                                    xfill True
                                    
                                    # Stats bars
                                    for name, value in sorted(branch_data["stats"].items()):
                                        vbox:
                                            spacing 3
                                            xfill True
                                            
                                            # Stat name and value
                                            hbox:
                                                xfill True
                                                text "• [name.capitalize().replace('_', ' ')]" style "modern_stat_name"
                                                text "[value]" style "modern_stat_value" xalign 1.0
                                            
                                            # Progress bar
                                            bar:
                                                value value
                                                range 10
                                                xfill True
                                                ysize 12
                                                left_bar "#F0A840"
                                                right_bar "#303848"
                    
                    # Panel 4 - Topic 4 (Story Flags & Outcomes)
                    frame:
                        background "#242A38"
                        xfill True
                        yfill True
                        padding (15, 15)
                        
                        vbox:
                            spacing 10
                            xfill True
                            
                            text "GAME PROGRESS" style "modern_panel_title" xalign 0.5
                            
                            viewport:
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                xfill True
                                yfill True
                                
                                vbox:
                                    spacing 15
                                    xfill True
                                    
                                    # Story flags section (only showing true flags)
                                    vbox:
                                        spacing 8
                                        xfill True
                                        
                                        text "Story Flags" style "modern_subpanel_title"
                                        
                                        # Only show flags that are True
                                        $ true_flags = [(name, value) for name, value in sorted(branch_data["flags"].items()) if value == True]
                                        
                                        for name, value in true_flags:
                                            hbox:
                                                spacing 5
                                                xfill True
                                                
                                                text "• [name.replace('_', ' ').capitalize()]" style "modern_flag_text"
                                    
                                    # Outcomes section
                                    vbox:
                                        spacing 8
                                        xfill True
                                        
                                        text "Story Outcomes" style "modern_subpanel_title"
                                        
                                        # List layout for outcomes (skip "unset" values)
                                        for name, value in sorted(branch_data["outcomes"].items()):
                                            if value != "unset" and value != "none":
                                                hbox:
                                                    xfill True
                                                    text "• [name.replace('_', ' ').capitalize()]" style "modern_outcome_name"
                                                    text "[value]" style "modern_outcome_value" xalign 1.0
            
            # Bottom navigation
            frame:
                background "#242A38"
                padding (10, 5)
                xfill True
                
                hbox:
                    xalign 0.5
                    spacing 10
                    
                    textbutton "Back":
                        style "modern_button"
                        text_style "modern_button_text"
                        action Return()

# Retain the existing styles
style modern_tab_button:
    padding (50, 15)
    background "#242A38"
    hover_background "#303848"
    selected_background "#3B4356"

style modern_tab_text:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 26
    color "#9BA6BE"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"

style modern_panel_title:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 24
    color "#FFFFFF"
    text_align 0.5
    margin (0, 0, 0, 10)

style modern_subpanel_title:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#4C88F0"
    text_align 0.0
    margin (0, 0, 0, 8)

style modern_stat_name:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 20
    color "#FFFFFF"
    
style modern_stat_value:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 20
    color "#F0A840"
    
style modern_flag_text:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 20
    color "#FFFFFF"
    
style modern_outcome_name:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 20
    color "#FFFFFF"
    
style modern_outcome_value:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 20
    color "#F0A840"
    
style modern_button:
    background None
    hover_background "#303848"
    padding (20, 10)
    
style modern_button_text:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#9BA6BE"
    hover_color "#FFFFFF"
    
# Modern styles with Rajdhani font family
style modern_tab_button:
    padding (50, 15)
    background "#242A38"
    hover_background "#303848"
    selected_background "#3B4356"

style modern_tab_text:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 26
    color "#9BA6BE"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"

style modern_panel_title:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 30
    color "#FFFFFF"
    text_align 0.5
    margin (0, 0, 0, 15)

style modern_subpanel_title:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 24
    color "#4C88F0"  # Blue for section headers
    text_align 0.0
    margin (0, 0, 0, 10)

style modern_choice_text:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 22
    color "#FFFFFF"
    hover_color "#4C88F0" # Blue on hover

style modern_outcome_choice:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 24
    color "#4C88F0" # Blue for choice headers

style modern_outcome_paragraph:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 22
    color "#FFFFFF"
    line_spacing 5

style modern_button:
    background None
    hover_background "#303848"
    padding (20, 10)
    
style modern_button_text:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#9BA6BE"
    hover_color "#FFFFFF"

style modern_stat_name:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 22
    color "#FFFFFF"
    
style modern_stat_value:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 22
    color "#F0A840" # Orange for values
    
style modern_flag_text:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 20
    color "#FFFFFF"
    
style modern_outcome_name:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 20
    color "#FFFFFF"
    
style modern_outcome_value:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 20
    color "#F0A840" # Orange for values
label test_feedback_screen:
    show screen choice_impact_feedback()
    $ renpy.pause(100, hard=True)
    return

init python:
    def get_impact_text(itype):
        return {
            "RELATIONSHIP": "Bond Strengthened",
            "KNOWLEDGE": "Understanding Gained",
            "CRITICAL_THINKING": "Critical Thinking Boosted",
            "FOCUS": "Focus Improved",
            "MOTIVATION": "Motivation Increased",
            "IMMERSION": "Deeper Immersion",
            "EMOTION": "Emotional Impact",
            "STORY": "Story Progressed",
            "INDEPENDENCE": "Independent Thinking Encouraged",
            "CONFIDENCE": "Confidence Gained",
            "CURIOSITY": "Curiosity Sparked",
            "REFLECTION": "Reflection Deepened"
        }.get(itype, "Impact")

    def get_impact_icon(itype):
        return {
            "RELATIONSHIP": "🤝",
            "KNOWLEDGE": "🧠",
            "CRITICAL_THINKING": "🧐",
            "FOCUS": "🎯",
            "MOTIVATION": "🔥",
            "IMMERSION": "🌌",
            "EMOTION": "💓",
            "STORY": "📖",
            "INDEPENDENCE": "🚀",
            "CONFIDENCE": "💪",
            "CURIOSITY": "🔎",
            "REFLECTION": "🪞"
        }.get(itype, "❔")



# style choice_feedback_frame is default:
#     background "#000a"  # translucent black
#     padding (16, 16)
#     xalign 0.95
#     yalign 0.1
#     xmaximum 500
#     color "#fff"


transform choice_feedback_slide:
    on show:
        alpha 0
        linear 0.25 alpha 1
    on hide:
        linear 0.25 alpha 0

transform feedback_popup_anim:
    alpha 0
    ypos 0.03
    xoffset 20
    linear 0.25 alpha 1 ypos 0.05 xoffset 0
    pause 3
    linear 0.25 alpha 0 ypos 0.03 xoffset 20



style choice_feedback_text:
    size 36
    color "#ffffff"
    bold True
    spacing 2
    font "gui/fonts/Rajdhani-Medium.ttf"
    outlines [(1, "#000000", 0, 0)]
    text_align 1.0



style choice_feedback_icon is default:
    size 36
    color "#ffffff"
    bold True
    outlines [(1, "#000000", 0, 0)]



style choice_feedback_frame is default:
    background "#000a"
    xmaximum 600
    padding (16, 12)
