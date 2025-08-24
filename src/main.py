import argparse
from indexer import VideoTextIndexer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dashcam Video Search System")
    parser.add_argument('--build_index', action='store_true', help='Build the video index')
    parser.add_argument('--search', type=str, help='Search query')
    args = parser.parse_args()

    indexer = VideoTextIndexer()

    if args.build_index:
        # Example usage, customize bucket/tsv as needed
        bucket_name = 'motiverse-2025-data'
        tsv_key = 'video_features.tsv'
        indexer.build_index(bucket_name, tsv_key, use_claude=True)
    elif args.search:
        # Load index and search
        indexer.load_index('video_index.pkl')
        results = indexer.search(args.search)
        print("Search results:", results)
    else:
        parser.print_help()
