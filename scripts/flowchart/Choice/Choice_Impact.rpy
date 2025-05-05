init -590 python:
    class ChoiceImpact:
        def __init__(self,
                    affected_characters=None,
                    knowledge_requirements=None,
                    future_branch_changes=None,
                    stat_changes=None,
                    flags_to_set=None,
                    outcome_changes=None,
                    immersion_effects=None,
                    emotion_effects=None):
                        
            self.affected_characters = affected_characters or []
            self.knowledge_requirements = knowledge_requirements or []
            self.future_branch_changes = future_branch_changes or {}
            self.stat_changes = stat_changes or {}
            self.flags_to_set = flags_to_set or []
            self.outcome_changes = outcome_changes or {}
            self.immersion_effects = immersion_effects or {}
            self.emotion_effects = emotion_effects or {}

        def apply(self):
            for char in self.affected_characters:
                increase_rel(char, 1)

            for stat, val in self.stat_changes.items():
                increase_stat(stat, val)

            for flag in self.flags_to_set:
                set_flag(flag)

            for outcome_key, value in self.outcome_changes.items():
                set_outcome(outcome_key, value)

            for dim, val in self.immersion_effects.items():
                immersion_tracker.dimensions[dim] += val

            for char, val in self.emotion_effects.items():
                emotional_profile.character_empathy[char] = \
                    emotional_profile.character_empathy.get(char, 0) + val
            
            print("Applying choice impact:")
            print(f"Characters: {self.affected_characters}")
            print(f"Knowledge: {self.knowledge_requirements}")
            print(f"Branches: {self.future_branch_changes}")
            print(f"Stats: {self.stat_changes}")
            print(f"Flags: {self.flags_to_set}")
            print(f"Outcomes: {self.outcome_changes}")
            print(f"Immersion: {self.immersion_effects}")
            print(f"Emotion: {self.emotion_effects}")

        def serialize(self):
            return {
                "characters": list(self.affected_characters),
                "knowledge": list(self.knowledge_requirements),
                "branches": dict(self.future_branch_changes),
                "stats": dict(self.stat_changes),
                "flags": list(self.flags_to_set),
                "outcomes": dict(self.outcome_changes),
                "immersion": dict(self.immersion_effects),
                "emotion": dict(self.emotion_effects),
            }
