# Annotation Format for Gavagai Attitude Learning

This document explains the annotation format used in the Gavagai project for propositional attitude learning.

## Overview

Annotations are stored as JSON files in the `data/annotations` directory. Each annotation file represents a dialogue with one or more speakers and their expressed attitudes.

## Format

Each annotation file should follow this format:

```json
{
  "dialogue_id": "unique_id",
  "context": [
    {"speaker": "A", "text": "Original utterance by speaker A"},
    {"speaker": "B", "text": "Original utterance by speaker B"}
  ],
  "annotations": [
    {"speaker": "A", "attitude": "believes", "content": "The proposition that A believes"},
    {"speaker": "B", "attitude": "doubts", "content": "The proposition that B doubts"}
  ]
}
```

## Fields

- `dialogue_id`: A unique identifier for the dialogue
- `context`: An array of utterances with the following fields:
  - `speaker`: An identifier for the speaker (can be a name or letter)
  - `text`: The actual text spoken by the speaker
- `annotations`: An array of attitude annotations with the following fields:
  - `speaker`: The speaker who expressed the attitude
  - `attitude`: The type of attitude expressed (believes, knows, hopes, etc.)
  - `content`: The propositional content of the attitude

## Supported Attitude Types

The following attitude types are currently supported:

- `believes` - The speaker believes the content to be true
- `knows` - The speaker knows (with certainty) the content
- `hopes` - The speaker hopes the content will be true
- `doubts` - The speaker doubts the truth of the content
- `suspects` - The speaker suspects the content might be true
- `angry_about` - The speaker is angry about the content
- `appreciates` - The speaker appreciates the content

You can add more attitude types as needed, and the model will learn to classify them.

## Example

```json
{
  "dialogue_id": "0001",
  "context": [
    {"speaker": "Alice", "text": "I believe climate change is a serious threat."},
    {"speaker": "Bob", "text": "I'm not convinced by the evidence."}
  ],
  "annotations": [
    {"speaker": "Alice", "attitude": "believes", "content": "Climate change is a serious threat."},
    {"speaker": "Bob", "attitude": "doubts", "content": "The evidence for climate change is convincing."}
  ]
}
```

## Creating New Annotations

See `scripts/annotate_sample.py` for an example of how to create new annotation files programmatically.
