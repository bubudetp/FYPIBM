image hinata happy_talk:
    "images/characters/hinata/happy_closed.png"
    pause renpy.random.uniform(0.15, 0.25)  # Random pause between 0.15s - 0.25s
    "images/characters/hinata/happy_open.png"
    pause renpy.random.uniform(0.15, 0.25)
    repeat

image hinata thinking_talk:
    "images/characters/hinata/thinking_closed.png"
    pause renpy.random.uniform(0.2, 0.35)
    "images/characters/hinata/thinking_open.png"
    pause renpy.random.uniform(0.2, 0.35)
    repeat

image hinata frustrated_talk:
    "images/characters/hinata/neutral_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/neutral_open.png"
    pause renpy.random.uniform(0.2, 0.25)
    repeat

image hinata worried_talk:
    "images/characters/hinata/worried_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/worried_open.png"
    pause renpy.random.uniform(0.2, 0.3)
    repeat

image hinata neutral_talk:
    "images/characters/hinata/neutral_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/neutral_open.png"
    pause renpy.random.uniform(0.2, 0.25)
    repeat
image hinata smile_talk:
    "images/characters/hinata/smile_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/smile_open.png"
    pause renpy.random.uniform(0.2, 0.25)
    repeat
# Hayashi Talking Animation
image hayashi happy_talk:
    "images/characters/hayashi/happy_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hayashi/happy_open.png"
    pause renpy.random.uniform(0.2, 0.3)
    repeat

image hayashi smile_talk:
    "images/characters/hayashi/smile_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hayashi/smile_open.png"
    pause renpy.random.uniform(0.2, 0.3)
    repeat

image hayashi serious_talk:
    "images/characters/hayashi/serious_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hayashi/serious_open.png"
    pause renpy.random.uniform(0.2, 0.3)
    repeat

image hayashi thinking_talk:
    "images/characters/hayashi/thinking_closed.png"
    pause renpy.random.uniform(0.2, 0.35)
    "images/characters/hayashi/thinking_open.png"
    pause renpy.random.uniform(0.2, 0.35)
    repeat

image hayashi neutral_talk:
    "images/characters/hayashi/neutral_closed.png"
    pause renpy.random.uniform(0.2, 0.35)
    "images/characters/hayashi/neutral_open.png"
    pause renpy.random.uniform(0.2, 0.35)
    repeat
# Kaito Talking Animation
image kaito neutral_talk:
    "images/characters/kaito/neutral_open.png"
    pause renpy.random.uniform(0.2, 0.35)
    "images/characters/kaito/neutral_closed.png"
    pause renpy.random.uniform(0.2, 0.35)
    repeat

# Erika Talking Animation
image erika happy_talk:
    "images/characters/hinata/happy_closed.png"
    pause renpy.random.uniform(0.15, 0.25)  # Random pause between 0.15s - 0.25s
    "images/characters/hinata/happy_open.png"
    pause renpy.random.uniform(0.15, 0.25)
    repeat

image erika thinking_talk:
    "images/characters/hinata/thinking_closed.png"
    pause renpy.random.uniform(0.2, 0.35)
    "images/characters/hinata/thinking_open.png"
    pause renpy.random.uniform(0.2, 0.35)
    repeat

image erika worried_talk:
    "images/characters/hinata/worried_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/worried_open.png"
    pause renpy.random.uniform(0.2, 0.3)
    repeat

image erika neutral_talk:
    "images/characters/hinata/neutral_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/neutral_open.png"
    pause renpy.random.uniform(0.2, 0.25)
    repeat

image erika frustrated_talk:
    "images/characters/hinata/neutral_closed.png"
    pause renpy.random.uniform(0.2, 0.3)
    "images/characters/hinata/neutral_open.png"
    pause renpy.random.uniform(0.2, 0.25)
    repeat
# Hayashi Talk

# Transform

transform slide_slight_left:
    linear 1.0 xalign 0

transform return_to_center:
    linear 0.8 xalign 0.5

transform move_right_to_left:
    xalign 1.4
    linear 1.0 xalign 0.95

transform left_far_mov:
    xpos 0.1
    
transform right_far_mov:
    xpos 0.9


# Define these at the top of your script, before any labels

# Character position transforms
transform at_left_side():
    subpixel True
    xpos 0.26 ypos 1.28 zoom 1.66

transform at_right_side():
    subpixel True
    xpos 0.75 ypos 1.28 zoom 1.66

transform move_forward():
    subpixel True
    zoom 1.66
    ease 1.14 zoom 1.84 ypos 1.37

transform move_backward():
    subpixel True
    zoom 1.66
    ease 1.14 zoom 1.55 zpos -243.0

transform position_left:
    xpos 0.25 xanchor 0.5 ypos 1.28 zrotate 0.0 zoom 1.66

transform position_right:
    xpos 0.75 xanchor 0.5 ypos 1.28 zrotate 0.0 zoom 1.66

transform position_left_far:
    xpos 0.15 xanchor 0.5 ypos 1.1 zrotate 0.0 zoom 1.20

transform position_right_far:
    xpos 0.85 xanchor 0.5 ypos 1.1 zrotate 0.0 zoom 1.20


transform lean_towards(x_initial, y_initial, is_left=True):
    subpixel True
    linear 1.14 pos (
        (x_initial - 0.22 if is_left else x_initial + 0.22),  # Left moves left, Right moves right
        y_initial + 0.09  # Moves slightly upward
    ) zoom 1.84

transform lean_away(x_initial, y_initial, is_left=True):
    subpixel True
    linear 1.14 pos (
        (x_initial + 0.04 if is_left else x_initial - 0.04),  # Left moves slightly right, Right moves slightly left
        y_initial
    ) zoom 1.55 zpos -243.0

transform return_to_neutral_left:
    linear 0.8 xpos 0.25 ypos 1.28 zoom 1.66

transform return_to_neutral_right:
    linear 0.8 xpos 0.25 ypos 1.28 zoom 1.66


transform zoom_face_left:
    subpixel True
    matrixtransform IdentityMatrix()  # Resets any previous transformations
    linear 0.8 xpos -0.2 ypos 1.50 zoom 2 yrotate 18.0 zrotate 7.0

# CHARACTER MOVEMENT FUNCTIONS
init python:
    def position_character(char, position):
        """Place a character in a fixed position (left or right) with consistent size"""
        if position == "left":
            renpy.show(char, at_list=[position_left])  # Zoom is already included in ATL
        else:
            renpy.show(char, at_list=[position_right])

        renpy.pause(0.5)

    def reset_to_neutral_smooth(char, side):
        """Smoothly reset a character's position back to their neutral position using ATL."""
        if side == "left":
            renpy.show(char, at_list=[return_to_neutral_left])
        else:
            renpy.show(char, at_list=[return_to_neutral_right])

        renpy.pause(0.8)

    def zoom_character_face(char, side):
        """Smoothly zoom in on a character's face without changing their given position."""
        if side == "left":
            renpy.show(char, at_list=[zoom_face_left])


        renpy.pause(0.8)
    def ease_character_to_position(char, start_pos, end_pos, transition_time=1.15):
        left_pos = (0.26, 1.28)
        right_pos = (0.75, 1.28)
        
        start_pos = left_pos if start_pos == "left" else right_pos
        end_pos = left_pos if end_pos == "left" else right_pos

        renpy.show(char, at_list=[Position(xpos=start_pos[0], ypos=start_pos[1]), easein(transition_time, xpos=end_pos[0], ypos=end_pos[1])])
        renpy.pause(transition_time)

    def character_lean(char, direction, x_initial, y_initial):
        """Lean a character forward or backward dynamically based on their position"""
        is_left = x_initial < 0.5  # Determine if character is on the left side

        if direction == "forward":
            renpy.show(char, at_list=[lean_towards(x_initial, y_initial, is_left)])
        else:
            renpy.show(char, at_list=[lean_away(x_initial, y_initial, is_left)])

        renpy.pause(1.14)

# Transform definitions for smooth animation
transform transform_hayashi_intro:
    subpixel True
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0) * OffsetMatrix(1269.0, 0.0, 0.0)
    linear 0.64 matrixtransform ScaleMatrix(1.0, 1.0, 1.0) * OffsetMatrix(450.0, 0.0, 0.0) zoom 1.12

transform transform_hayashi_final:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0) * OffsetMatrix(450.0, 0.0, 0.0) zoom 1.12


transform character_base_pose:
    subpixel True
    xpos 0.5  # center
    ypos 0.2
    zoom 0.60
    # matrixtransform OffsetMatrix(0.0, 495.0, 0.0)

transform character_base_pose_left:
    subpixel True
    xpos 0.1  # center
    ypos 0.2
    zoom 0.60
    # matrixtransform OffsetMatrix(0.0, 495.0, 0.0)

transform character_base_pose_left_mai:
    subpixel True
    xpos 0.1  # center
    ypos 0.1
    zoom 0.60
    # matrixtransform OffsetMatrix(0.0, 495.0, 0.0)
transform character_center_zoom_mai:
    subpixel True
    xpos 0.23  # center
    zoom 0.75
    # matrixtransform OffsetMatrix(0.0, 495.0, 0.0)

transform character_base_pose_right_eren:
    subpixel True
    xpos 0.5  # center
    ypos 0.1
    zoom 0.60
    # matrixtransform OffsetMatrix(0.0, 495.0, 0.0)
transform character_center_zoom_eren:
    subpixel True
    xpos 0.25  # center
    ypos 0.05
    zoom 0.80
    # matrixtransform OffsetMatrix(0.0, 495.0, 0.0)

transform slide_pos:
    subpixel True pos (0.1, 0.16) yzoom 0.98 zoom 0.63 

transform slide_pos2:
    subpixel True pos (0.1, 0.16) zoom 0.45 

transform flashback_effect_1:
    blur 4.0
    matrixcolor InvertMatrix(0.0) * ContrastMatrix(2.5) * SaturationMatrix(0.27)

    
transform slide_pos3:
    subpixel True pos (0.1, 0.17) yzoom 0.98 zoom 1.32