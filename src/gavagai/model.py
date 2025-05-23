import torch
import pytorch_lightning as pl
from transformers import BertForSequenceClassification, BertTokenizer
import logging

from torchmetrics import Accuracy, F1Score

logger = logging.getLogger(__name__)

class AttitudeClassifier(pl.LightningModule):
    def __init__(self, num_labels: int, lr: float = 1e-5):
        super().__init__()
        self.save_hyperparameters()
        self.model = BertForSequenceClassification.from_pretrained(
            "bert-base-uncased", num_labels=num_labels
        )
        
        # Metrics can only be used when we have at least 2 classes
        if num_labels >= 2:
            self.train_acc = Accuracy(task="multiclass", num_classes=num_labels)
            self.train_f1 = F1Score(task="multiclass", num_classes=num_labels, average="macro")
            self.use_metrics = True
        else:
            logger.warning("Only one class available, metrics will not be used")
            self.use_metrics = False

    def training_step(self, batch, batch_idx):
        outputs = self(**batch)
        loss = outputs.loss
        
        self.log("train_loss", loss)
        
        # Only compute and log metrics if we have multiple classes
        if self.use_metrics:
            logits = outputs.logits
            preds = torch.argmax(logits, dim=1)
            labels = batch["label"]

            self.train_acc(preds, labels)
            self.train_f1(preds, labels)
            
            self.log("train_acc", self.train_acc, prog_bar=True)
            self.log("train_f1", self.train_f1, prog_bar=True)
            
        return loss
        
    def forward(self, input_ids, attention_mask, label=None):
        return self.model(input_ids=input_ids, attention_mask=attention_mask, labels=label)

    def configure_optimizers(self):
        return torch.optim.AdamW(self.parameters(), lr=self.hparams.lr)

