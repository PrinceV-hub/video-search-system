# Motive Project

This repository indexes and searches dashcam video incidents using AWS S3, Bedrock Claude, and semantic search with Sentence Transformers.

## Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd motive-project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your AWS credentials:
   ```bash
   cp .env.example .env
   # Edit .env and add your credentials
   ```

## Usage

Run the main script to build the index and generate submissions:
```bash
python main.py
```

## Security
- **Never commit your `.env` file or credentials.**
- Sensitive files like `video_index.pkl` and submission CSVs are ignored by `.gitignore`.

## License
MIT
