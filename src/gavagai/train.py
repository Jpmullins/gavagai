import pytorch_lightning as pl
from torch.utils.data import DataLoader
from gavagai.dataset import AttitudeDataset
from gavagai.model import AttitudeClassifier

from pytorch_lightning.loggers import MLFlowLogger
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    os.environ["MLFLOW_EXPERIMENT_NAME"] = "Gavagai-AttitudeLearning"
    
    # Use absolute path to the data directory
    data_dir = Path("/workspace/code/gavagai/data/annotations")
    
    logger.info(f"Looking for annotations in {data_dir}")
    
    # Check if data directory exists and contains files
    if not data_dir.exists():
        logger.warning(f"Data directory {data_dir} does not exist. Creating it...")
        data_dir.mkdir(parents=True, exist_ok=True)
        logger.warning(f"Please add annotation files to {data_dir} before training.")
        return
    
    # Check for annotation files
    annotation_files = list(data_dir.glob("*.json"))
    if not annotation_files:
        logger.warning(f"No annotation files found in {data_dir}")
        return
    
    logger.info(f"Found {len(annotation_files)} annotation files: {[f.name for f in annotation_files]}")
    
    ds = AttitudeDataset(data_dir=str(data_dir))
    logger.info(f"Dataset loaded with {len(ds)} examples")
    logger.info(f"Attitude labels: {ds.label2id}")
    
    # Need at least 2 classes for training
    if len(ds.label2id) < 2:
        logger.error("Need at least 2 different attitude labels for classification")
        return
    
    dl = DataLoader(ds, batch_size=8, shuffle=True)

    model = AttitudeClassifier(num_labels=len(ds.label2id))
    logger.info(f"Model initialized with {len(ds.label2id)} output classes")

    # Set up MLFlow logging with absolute path
    mlruns_dir = Path("/workspace/code/gavagai/mlruns")
    logger.info(f"MLFlow logs will be stored in {mlruns_dir}")
    mlf_logger = MLFlowLogger(
        experiment_name="Gavagai-AttitudeLearning",
        tracking_uri=f"file:{mlruns_dir}"
    )

    trainer = pl.Trainer(
        max_epochs=3,
        log_every_n_steps=1,
        logger=mlf_logger
    )
    logger.info("Starting training...")
    trainer.fit(model, dl)
    logger.info("Training completed")

if __name__ == "__main__":
    main()