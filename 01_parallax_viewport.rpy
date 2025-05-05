################################################################################
##
## Parallax Viewport for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for a parallax displayable in Ren'Py. There is both
## a CDD to handle the rendering of the viewport, and a screen language keyword
## so it can be easily declared in-game.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the other file,
## parallax_vp_examples.rpy! This is just the backend; you don't need to
## understand everything in this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_parallax_viewport.rpy", None)
    build.classify("**01_parallax_viewport.rpyc", "archive")
################################################################################
init -100 python early:

    class ParallaxVP(renpy.display.viewport.Viewport):
        """
        A special viewport that will scroll its children in parallax based
        on their sizes. Inherits from the built-in Viewport.
        """
        def render(self, width, height, st, at):
            ## This initial setup is as per the Viewport class
            self.width = width
            self.height = height

            child_width = self.child_width or width
            child_height = self.child_height or height

            surf = renpy.render(self.child, child_width, child_height, st, at)

            cw, ch = surf.get_size()
            cxo, cyo, width, height = self.update_offsets(cw, ch, st)

            self.offsets = [ (cxo, cyo) ]

            rv = renpy.Render(width, height)
            xoffset = self.xadjustment.value if self.xadjustment else 0

            ## Get the size of each child to determine its offset
            for child in self.child.children:
                child_render = child.render(width, height, st, at)
                # pct_xscrolled = self.xadjustment.value / max(self.xadjustment.range, 1.0)
                # pct_yscrolled = self.yadjustment.value / max(self.yadjustment.range, 1.0)
                # child_w, child_h = child_render.get_size()
                # ## What's the end position for this layer?
                # ## Ergo we should be offset end_x * pct_xscrolled
                # new_xo = ((width - child_w) * pct_xscrolled)
                # ## And the same for y
                # new_yo = ((height - child_h) * pct_yscrolled)

                # ## Prevent flickering
                # child_render.xclipping = False
                # child_render.yclipping = False
                ## Keep the smaller layers on-screen
                # rv.blit(child_render, (new_xo, new_yo))
                rv.blit(child_render, (-xoffset, 0))

            rv = rv.subsurface((0, 0, width, height), focus=True)

            if self.draggable or self.arrowkeys:
                rv.add_focus(self, None, 0, 0, width, height)

            return rv

    renpy.register_sl_displayable("parallax_viewport", ParallaxVP, 'viewport', 1,
        replaces=True, pass_context=True,
    ).add_property("child_size"
    ).add_property("mousewheel"
    ).add_property("arrowkeys"
    ).add_property("pagekeys"
    ).add_property("draggable"
    ).add_property("edgescroll"
    ).add_property("xadjustment"
    ).add_property("yadjustment"
    ).add_property("xinitial"
    ).add_property("yinitial"
    ).add_property("scrollbars"
    ).add_property("spacing"
    ).add_property("transpose"
    ).add_property("xminimum"
    ).add_property("yminimum"
    ).add_property_group("position",
    ).add_property_group("ui",
    )

init python:
    flow_data = [
        { "id": "start", "label": "Mission Start", "pos": (0, 200), "jump": "label_start", "unlocked": True },
        { "id": "talk", "label": "Talk to Capt. Allen", "pos": (300, 200), "jump": "label_talk", "unlocked": True },
        { "id": "save_fish", "label": "Save Fish", "pos": (600, 100), "jump": "label_save_fish", "unlocked": False },
        { "id": "leave_fish", "label": "Leave Fish", "pos": (600, 300), "jump": "label_leave_fish", "unlocked": False },
    ]

    flow_links = [
        ("start", "talk"),
        ("talk", "save_fish"),
        ("talk", "leave_fish"),
    ]

    def get_node_by_id(node_id):
        for node in flow_data:
            if node["id"] == node_id:
                return node
        return None


init python:

    class AnimateScroll(Scroll):
        """
        A subclass of the Scroll action which takes a warper for the
        scrolling time.

        Notably, it also takes the following values for amount besides
        "page" and "step":
            "max" - Scrolls to the end of the viewport
            "min" - Scrolls to the start of the viewport
            "toggle" - Scrolls to the end if not already there, and to the start
                if it is.
        """
        def __init__(self, id, direction, amount="step", delay=0.0, warper="ease"):
            ## 7.5 compatibility
            try:
                super(AnimateScroll, self).__init__(id, direction, amount, delay)
            except TypeError:
                super(AnimateScroll, self).__init__(id, direction, amount)
                self.delay = 0.0
            self.warper = warper

        def get_adjustment_and_delta(self):
            d = renpy.get_widget(None, self.id)
            if d is None:
                return None, +1


            if self.direction == "increase":
                delta = +1
                adjustment = d.adjustment
            elif self.direction == "decrease":
                delta = -1
                adjustment = d.adjustment
            elif self.direction == "horizontal increase":
                delta = +1
                adjustment = d.xadjustment
            elif self.direction == "horizontal decrease":
                delta = -1
                adjustment = d.xadjustment
            elif self.direction == "vertical increase":
                delta = +1
                adjustment = d.yadjustment
            elif self.direction == "vertical decrease":
                delta = -1
                adjustment = d.yadjustment
            elif self.direction is None:
                if self.amount == "toggle":
                    adjustment = d.adjustment
                elif self.amount == "vertical toggle":
                    adjustment = d.yadjustment
                elif self.amount == "horizontal toggle":
                    adjustment = d.xadjustment
                else:
                    raise Exception("Unknown scroll direction: {}".format(self.direction))

                if adjustment.value == adjustment.range:
                    delta = -1
                else:
                    delta = +1
            else:
                raise Exception("Unknown scroll direction: {}".format(self.direction))

            return adjustment, delta

        def __call__(self):

            adjustment, delta = self.get_adjustment_and_delta()

            if adjustment is None:
                raise Exception("There is no displayable with the id {}.".format(self.id))

            if self.amount == "step":
                amount = delta * adjustment.step
            elif self.amount == "page":
                amount = delta * adjustment.page
            elif self.amount == "max":
                ## Max/min use range for safety
                amount = adjustment.range
            elif self.amount == "min":
                amount = -adjustment.range
            elif self.amount in ("horizontal toggle", "vertical toggle", "toggle"):
                if adjustment.value == adjustment.range:
                    amount = -adjustment.range
                else:
                    amount = adjustment.range
            else:
                ## <8.2 compatibility
                try:
                    amount = absolute.compute_raw(delta*self.amount, adjustment.range)
                except:
                    if isinstance(self.amount, float) and not isinstance(self.amount, absolute):
                        amount = delta * self.amount * adjustment.range
                    else:
                        amount = delta * self.amount

            if self.delay == 0.0:
                if self.amount in ("max", "min"):
                    adjustment.change(amount)
                else:
                    adjustment.change(adjustment.value + amount)
            else:
                adjustment.animate(amount, self.delay, renpy.atl.warpers[self.warper])

style vparallax_fixed:
    xfit True yfit True