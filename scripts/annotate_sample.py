"""
Quick annotation script for propositional attitudes.
"""

sample = {
    "dialogue_id": "0001",
    "context": [
        {"speaker": "A", "text": "I think it's going to rain tomorrow."},
        {"speaker": "B", "text": "No way. The forecast says sunny all week."}
    ],
    "annotations": [
        {"speaker": "A", "attitude": "believes", "content": "It will rain tomorrow."},
        {"speaker": "B", "attitude": "believes", "content": "It will not rain tomorrow."}
    ]
}

import json
with open("data/annotations/0001.json", "w") as f:
    json.dump(sample, f, indent=2)
