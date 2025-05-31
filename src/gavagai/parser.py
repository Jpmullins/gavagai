"""
Parser and Annotation Tools for Triangulation RL

This module will provide utilities for extracting sentences, utterances, and propositional attitude annotations from dialogues, supporting both data preparation and online agent interaction.
"""

# TODO: Implement advanced parsing and annotation extraction

def extract_utterances(dialogue):
    """Split a dialogue string into utterances (very basic stub)."""
    import re
    return re.split(r'(?<=[.?!])\s+', dialogue.strip())

# TODO: Add functions for extracting and annotating beliefs, desires, intentions, etc.
