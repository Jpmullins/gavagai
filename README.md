# Gavagai

Inspired by Quine and Davidson, Gavagai explores how agents can learn *belief*, *desire*, and *intention* not as predefined states, but as emergent patterns from empirical learning. This project aims to:

- Represent propositional attitudes holophrastically
- Anchor meaning through intersubjective triangulation
- Model rational normativity and interpretive understanding

> “Meaning is not in the head. It is in the act of interpretation.”

This repository includes:
- A growing dataset of annotated dialogues
- Baseline models for learning interpretive structure
- Philosophical framing and technical vision


## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/gavagai.git
cd gavagai
pip install -e .
```

### Creating Annotations

You can create new annotations using the interactive tool:

```bash
python scripts/create_annotation.py
```

See [Annotation Format Documentation](docs/annotation_format.md) for details on the annotation format.

### Training a Model

```bash
python -c "from gavagai.train import main; main()"
```

=======

Collaborators welcome.
