init -999 python:
    from collections import OrderedDict
    class StoryArc:
# ------------------------------------------------------------------------ StoryArc Class
        def __init__(self, arc_id, title):
            self.arc_id = arc_id
            self.title = title
            self.flowchart = None
            self.unlocked = False
            self.completion = 0.0
            self.thumbnail = None
            self.description = ""
            self.start_label = ""
    
    class FlowchartManager:
# ------------------------------------------------------------------------ FlowchartManager Class
        def __init__(self):
            self.arcs = OrderedDict()
            self.current_arc = None  # ID of currently active arc
            self.current_arc_index = 0  # Position in ordered dict
            self.global_completion = 0.0
            self.player_path = [] 
        
        def register_arc(self, arc_id, title, flowchart_init_func, **kwargs):
            print("adding story to flowchart manager", self)
            arc = StoryArc(arc_id, title)
            arc.flowchart = flowchart_init_func()
            arc.thumbnail = kwargs.get("thumbnail", None)
            arc.description = kwargs.get("description", "")
            self.arcs[arc_id] = arc
            if len(self.arcs) == 1:
                arc.unlocked = True
                self.current_arc = arc_id
            self.arcs[arc_id].start_label = kwargs.get("start_label", None)
        
        def get_current_flowchart(self):
            return self.arcs[self.current_arc].flowchart
        
        def mark_node_visited(self, node_id, arc_id = None):
            arc_id = arc_id or self.current_arc
            clean_id = node_id.replace(f"{arc_id}_", "")
            self.player_path.append((arc_id, clean_id))
        
        def calculate_global_progress(self):
            total = sum(arc.flowchart.calculate_completion() for arc in self.arcs.values())
            self.global_completion = total / len(self.arcs)
            return self.global_completion

        def get_current_arc(self):
            """Get the current arc object"""
            return self.arcs.get(self.current_arc)
    
        def get_arc_by_id(self, arc_id):
            """Get specific arc by ID"""
            return self.arcs.get(arc_id)
        
        def get_current_flowchart(self):
            """Get flowchart of current arc"""
            current = self.get_current_arc()
            return current.flowchart if current else None
        
        def get_arc_progress(self, arc_id=None):
            """Get completion percentage for an arc"""
            arc = self.get_current_arc() if arc_id is None else self.get_arc_by_id(arc_id)
            return arc.calculate_completion() if arc else 0.0

        
        def unlock_arc(self, arc_id, switch_to_it=True):
            """Unlock an arc and optionally switch to it"""
            if arc_id not in self.arcs:
                return False
                
            self.arcs[arc_id].unlocked = True
            
            # If requested, switch to this arc
            if switch_to_it:
                self.switch_arc(arc_id)
                
            # Special case: if this was the next sequential arc after current,
            # auto-switch to it (like a story progression)
            arc_keys = list(self.arcs.keys())
            current_idx = arc_keys.index(self.current_arc) if self.current_arc else -1
            new_idx = arc_keys.index(arc_id)
            
            if new_idx == current_idx + 1:
                self.switch_arc(arc_id)
                
            return True

        def switch_arc(self, arc_id):
            """Switch to the specified arc if unlocked"""
            if arc_id not in self.arcs or not self.arcs[arc_id].unlocked:
                return False
                
            self.current_arc = arc_id
            self.current_arc_index = list(self.arcs.keys()).index(arc_id)
            return True

        def get_next_arc_id(self):
            """Get the ID of the next arc in sequence (whether unlocked or not)"""
            keys = list(self.arcs.keys())
            if self.current_arc_index + 1 < len(keys):
                return keys[self.current_arc_index + 1]
            return None

        def unlock_next_arc(self):
            """Unlock and switch to the next arc in sequence"""
            next_id = self.get_next_arc_id()
            if next_id:
                return self.unlock_arc(next_id, switch_to_it=True)
            return False
        @property
        def unlocked(self):
            return self._unlocked or check_arc_unlocked(self.arc_id)
        
        @unlocked.setter
        def unlocked(self, value):
            self._unlocked = bool(value)

    
    
default persistent.drawn_pairs = set()
default persistent.relationships_stats = {}


init -998 python:
    import renpy.store as store
    store.flowchart_manager = FlowchartManager()
    store.immersion_tracker = ImmersionTracker()
    store.emotional_profile = EmotionalProfile()
# ------------------------------------------------------------------------ Arc Registration FlowchartManager
    def register_all_arcs():
        flowchart_manager = store.flowchart_manager

        print(flowchart_manager, "prinitng")
        flowchart_manager.register_arc(
            "act1", 
            "Act 1: Foundations",
            init_act1_flowchart,
            thumbnail="home_day",
            description="The beginning of your AI Academy journey",
            start_label="start"
        )

        flowchart_manager.register_arc(
            "act2", 
            "Act 2: Determination",
            init_act2_flowchart,
            thumbnail="shopping_street_day",
            description="The beginning of your AI Academy journey",
            start_label="scene2d"
        )

        flowchart_manager.register_arc(
            "act3", 
            "Act 3: Isolation",
            init_act3_flowchart,
            thumbnail="classroom_night",
            description="Confronting absence and system mysteries",
            start_label="scene3_1_5"
        )
        flowchart_manager.register_arc(
            "act3_quiz", 
            "Act 3: Framework Quiz",
            init_act3_quiz_flowchart,
            thumbnail="classroom_quiz",
            description="Deep learning framework knowledge test",
            start_label="scene3_3"
        )
        print(flowchart_manager.arcs["act1"].start_label, "printing arcs")

        print("Registered Act 1 Flowchart")
        
        # flowchart_manager.register_arc(
        #     "act2",
        #     "Act 2: Complications",
        #     init_act2_flowchart,
        #     thumbnail="home_night",
        #     description="Advanced challenges and team dynamics"
        # )

        # flowchart_manager.register_arc(
        #     "act3",
        #     "Act 3: Complications",
        #     init_act3_flowchart,
        #     thumbnail="home_night",
        #     description="Advanced challenges and team dynamics"
        # )

        # flowchart_manager.register_arc(
        #     "act4",
        #     "Act 4: Complications",
        #     init_act4_flowchart,
        #     thumbnail="home_night",
        #     description="Advanced challenges and team dynamics"
        # )
    
    register_all_arcs()
    print("Registered all arcs before")