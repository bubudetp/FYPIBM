init python:
    cool_matrix = InvertMatrix(1.05) * ContrastMatrix(1.02) * SaturationMatrix(1.0) * BrightnessMatrix(0.0) * HueMatrix(0.0)
    
    def apply_cool_effect(overlay_image=None):
        # Apply matrix effect to master layer
        renpy.show_layer_at(Transform(matrixcolor=cool_matrix), layer='master')
        
        # Show overlay image if provided, with effect pre-applied
        if overlay_image:
            renpy.show(overlay_image, at_list=[Transform(matrixcolor=cool_matrix)], layer='transient')
        
        # Play sound effects
        renpy.play("death_sound.wav")
        renpy.play("respawn_sound.wav")
        
        renpy.restart_interaction()
    
    def reset_camera_effect():
        # Use an empty list instead of None
        renpy.show_layer_at([], layer='master')
        renpy.show_layer_at([], layer='transient')
        renpy.restart_interaction()