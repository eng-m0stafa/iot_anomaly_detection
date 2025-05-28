# Data Documentation

## Data Files Location
The model files and data are stored in Google Drive:
https://drive.google.com/drive/folders/1xlgUnIGV5O_M7owjcbi-MtfSXAWaXC4t

## Files Description
1. Data Files:
   - BREMaster.csv (1.14 GB)
   - CUMaster.csv (3.82 GB)
   - Phy_BRE_Master.csv (4.99 GB)

2. Model Files:
   - enhanced_autoencoder.pth
   - enhanced_lstm.pth
   - enhanced_dlrm.pth
   - enhanced_rnn.pth

## How to Download
1. Access the Google Drive link: https://drive.google.com/drive/folders/1xlgUnIGV5O_M7owjcbi-MtfSXAWaXC4t
2. Download the required files
3. Place them in the appropriate directories:
   - Model files → `models/` directory
   - Data files → `data/` directory

## Data Format
The data files are in CSV format with the following specifications:
- BREMaster.csv: 1.14 GB
- CUMaster.csv: 3.82 GB
- Phy_BRE_Master.csv: 4.99 GB

## Model Requirements
The models are trained on the provided data files and require:
- Input dimension matching the training data
- PyTorch 1.9.0 or higher
- CUDA support for GPU acceleration (optional)
