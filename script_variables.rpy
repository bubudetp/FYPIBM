# Initialize all possible branch tracking variables
default branch_data = {
    "relationships": {
        "hayashi": 0,
        "eren": 0,
        "mai": 0,
        "jennie": 0
    },
    "stats": {
        "remembering": 0,
        "glitches": 0,
        "reflection_score": 0,
        "lesson_progress": 0,
        "physics_skill": 0,
        "ml_skill": 0,
        "deterministic_systems_skill": 0,
        "probability_skill": 0,
        "ml_intro_skill": 0,
        "supervised_learning_skill": 0,
        "unsupervised_learning_skill": 0,
        "reinforcement_learning_skill": 0,
        "training_nn_skill": 0,
        "deep_learning_frameworks_skill": 0,
        "decision_tree_skill": 0,
        "curiosity": 0,
        "empathy": 0,
        "comprehension": 0,
        "trust_level": 0,
        "resilience": 0,
        "deviation_level": 0,
        "memory_fragments_collected": 0,
        "decision_clarity": 0,
        "glitch_resistance": 0
    },
    "flags": {
        "visited_clubroom": False,
        "deviant_path": False,
        "forest_flag": False,
        "walked_with_mai": False,
        "jennie_friend": None,
        "asked_to_sit": False,
        "helped_eren_search": False,
        "helped_mai_sketchbook": False,
        "eren_absent_next_scenes": False,
        "mai_absent_next_scenes": False,
        "eren_search_fail": False,
        "eren_search_success": False,
        "mai_search_fail": False,
        "mai_search_success": False,
        "kuma_final_quiz_passed": False,
        "saved_eren": False,
        "saved_mai": False,
        "saved_jennie": False,
        "hayashi_disappeared": False,
        "found_secret_message": False,
        "remembered_disappeared_character": False,
        "glitched_out": False,
        "reflection_perfect": False
    },
    "outcomes": {
        "forest_path_outcome": "unset",
        "deterministic_systems_outcome": "unset",
        "ml_types_outcome": "unset",
        "probability_and_classifiers_outcome": "unset",
        "neural_networks_outcome": "unset",
        "deep_learning_frameworks_outcome": "unset",
        "classifier_quiz_outcome": "unset",
        "kuma_final_quiz_outcome": "unset",
        "mai_storyline_outcome": "unset",
        "eren_storyline_outcome": "unset",
        "jennie_storyline_outcome": "unset",
        "system_stability_outcome": "unset",
        "final_reflection_outcome": "unset",
        "final_quiz_outcome": "unset",
    },
    "text_vars": {
        "insight": "",
        "self_model": "",
        "walk_response": ""
    }
}
init python:
    # Helper functions for cleaner access
    def rel(name, value=None):
        if value is not None:
            branch_data["relationships"][name] = value
        return branch_data["relationships"].get(name, 0)

    def stat(name, value=None):
        if value is not None:
            branch_data["stats"][name] = value
        return branch_data["stats"].get(name, 0)

    def flag(name, value=None):
        if value is not None:
            branch_data["flags"][name] = value
        return branch_data["flags"].get(name, False)

    def outcome(name, value=None):
        if value is not None:
            branch_data["outcomes"][name] = value
        return branch_data["outcomes"].get(name, "")
    # Helper functions for modifying data
    def increase_rel(name, amount=1):
        """Increase a relationship value by the specified amount (default 1)"""
        current = rel(name)
        rel(name, current + amount)
        return current + amount

    def increase_stat(name, amount=1):
        """Increase a stat value by the specified amount (default 1)"""
        current = stat(name)
        stat(name, current + amount)
        return current + amount

    def set_flag(name, value=True):
        """Set a flag to a specific value (default True), and create it if missing"""
        if name not in branch_data["flags"]:
            branch_data["flags"][name] = value
        else:
            branch_data["flags"][name] = value
        return value

    def set_outcome(name, value):
        """Set an outcome to a specific value"""
        outcome(name, value)
        return value

    def get_text_var(name):
        """Get a text variable"""
        return branch_data["text_vars"].get(name, "")

    def set_text_var(name, value):
        """Set a text variable"""
        branch_data["text_vars"][name] = value
        return value

    def flag(name, value=None):
        """Get or set a flag; creates flag if missing"""
        if value is not None:
            # If a value is passed in, it's a SET operation
            branch_data["flags"][name] = value
            return value
        return branch_data["flags"].get(name, False)


    # Check functions to evaluate conditions
    def has_stat_minimum(stat_name, minimum):
        """Check if a stat meets or exceeds a minimum value"""
        return stat(stat_name) >= minimum

    def has_flag(flag_name):
        """Check if a flag is True"""
        return flag(flag_name) == True

    def has_relationship_minimum(name, minimum):
        """Check if a relationship meets or exceeds a minimum value"""
        return rel(name) >= minimum

    def get_highest_relationship():
        """Returns the name of the character with the highest relationship value"""
        relationships = branch_data["relationships"]
        return max(relationships, key=relationships.get)

    def reset_stat(stat_name):
        """Reset a stat to 0"""
        stat(stat_name, 0)
        return 0

    def evaluate_outcome(condition_dict):
        """
        Evaluates conditions and returns the corresponding outcome
        condition_dict should be a dictionary where keys are outcome names
        and values are functions that return True/False
        """
        for outcome_name, condition_func in condition_dict.items():
            if condition_func():
                return outcome_name
        return "default"
        
    def get_outcome(name):
        """Get the outcome value"""
        return branch_data["outcomes"].get(name, "unset")

default time_display = ""