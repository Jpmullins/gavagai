def extract_sentences(dialogue):
    """
    Very basic sentence splitter for bootstrapping.
    """
    import re
    sentences = re.split(r'(?<=[.?!])\s+', dialogue.strip())
    return [s.strip() for s in sentences if s]
