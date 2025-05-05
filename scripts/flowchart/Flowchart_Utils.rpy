init -102 python:
    arc_unlock_conditions = {}

# ------------------------------------------------------------------------ Flowchart Utility Functions
    # def init_act2_flowchart():
    #     flowchart = Flowchart("AI Academy Story - Act 2")
    #     # Position constants for Act 2
    #     ACT2_COL_SPACING = 320
    #     ACT2_ROW_SPACING = 160
        
    #     nodes = [
    #         FlowchartNode(id="start", title="NEW SEMESTER", label="act2_start", 
    #                     x=200, y=300, arc_id="act2", major=True),
    #         # [More Act 2 nodes...]
    #     ]
        
    #     for node in nodes:
    #         flowchart.add_node(node)
            
    #     # [Add connections...]
    #     return flowchart
    def calculate_progression(flowchart):
            """Calculate completion percentage based on dynamic paths"""
            current_path = progression_paths.get(flowchart.name, [])
            if not current_path or not flowchart.current_node:
                return 0
                
            # Check if current node is in path
            try:
                current_index = current_path.index(flowchart.current_node)
                return int((current_index + 1) * 100 / len(current_path))
            except ValueError:
                # Find the furthest completed node in path
                last_completed = -1
                for i, node in enumerate(current_path):
                    if node in flowchart.visited_nodes:
                        last_completed = i
                return int((last_completed + 1) * 100 / len(current_path)) if last_completed >= 0 else 0
    def calculate_dynamic_progression(flowchart, path):
        """Calculate progress using the provided path"""
        if not path:
            return 0
            
        # Find current position in path
        try:
            current_index = path.index(flowchart.current_node)
            return int((current_index + 1) * 100 / len(path))
        except ValueError:
            # Find last completed node in path
            completed = [i for i, node in enumerate(path) if node in flowchart.visited_nodes]
            return int((max(completed) + 1) * 100 / len(path)) if completed else 0
    def add_progression_path(flowchart_id, path):
            progression_paths[flowchart_id] = path

    def check_arc_unlocked(arc_id):
        if arc_id not in arc_unlock_conditions:
            return False
        condition = globals().get(arc_unlock_conditions[arc_id])
        return condition() if condition else False
    def requires_nodes(arc_id, required_nodes, operation="OR"):
        """Check if nodes were visited in another arc"""
        source_arc = arc_id.split('_')[0]
        
        for node in required_nodes:
            if operation == "OR":
                return any(node_id in flowchart_manager.arcs[source_arc].flowchart.visited_nodes for node_id in required_nodes)
            if operation == "AND":
                return all(node_id in flowchart_manager.arcs[source_arc].flowchart.visited_nodes for node_id in required_nodes)

    def requires_percentage(arc_id, min_percentage):
        source_arc = arc_id.split('_')[0]
        if source_arc not in flowchart_manager.arcs:
            return False
            
        # Calculate completion if not already cached
        if not hasattr(flowchart_manager.arcs[source_arc], 'completion'):
            flowchart_manager.calculate_global_progress()
            
        return flowchart_manager.arcs[source_arc].completion >= min_percentage

# ------------------------------------------------------------------------------------------------- Flowchart Unlock Utility Functions
    def register_unlock_condition(arc_id, condition):
        arc_unlock_conditions[arc_id] = condition
        globals()[condition.__name__] = condition
    def unlock_act1():
        return True
    def unlock_act2():
        return flowchart_manager.arcs["act1"].completion >= 100
    def unlock_act3():
        return requires_percentage("act2_act3", 70)
    
    # Register all arcs and their unlock conditions
    register_unlock_condition("act1", unlock_act1)
    register_unlock_condition("act2", unlock_act2)
    register_unlock_condition("act3", unlock_act3)

    # Scene Immersion and Emotion Wrapper Application
    def apply_scene_immersion(node_id):
        arc_id = node_id.split("_")[0] if "_" in node_id else flowchart_manager.current_arc
        node = flowchart_manager.arcs[arc_id].flowchart.nodes.get(node_id)
        if node and node_id not in flowchart_manager.arcs[arc_id].flowchart.visited_nodes:
            immersion_tracker.update(node)
            emotional_profile.apply_effect(node)
            
# ------------------------------------------------------------------------ Flowchart Main Label
label update_flowchart_status(node_id):
    python:
        # Auto-detect arc if not specified
        if "_" in node_id:
            arc_id = node_id.split("_")[0]
            if arc_id not in flowchart_manager.arcs:
                arc_id = flowchart_manager.current_arc
        else:
            print("i am here, after defining the flowchart manager in a python block in -998, my value is ", flowchart_manager)
            arc_id = flowchart_manager.current_arc

        flowchart = flowchart_manager.arcs[arc_id].flowchart
        clean_id = node_id.replace(f"{arc_id}_", "")
        node = flowchart.nodes.get(clean_id)

        prev_node = flowchart.current_node

        # If first time visiting, apply immersion and emotion effects
        if clean_id not in flowchart.visited_nodes and node:
            immersion_tracker.update(node)
            emotional_profile.apply_effect(node)

        # Update visit state
        flowchart_manager.mark_node_visited(node_id, arc_id)
        flowchart.set_current(clean_id)
        flowchart.mark_visited(clean_id)

        # Track visited path if coming from another node
        if prev_node and prev_node != clean_id:
            flowchart.mark_path_visited(prev_node, clean_id)

        # Check arc unlocks
        for check_arc_id, arc in flowchart_manager.arcs.items():
            if not arc.unlocked and arc.unlocked:
                arc._unlocked = True
                renpy.notify(f"New Arc Unlocked: {arc.title}")
                if arc_id == "act1" and clean_id == "scene2d_transition":
                    renpy.show_screen("arc_unlock_notification", arc.title, arc.thumbnail)

        # Update completion percentages
        flowchart_manager.calculate_global_progress()

        if config.developer:
            print(f"Updated node: {clean_id} in {arc_id}")
            print(f"Current unlocked arcs: {[a for a in flowchart_manager.arcs.values() if a.unlocked]}")

    return

    # ------------------------------------------------------------------------ Style Functions
init -100 python early:

    def get_node_style(node, current_node_id):
        # Base style properties
        bg_color = "#1a3e6c"  # Default blue background
        border_color = "#3a7bbd"
        text_color = "#ffffff"
        width = 220 if node.major_event else 180
        height = 60 if node.major_event else 40
        
        # Modify appearance based on node type
        if node.node_type == "warning":
            bg_color = "#8b2e2e"  # Red for warnings
            border_color = "#d13838"
        elif node.node_type == "info":
            bg_color = "#2e648b"  # Blue for info
            border_color = "#38a9d1"
            
        # Highlight current node
        if node.id == current_node_id:
            border_color = "#ffffff"
            bg_color = "#2a5694"  # Brighter blue
            
        # Dim unvisited nodes
        if not node.visited:
            bg_color = darken_color(bg_color, 0.5)
            border_color = darken_color(border_color, 0.5)
            text_color = "#aaaaaa"
            
        return {
            "bg_color": bg_color,
            "border_color": border_color,
            "text_color": text_color,
            "width": width,
            "height": height
        }
    def darken_color(hex_color, factor):
        # Convert hex to RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        
        # Darken
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"