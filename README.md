# Dashcam Search System
![Project Logo](video-search-system/motive.png)






A modular pipeline for semantic search over dashcam video features using AWS S3, Bedrock Claude, and Sentence Transformers.

## Directory Structure
```
dashcam-search/
│── README.md
│── requirements.txt
│── .gitignore
│
├── src/
│   ├── indexer.py        # VideoTextIndexer class (main pipeline)
│   ├── utils.py          # Helper functions
│   └── main.py           # Entry point to build index / search
│
├── notebooks/            # Jupyter notebooks for experiments
├── data/                 # Example TSV or small sample features
├── saved_index/          # Pickled embeddings + metadata
├── outputs/              # Search results, submission CSV
└── diagrams/             # Pipeline diagrams
```

## ⚙️ Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/yourusername/dashcam-search.git
cd dashcam-search
pip install -r requirements.txt
```
Dependencies include:
- torch
- sentence-transformers
- pandas
- scikit-learn
- boto3 (for AWS S3 + Bedrock)
- matplotlib (for optional video rendering)

## 🔑 AWS Setup
This project uses Amazon S3 for data and Bedrock (Claude) for description generation.

Configure AWS credentials locally:
```bash
aws configure
```
Or set environment variables in a `.env` file:
```
AWS_ACCESS_KEY_ID=xxxx
AWS_SECRET_ACCESS_KEY=xxxx
AWS_DEFAULT_REGION=us-east-1
```

## 🚀 Usage
### 1. Build the index (descriptions + embeddings)
```bash
python src/main.py --build_index
```
This will:
- Load video features from S3
- Generate natural language descriptions (Claude or fallback)
- Create embeddings
- Save everything in `saved_index/`

### 2. Run a search query
```bash
python src/main.py --search "car accident at intersection"
```
This will:
- Convert your query to an embedding
- Find most similar video descriptions
- Show top-K matches with S3 paths
- Save results in `outputs/`

### 3. Export submission file
```bash
python src/main.py --export_submission
```
Creates a `submission.csv` file inside `outputs/`.

## 📊 Example Query
Query: "A pedestrian crossing the road at night"
Top results:
1. s3://bucket/video1.mp4  (score: 0.87)
2. s3://bucket/video2.mp4  (score: 0.83)
...

## 📌 Features
- End-to-end pipeline (S3 → Descriptions → Embeddings → Search)
- Fallback description generator (if Claude API fails)
- Save/load index to avoid recomputation
- Easy submission file generator
- Optional Jupyter notebooks for exploration
