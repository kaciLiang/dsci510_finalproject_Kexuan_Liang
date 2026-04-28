import os
import requests
import pandas as pd
from config import DATA_DIR, YOUTUBE_API_KEY, YOUTUBE_QUERIES

def download_from_drive(url, filename):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        return path
    print(f"Downloading {filename}...")
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Download failed ({r.status_code})")
        return None
    with open(path, "wb") as f:
        f.write(r.content)
    return path

# load csv
def load_local_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None

    df = pd.read_csv(path)
    print(f"Loaded {filename}, rows: {len(df)}")
    return df

# AI generated - YouTube Data collect
def get_youtube_data(queries=None, max_results=50):
    if not YOUTUBE_API_KEY:
        print("Error: YOUTUBE_API_KEY not set in src/.env")
        return None

    if queries is None:
        queries = YOUTUBE_QUERIES

    print("Getting YouTube data")
    all_rows = []

    for query in queries:
        search_url = "https://www.googleapis.com/youtube/v3/search"

        r = requests.get(search_url, params={
            "part": "id",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "key": YOUTUBE_API_KEY,
        })

        if r.status_code != 200:
            print(f"  search error {r.status_code}: {r.text[:200]}")
            continue

        video_ids = [item["id"]["videoId"] for item in r.json().get("items", [])]
        if not video_ids:
            continue

        stats_url = "https://www.googleapis.com/youtube/v3/videos"

        r2 = requests.get(stats_url, params={
            "part": "snippet,statistics",
            "id": ",".join(video_ids),
            "key": YOUTUBE_API_KEY,
        })

        if r2.status_code != 200:
            print(f"  stats error {r2.status_code}: {r2.text[:200]}")
            continue

        for item in r2.json().get("items", []):
            snip = item.get("snippet", {})
            stats = item.get("statistics", {})

            all_rows.append({
                "video_id":      item.get("id"),
                "title":         snip.get("title"),
                "published_at":  snip.get("publishedAt"),
                "channel":       snip.get("channelTitle"),
                "tags_count":    len(snip.get("tags", [])),
                "title_length":  len(snip.get("title", "")),
                "view_count":    int(stats.get("viewCount", 0)),
                "like_count":    int(stats.get("likeCount", 0)),
                "comment_count": int(stats.get("commentCount", 0)),
                "query":         query,
            })

    if not all_rows:
        return None

    df = pd.DataFrame(all_rows)

    # define engagement rate
    df["engagement"] = df["like_count"] + df["comment_count"]
    df["engagement_rate"] = df["engagement"] / df["view_count"].replace(0, 1)

    # timing features
    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")
    df["post_hour"] = df["published_at"].dt.hour
    df["day_of_week"] = df["published_at"].dt.day_name()

    print(f"Collected {len(df)} videos")
    return df


def save_data(df, filename):
    path = os.path.join(DATA_DIR, filename)
    df.to_csv(path, index=False)
    print(f"Saved -> {filename}")