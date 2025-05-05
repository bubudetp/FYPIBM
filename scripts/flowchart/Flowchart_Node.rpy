init -999 python:
    class StoryNode:
            def __init__(self, 
                        curitosity=0, concentration=0, challenge=0, control=0, 
                        comprehension=0, empathy=0, familiarity=0,
                        emotion=None, character_interactions=None):
                self.curitosity = curitosity
                self.concentration = concentration
                self.challenge = challenge
                self.control = control
                self.comprehension = comprehension
                self.empathy = empathy
                self.familiarity = familiarity
                self.emotion = emotion or {}
                self.character_interactions = character_interactions or {}

# ------------------------------------------------------------------------ FlowchartNode Class
    class FlowchartNode:
        def __init__(self, id, label, title, x, y, major=False, subtitle=None, completion_rate=None,
                    node_type=None, thumbnail=None, story_node=None):
            
            self.id = id
            self.label = label
            self.title = title
            self.x = x
            self.y = y
            self.major_event = major
            self.subtitle = subtitle
            self.completion_rate = completion_rate
            self.node_type = node_type
            self.visited = False
            self.connections = []
            self.thumbnail = thumbnail
            self.choice_impacts = {}
            self.feedback_delay = 1.5
            self.story_node = story_node or StoryNode()

            
        def add_connection(self, target_id, connection_type=None, choice_data=None):
            """Add a connection with optional connection type"""
            connection = {
                "target": target_id,
                "type": connection_type or "normal",
                "choice_data": choice_data or {}
            }

            self.connections.append(connection)
        
        # def get_choice_impact(self, choice_index):
        #     if len(self.connections) > choice_index:
        #         data = self.connections[choice_index].get("choice_data", {})
        #         if data:
        #             icons = {
        #                 "knowledge": "gui/knowledge_icon.png",
        #                 "relationships": "gui/relationship_icon.png",
        #                 "difficulty": "gui/difficulty_icon.png"
        #             }
        #             return (
        #                 f"{icons.get(data["impact_type"], "")}"
        #                 f"{data.get("feedback_text", "")}"
        #             )