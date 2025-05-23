from pathlib import Path
import json
import torch
from torch.utils.data import Dataset
from transformers import BertTokenizer
import logging

class AttitudeDataset(Dataset):
    def __init__(self, data_dir="data/annotations"):
        self.data = []
        data_path = Path(data_dir)
        files = list(data_path.glob("*.json"))
        
        if not files:
            logging.warning(f"No JSON files found in {data_dir}. You may need to add annotation files.")
            # Add a dummy example to prevent errors
            self.data = [("This is a placeholder example", "neutral")]
        else:
            for file in files:
                try:
                    item = json.load(open(file))
                    if "annotations" in item:
                        for ann in item["annotations"]:
                            # Handle new annotation format with speaker, attitude, content
                            if "speaker" in ann and "attitude" in ann and "content" in ann:
                                self.data.append((ann["content"], ann["attitude"]))
                            # Handle old format with just content and attitude
                            elif "content" in ann and "attitude" in ann:
                                self.data.append((ann["content"], ann["attitude"]))
                except Exception as e:
                    logging.error(f"Error loading {file}: {e}")

        self.label2id = {label: i for i, label in enumerate(sorted(set(x[1] for x in self.data)))}
        self.id2label = {i: label for label, i in self.label2id.items()}
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    def __len__(self): return len(self.data)

    def __getitem__(self, idx):
        text, label = self.data[idx]
        encoding = self.tokenizer(text, truncation=True, padding="max_length", max_length=64, return_tensors="pt")
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "label": torch.tensor(self.label2id[label], dtype=torch.long),
        }
