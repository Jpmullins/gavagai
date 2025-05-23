#!/usr/bin/env python
"""
Interactive annotation tool for Gavagai propositional attitudes.

This script helps you create annotation files for the Gavagai project.
"""
import json
from pathlib import Path
import uuid

def create_annotation():
    """Create an annotation file interactively."""
    print("Gavagai Attitude Annotation Tool")
    print("================================")
    
    dialogue_id = input("Enter dialogue ID (or press Enter for auto-generated ID): ")
    if not dialogue_id:
        dialogue_id = str(uuid.uuid4())[:8]
    
    context = []
    annotations = []
    
    print("\nEnter context utterances (press Enter on an empty line to finish):")
    while True:
        speaker = input("Speaker (e.g., 'A', 'Alice'): ")
        if not speaker:
            break
        
        text = input("Text: ")
        if not text:
            break
        
        context.append({"speaker": speaker, "text": text})
        
        # Ask for attitude annotation immediately after each utterance
        add_annotation = input("Add an attitude annotation for this utterance? (y/n): ").lower()
        if add_annotation == 'y':
            attitude = input("Attitude (believes, knows, hopes, doubts, etc.): ")
            content = input("Content (the proposition): ")
            annotations.append({
                "speaker": speaker,
                "attitude": attitude,
                "content": content
            })
        
        more = input("Add another utterance? (y/n): ").lower()
        if more != 'y':
            break
    
    print("\nAdd any additional annotations (press Enter on an empty line to finish):")
    while True:
        speaker = input("Speaker (e.g., 'A', 'Alice'): ")
        if not speaker:
            break
        
        attitude = input("Attitude (believes, knows, hopes, doubts, etc.): ")
        if not attitude:
            break
        
        content = input("Content (the proposition): ")
        if not content:
            break
        
        annotations.append({
            "speaker": speaker,
            "attitude": attitude,
            "content": content
        })
        
        more = input("Add another annotation? (y/n): ").lower()
        if more != 'y':
            break
    
    # Create the annotation object
    annotation = {
        "dialogue_id": dialogue_id,
        "context": context,
        "annotations": annotations
    }
    
    # Save the annotation
    data_dir = Path(__file__).parent.parent / "data" / "annotations"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{dialogue_id}.json"
    filepath = data_dir / filename
    
    with open(filepath, 'w') as f:
        json.dump(annotation, f, indent=2)
    
    print(f"\nAnnotation saved to {filepath}")
    return filepath

if __name__ == "__main__":
    filepath = create_annotation()
    
    # Show a preview of the created annotation
    print("\nAnnotation Preview:")
    with open(filepath, 'r') as f:
        print(json.dumps(json.load(f), indent=2))
