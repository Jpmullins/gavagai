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

# TODO: Add data loading, saving, and simulation utilities as needed
