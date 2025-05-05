
init python:
    # Default Slide Content
    title_text = "Title of the slide"
    paragraph1_content = ""
    paragraph2_content = ""

    paragraph1_is_image = False
    paragraph2_is_image = False
    paragraph1_image = None
    paragraph2_image = None

    # Layout & Display Settings
    screen_width = 1280
    screen_height = 720

    title_xalign = 0.5
    title_yalign_normal = 0.3
    title_yalign_centered = 0.5

    box_width = 600
    box_height = 500
    box_spacing = 100

    image_max_width = 580  # Image max width inside the box
    image_max_height = 480  # Image max height inside the box

    line_spacing = 10
    font_size = 28

    def set_title(new_title):
        global title_text
        title_text = new_title

    def set_paragraph1(content, is_image=False, image_path=None):
        global paragraph1_content, paragraph1_is_image, paragraph1_image
        paragraph1_is_image = is_image
        if is_image:
            paragraph1_image = image_path  # Store the image path
            paragraph1_content = ""  # Clear text when image is set
        else:
            paragraph1_content = content  # Set text
            paragraph1_image = None  # Remove image if setting text

    def set_paragraph2(content, is_image=False, image_path=None):
        global paragraph2_content, paragraph2_is_image, paragraph2_image
        paragraph2_is_image = is_image
        if is_image:
            paragraph2_image = image_path
            paragraph2_content = ""  # Clear text when image is set
        else:
            paragraph2_content = content  # Set text
            paragraph2_image = None  # Remove image if setting text

    def get_title_yalign():
        """Determine whether title should be centered or not."""
        if not paragraph1_content.strip() and not paragraph2_content.strip() and not paragraph1_image and not paragraph2_image:
            return title_yalign_centered
        return title_yalign_normal

    def get_box_widths():
        """Return appropriate width for each box based on paragraph content."""
        only_one = (bool(paragraph1_content.strip()) or paragraph1_is_image) != (bool(paragraph2_content.strip()) or paragraph2_is_image)
        if only_one:
            return screen_width - (2 * box_spacing)
        return box_width


# custom UI time system
        # Time variables
    hour = 8
    minute = 0
    period = "AM"
    day = 1
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_name = day_names[0]
    
    def advance_time(h=0, m=0):
        """
        Advance time by specified hours and minutes
        Example: advance_time(1, 30) - adds 1 hour and 30 minutes
        """
        global hour, minute, period, day, current_day_name
        
        # Add minutes
        minute += m
        
        # Handle minute overflow
        while minute >= 60:
            minute -= 60
            hour += 1
        
        # Add hours
        hour += h
        
        # Handle hour overflow and period change
        while hour >= 12:
            if hour >= 13:  # Only reduce if we go beyond 12
                hour -= 12
            
            # Toggle AM/PM when we pass 12
            if period == "AM":
                period = "PM"
            else:
                period = "AM"
                if hour != 12: 
                    day += 1
                    day_index = (day - 1) % 7  # Calculate day of week (0-6)
                    current_day_name = day_names[day_index]
        
        # Update the display
        renpy.restart_interaction()
    
    def set_time(h, m, p="AM"):
        """
        Set the time to a specific hour, minute, and period
        Example: set_time(3, 30, "PM") - sets time to 3:30 PM
        """
        global hour, minute, period
        
        # Validate inputs
        if h < 1 or h > 12:
            h = 12 if h == 0 else min(12, max(1, h))
        
        if m < 0 or m > 59:
            m = min(59, max(0, m))
        
        if p not in ["AM", "PM"]:
            p = "AM"
        
        # Set the time
        hour = h
        minute = m
        period = p
        
        # Update the display
        renpy.restart_interaction()
    
    def set_day(d, name=None):
        """
        Set the day number and optionally the day name
        Example: set_day(5, "Friday") - sets day to 5 and day name to Friday
        """
        global day, current_day_name
        
        day = max(1, d)  # Ensure day is at least 1
        
        if name and name in day_names:
            current_day_name = name
        else:
            # Automatically set day name based on day number
            day_index = (day - 1) % 7
            current_day_name = day_names[day_index]
        
        # Update the display
        renpy.restart_interaction()


# screen chapter_diagnostic():

#     tag menu

#     add "gui/diagnostic_bg.png"  # Replace with your custom background if desired

#     frame:
#         xalign 0.5
#         yalign 0.1
#         background None
#         has vbox spacing 15

#         text "Chapter 1 — System Snapshot" size 42 color "#FFFFFF" bold True

#     vbox:
#         spacing 20
#         xalign 0.5
#         yalign 0.25
#         text "🧠 Reflection Score: [reflection_score]" size 28 color "#CCCCFF"
#         text "🧍 Remembering: [remembering]" size 28 color "#A5FFDA"
#         text "⚠️ Glitches Detected: [glitches]" size 28 color "#FFAFAF"

#     vbox:
#         xalign 0.5
#         yalign 0.55
#         spacing 10
#         text "🔑 Key Choices Made:" size 30 color "#FFFFFF" underline True

#         if insight:
#             text "• Insight: [insight]" size 24 color "#FFFFFF"
#         if self_model:
#             text "• Self Model: [self_model]" size 24 color "#FFFFFF"
#         if walk_response:
#             text "• Walk Home Thought: [walk_response]" size 24 color "#FFFFFF"

#     vbox:
#         xalign 0.5
#         yalign 0.78
#         spacing 10
#         text "💬 Relationship Summary" size 30 color "#FFFFFF" underline True

#         text "• Girl C: [rel_girl_c]%" size 24 color "#FFC9F4"
#         text "• Boy A: [rel_boy_a]%" size 24 color "#C9F2FF"
#         text "• Girl A: [rel_girl_a]%" size 24 color "#FFDAB9"

#     textbutton "Continue" action Return() xalign 0.5 yalign 0.95
