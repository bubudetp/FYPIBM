init python:
    def adjust_immersion(dim, delta):
        if dim in immersion_tracker.dimensions:
            immersion_tracker.dimensions[dim] += delta

    def adjust_emotion(transport=0.0, imagery=0.0):
        emotional_profile.transportation += transport
        emotional_profile.mental_imagery += imagery

    def adjust_empathy(char, delta):
        emotional_profile.character_empathy[char] = emotional_profile.character_empathy.get(char, 0) + delta