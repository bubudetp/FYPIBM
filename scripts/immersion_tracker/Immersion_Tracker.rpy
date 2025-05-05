init -999 python:
    class ImmersionTracker:
# ------------------------------------------------------------------------ ImmersionTracker Class
        def __init__(self):
            self.dimensions = {
                "curitosity": 0.0,
                "concentration": 0.0,
                "challenge": 0.0,
                "control": 0.0,
                "comprehension": 0.0,
                "empathy": 0.0,
                "familiarity": 0.0
            }
        
        def update(self, node, choice=None):
            for dim in self.dimensions:
                self.dimensions[dim] = getattr(node, dim, 0)

                if choice == "explorative":
                    self.dimensions[dim] += 0.1

    class EmotionalProfile:
# ------------------------------------------------------------------------ EmotionalProfile Class
        def __init__(self):
            self.transportation = 0.0
            self.mental_imagery = 0.0
            self.character_empathy = {}
        
        def apply_effect(self, node):
            self.transportation += node.story_node.emotion.get("transport", 0)
            self.mental_imagery += node.story_node.emotion.get("imagery", 0)

            for char, intensity in node.story_node.character_interactions.items():
                self.character_empathy[char] = self.character_empathy.get(char, 0) + intensity
        
        