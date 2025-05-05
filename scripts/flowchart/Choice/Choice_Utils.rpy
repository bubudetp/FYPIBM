default outcome_history = []

init python:
    def record_choice_for_butterfly_effect(choice_text, impact_data):
        """Record a choice and its impact for the butterfly effect screen"""
        if not impact_data:
            return
            
        history_entry = {
            "choice_text": choice_text,
            "characters": impact_data.get("characters", []),
            "flags": impact_data.get("flags", []),
            "stats": impact_data.get("stats", {}),
            "outcomes": impact_data.get("outcomes", {}),
            "immersion": impact_data.get("immersion", {}),
            "emotion": impact_data.get("emotion", {})
        }
        
        store.outcome_history.append(history_entry)
    
    # Function to format outcome history for display
    def format_outcome_history():
        formatted = []
        
        for history_item in store.outcome_history:
            entry = {
                "choice_text": history_item["choice_text"],
                "impacts": []
            }
            
            # Format character relationships
            for char in history_item.get("characters", []):
                entry["impacts"].append(f"Relationship with {char} increased")
            
            # Format stats
            for stat_name, amount in history_item.get("stats", {}).items():
                # Convert to float if it's a string
                if isinstance(amount, str):
                    try:
                        amount = float(amount)
                    except ValueError:
                        amount = 0
                
                sign = "+" if amount > 0 else ""
                entry["impacts"].append(f"{stat_name.capitalize()} {sign}{amount}")
            
            # Format flags
            for flag in history_item.get("flags", []):
                entry["impacts"].append(f"Flag set: {flag}")
            
            # Format outcomes
            for outcome_name, value in history_item.get("outcomes", {}).items():
                # Convert to float if it's a string
                if isinstance(value, str):
                    try:
                        value = float(value)
                    except ValueError:
                        value = 0
                
                if value > 0:
                    level = "significantly" if value >= 1.0 else "slightly"
                    entry["impacts"].append(f"{outcome_name.replace('_', ' ').capitalize()} advanced {level}")
                elif value < 0:
                    level = "significantly" if value <= -1.0 else "slightly"
                    entry["impacts"].append(f"{outcome_name.replace('_', ' ').capitalize()} decreased {level}")
            
            # Format immersion effects
            for dim, val in history_item.get("immersion", {}).items():
                # Convert to float if it's a string
                if isinstance(val, str):
                    try:
                        val = float(val)
                    except ValueError:
                        val = 0
                        
                sign = "+" if val > 0 else ""
                entry["impacts"].append(f"Immersion: {dim} {sign}{val}")
            
            # Format emotion effects
            for char, val in history_item.get("emotion", {}).items():
                # Convert to float if it's a string
                if isinstance(val, str):
                    try:
                        val = float(val)
                    except ValueError:
                        val = 0
                        
                sign = "+" if val > 0 else ""
                entry["impacts"].append(f"Emotional connection with {char} {sign}{val}")
            
            formatted.append(entry)
        
        return formatted
    def handle_choice_impact(data):
            """
            Applies the serialized ChoiceImpact data to game state systems.
            """
            if not data:
                return

            # --- Characters (relationships)
            for char in data.get("characters", []):
                increase_rel(char, 1)

            # --- Stats
            for stat_name, amount in data.get("stats", {}).items():
                increase_stat(stat_name, amount)

            # --- Flags
            for flag_name in data.get("flags", []):
                set_flag(flag_name)

            # --- Outcomes
            for outcome_name, value in data.get("outcomes", {}).items():
                set_outcome(outcome_name, value)

            # --- Immersion Effects
            if "immersion" in data:
                for dim, val in data["immersion"].items():
                    if dim in immersion_tracker.dimensions:
                        immersion_tracker.dimensions[dim] += val

            # --- Emotion Effects
            if "emotion" in data:
                for char, val in data["emotion"].items():
                    emotional_profile.character_empathy[char] = \
                        emotional_profile.character_empathy.get(char, 0) + val

            # --- Future Branch Logic (you can expand this if needed)
            # This could be used to unlock nodes dynamically or log story branching
            for branch, change in data.get("branches", {}).items():
                pass  # Log, store, or trigger structural story changes as needed
    def determine_impact_type(translated_impact):
        """
        Automatically determine what kind of impact feedback to show based on translated impact dict.
        """
        if translated_impact.get("characters"):
            return "RELATIONSHIP"
        
        for stat_name in translated_impact.get("stats", {}):
            if "skill" in stat_name or stat_name in ["glitches", "reflection_score"]:
                return "KNOWLEDGE"
            elif stat_name in ["remembering", "curiosity", "comprehension", "empathy", "trust_level", "decision_clarity", "resilience"]:
                return "CURIOSITY"
            elif stat_name in ["deviation_level", "glitch_resistance"]:
                return "IMMERSION"
        
        if translated_impact.get("flags"):
            return "STORY"

        if translated_impact.get("outcomes"):
            return "STORY"

        if translated_impact.get("immersion"):
            return "IMMERSION"

        if translated_impact.get("emotion"):
            return "EMOTION"

        return "STORY"

    def build_reflection_choices(options, default_label="show_reflection_menu"):
        """
        Builds a reflection menu dynamically.
        Each option is a dict with:
        - "condition": string (optional)
        - "text": visible if unlocked
        - "next_label": the jump label if unlocked
        - "impact": optional ChoiceImpact-style dict
        """
        choices = []
        safe_context = {
            "has_flag": has_flag,
            "stat": stat,
            "rel": rel,
            "outcome": outcome,
            "has_stat_minimum": has_stat_minimum,
            "has_relationship_minimum": has_relationship_minimum
        }

        print(safe_context)
        for opt in options:
            try:
                unlocked = eval(opt.get("condition", "True"), {}, safe_context)
            except Exception:
                unlocked = False

            label = opt.get("next_label", default_label)

            # Clean and split the impact data
            raw_impact = opt.get("impact", {})
            translated_impact = {
                "characters": raw_impact.get("characters", []),
                "knowledge": raw_impact.get("knowledge", []),
                "flags": raw_impact.get("flags", []),
                "stats": raw_impact.get("stats", {}),
                "outcomes": raw_impact.get("outcomes", {}),
                "immersion": raw_impact.get("immersion", {}),
                "emotion": raw_impact.get("emotion", {}),
                "branches": {},  # store unknowns here
            }

            # Migrate branches if present
            for key, value in raw_impact.get("branches", {}).items():
                if key.startswith("rel_"):
                    translated_impact["characters"].append(key[4:])
                elif key.startswith("stat_"):
                    translated_impact["stats"][key[5:]] = value
                elif key.startswith("flag_"):
                    translated_impact["flags"].append(key[5:])
                elif key.startswith("outcome_"):
                    translated_impact["outcomes"][key[8:]] = value
                else:
                    translated_impact["branches"][key] = value  # fallback

            translated_impact["characters"] = list(set(translated_impact["characters"]))

            # >>> ADD AUTOMATIC IMPACT TYPE/FEEDBACK HERE <<<
            impact_type = determine_impact_type(translated_impact)
            feedback_text = get_impact_text(impact_type)

            choices.append({
                "prompt": opt.get("prompt", None),
                "text": opt["text"] if unlocked else "???",
                "next_label": label,
                "impact": translated_impact,
                "impact_type": impact_type,
                "feedback_text": feedback_text
            })

        print("=== [build_reflection_choices] Done ===\n")
        return choices



    def queue_choice_feedback(queue, delay=1):
        """Queue feedback but consolidate identical types to show only once each"""
        
        # Create a dictionary to track unique feedback types
        unique_feedbacks = {}
        
        # Consolidate identical types, keeping the most positive direction
        for ftype, direction in queue:
            if ftype not in unique_feedbacks:
                unique_feedbacks[ftype] = direction
            elif (direction == "↑" and unique_feedbacks[ftype] == "↓"):
                # If we have both up and down for the same type, prioritize the positive one
                unique_feedbacks[ftype] = direction
        
        # Queue only the unique feedback types
        for i, (ftype, direction) in enumerate(unique_feedbacks.items()):
            renpy.call_in_new_context("show_single_feedback", ftype, direction, delay * i)


label show_single_feedback(ftype, direction, delay):
    $ renpy.pause(delay, hard=True)
    show screen choice_impact_feedback(type=ftype, direction=direction)
    $ renpy.pause(0.5, hard=True)
    return

label handle_dynamic_choice:
    python:
        if not dynamic_choices:
            renpy.say(n, "No available choices.")
            renpy.return_statement()

        # Extract the prompt (only once!)
        if "prompt" in dynamic_choices[0]:
            current_prompt = dynamic_choices[0]["prompt"]
            # dynamic_choices = dynamic_choices[1:]  # Remove prompt from choices
        else:
            current_prompt = ""

        menu_items = []
        for i, choice in enumerate(dynamic_choices):
            menu_items.append((choice["text"], str(i)))

    # Show both screens at once
    show screen choice_title(current_prompt)
    $ result = renpy.display_menu(menu_items)
    hide screen choice_title

    python:
        if result is None:
            renpy.return_statement()
            
        selected = dynamic_choices[int(result)]
        impact_data = selected.get("impact", {})
        
        print("Applying choice impact:")
        print("Characters:", impact_data.get("characters", []))
        print("Knowledge:", impact_data.get("knowledge", []))
        print("Branches:", impact_data.get("branches", {}))
        print("Stats:", impact_data.get("stats", {}))
        print("Flags:", impact_data.get("flags", []))
        print("Outcomes:", impact_data.get("outcomes", {}))
        print("Immersion:", impact_data.get("immersion", {}))
        print("Emotion:", impact_data.get("emotion", {}))
        
        # ADD THIS LINE - Record the choice for butterfly effect
        record_choice_for_butterfly_effect(selected.get("text", ""), impact_data)
        
        if impact_data:
            ci = ChoiceImpact(
                affected_characters=impact_data.get("characters"),
                knowledge_requirements=impact_data.get("knowledge"),
                future_branch_changes=impact_data.get("branches"),
                stat_changes=impact_data.get("stats"),
                flags_to_set=impact_data.get("flags"),
                outcome_changes=impact_data.get("outcomes"),
                immersion_effects=impact_data.get("immersion"),
                emotion_effects=impact_data.get("emotion")
            )
            ci.apply()
            
            impact_queue = []
            if ci.affected_characters:
                impact_queue.append(("RELATIONSHIP", "↑"))
            if ci.stat_changes:
                for k, v in ci.stat_changes.items():
                    direction = "↑" if v >= 0 else "↓"
                    impact_queue.append(("KNOWLEDGE", direction))
            if ci.immersion_effects:
                for k, v in ci.immersion_effects.items():
                    direction = "↑" if v >= 0 else "↓"
                    impact_queue.append(("IMMERSION", direction))
            if ci.emotion_effects:
                for k, v in ci.emotion_effects.items():
                    direction = "↑" if v >= 0 else "↓"
                    impact_queue.append(("EMOTION", direction))
            if ci.future_branch_changes:
                for k, v in ci.future_branch_changes.items():
                    impact_queue.append(("STORY", "→"))
                    
            queue_choice_feedback(impact_queue)
            
        # === JUMP TO NEXT LABEL ===
        if "next_label" in selected:
            renpy.jump(selected["next_label"])
        else:
            renpy.jump(return_label if "return_label" in globals() else "main")

# label _show_feedback:
#     # Show all feedback at once (simpler than queuing)
#     show screen choice_impact_feedback
#     pause 1.5
#     hide screen choice_impact_feedback
#     return

# label _show_feedback(ftype, direction, delay):
#     $ renpy.pause(delay)
#     show screen choice_impact_feedback(type=ftype, direction=direction)
#     $ renpy.pause(1.5)
#     return
