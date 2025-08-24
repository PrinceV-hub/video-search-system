# Helper functions for dashcam search system

from typing import List, Dict

def watch_query_videos(indexer, query: str, top_k: int = 5):
    """
    Display top videos for a search query using the indexer.
    Args:
        indexer: VideoTextIndexer instance
        query: Search query string
        top_k: Number of top videos to display
    """
    indexer.watch_top_videos(query, top_k=top_k)


def get_query_video_info(indexer, query: str, top_k: int = 5) -> List[Dict]:
    """
    Get video information for a search query using the indexer.
    Args:
        indexer: VideoTextIndexer instance
        query: Search query string
        top_k: Number of top videos to get info for
    Returns:
        List of video information dictionaries
    """
    return indexer.get_video_urls(query, top_k=top_k)

# Add any utility/helper functions here, e.g. watch_query_videos, get_query_video_info, etc.

![Pipeline Diagram](diagrams/pipeline.png)
