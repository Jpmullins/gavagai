"""
Data Structures for Triangulation RL

This module will define data structures for annotated dialogues, world states, and propositional attitude tracking, suitable for multi-agent RL and Bayesian modeling.
"""

# TODO: Define Dialogue, WorldState, and Annotation classes

class Dialogue:
    """Represents a multi-agent dialogue with propositional attitude annotations."""
    def __init__(self, utterances, annotations=None):
        self.utterances = utterances  # List of (speaker, text)
        self.annotations = annotations or []  # List of attitude annotations

class WorldState:
    """Represents the latent state of the world (facts, events, propositions)."""
    def __init__(self, state_dict):
        self.state = state_dict

class Annotation:
    """Represents a propositional attitude annotation (belief, desire, etc.)."""
    def __init__(self, agent, attitude_type, content):
        self.agent = agent
        self.attitude_type = attitude_type  # e.g., 'belief', 'desire', 'intention'
        self.content = content  # e.g., proposition, goal, etc.

# Utility functions
def load_annotations(directory):
    """Load dialogue annotations from a directory of JSON files."""
    import json
    from pathlib import Path

    dialogues = []
    for path in Path(directory).glob("*.json"):
        with open(path, "r") as f:
            data = json.load(f)
        utterances = [(u["speaker"], u["text"]) for u in data.get("context", [])]
        ann = [
            Annotation(a["speaker"], a["attitude"], a["content"])
            for a in data.get("annotations", [])
        ]
        dialogues.append(Dialogue(utterances, ann))
    return dialogues

# TODO: Add data loading, saving, and simulation utilities as needed
