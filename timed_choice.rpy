# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Timed Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The first parameter, (items), is a list of objects, each with caption
## and action fields.
## With the additional functionality of timed choices, it also take optional
## parameters, (time), how long the timer will last, and (timeout), the name of the
## label to jump to if the timer runs out.
##
## https://cuteshadow.itch.io/renpy-timed-choice-menu
##
## This is a random example of how to make a timed choice. If you wanted to
## make an un-timed choice then just write menu: without the extra stuff as
## you would've done before.
##
# label chapter1:
#     yuu "I hate surprises..."

#     menu(time=10.5, timeout="left_her_hanging"):
#         e "Do you love me?"

#         "Yes":
#            "I do love you."

#         "No":
#            "I just don't feel like that."

#    "The end."

#    return


# label left_her_hanging:
#    e "Your silence says it all."

#    "The end."

#    return


# This setting multiplies the choice timer's speed.
# For example, setting it to 2.0 will make the timer
# go twice as fast.
# Feel free to let you players adjust this setting.
#
# Do not set this number to 0.
#
# bar style "slider" value FieldValue(persistent, "timed_choice_speed", min=0.1, max=1.0)
default persistent.timed_choice_speed = 1.0

# This setting enables choice timers for the
# entire game.
# Feel free to let your players adjust this setting.
#
# textbutton "Toggle Timed Choices" action ToggleField(persistent, "timed_choice_enabled")
default persistent.timed_choice_enabled = True

# If the player has disabled timed choices using
# the above setting, they will be given an
# alternative choice which would do the same
# thing as if they let the timer run down.
#
# This variable controls what that choice will say.
# If you set it to None then no alternative choice
# will appear.
define gui.timed_choice_timeout_alt_msg = "..."

# This is the hex color of the timer bar when it
# isn't filled in.         
# I suggest a darker color. 
define gui.timed_choice_timer_bar_under_color = gui.muted_color

# This is the hex color of the timer bar when it
# is filled in.         
# I suggest a brighter color. 
define gui.timed_choice_timer_bar_fill_color = gui.accent_color

# This is the width of the timer bar in pixels.
define gui.timed_choice_timer_bar_width = gui.choice_button_width/2

# This is the height of the timer bar in pixels.
define gui.timed_choice_timer_bar_height = 10


# This is a quick python function to check you have included
# both the time and timeout inputs.
# Otherwise, it will kindly remind you of your mistake.
init python:
    def timed_choice_has(time, timeout):
        if time and not timeout:
            raise TypeError("You included a time for the timed choice screen but didn't specify the timeout label.")
        
        elif not time and timeout:
            raise TypeError("You included a timeout label for the timed choice screen but didn't specify an appropriate time amount.")

        else:
            return time and timeout

# This is the modified choice screen that allows for timed choices.
# Please delete or rename the old choice screen as this will replace it
# completely.
screen choice(items, time=None, timeout=None):
    style_prefix "choice"

    # Check that you have included both inputs or neither.
    default timed_choice = timed_choice_has(time, timeout)

    # Set up the timer if it is appropriate to do so.
    if timed_choice and persistent.timed_choice_enabled:
        # Adjust the total time by the speed setting.
        default adjusted_time = time * (1 / persistent.timed_choice_speed)

        # Set a finish flag.
        default timer_finished = False

        if not timer_finished:  
            # If the timer has not finished then wait.
            timer adjusted_time action SetScreenVariable("timer_finished", True)
        else:
            # The player took too long.
            timer 0.01 action Jump(timeout)

    # Show the list of choices.
    vbox:
        # The choices.
        for i in items:
            textbutton i.caption action i.action

        # Add an equivalent button to timing out if timed choices are disabled.
        if timed_choice and not persistent.timed_choice_enabled and gui.timed_choice_timeout_alt_msg:
            textbutton "[gui.timed_choice_timeout_alt_msg]" action Jump(timeout)

        # The timer visual.
        if timed_choice and persistent.timed_choice_enabled:
            use timed_choice_visual(adjusted_time)


# This is a simple visual indicating how much
# time is left on the timer.
screen timed_choice_visual(adjusted_time):

    fixed:
        xsize int(gui.timed_choice_timer_bar_width) 
        ysize int(gui.timed_choice_timer_bar_height)
        xalign 0.5
        
        # The timer bar is not filled.
        add Solid(gui.timed_choice_timer_bar_under_color) 

        # The timer bar when it is filled.
        # It will shrink to the middle until the timer has run out.
        add Solid(gui.timed_choice_timer_bar_fill_color):
            at transform:
                xalign 0.5
                xzoom 1.0
                linear adjusted_time xzoom 0.0
