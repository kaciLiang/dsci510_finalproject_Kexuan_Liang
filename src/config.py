import os
from dotenv import load_dotenv

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_DIR    = os.path.join(BASE_DIR, '..', 'data')
RESULTS_DIR = os.path.join(BASE_DIR, '..', 'results')

load_dotenv(os.path.join(BASE_DIR, '.env.example'))

# data filenames
INSTAGRAM_CSV    = "Instagram_Analytics.csv"
VIRAL_TRENDS_CSV = "Cleaned_Viral_Social_Media_Trends.csv"
YOUTUBE_CSV      = "youtube_collected.csv"

# google drive datasets
INSTAGRAM_URL    = "https://drive.google.com/uc?export=download&id=1kFbRKn3x2SVt6eo6XElhePFKiKBMDKbw"
VIRAL_TRENDS_URL = "https://drive.google.com/uc?export=download&id=16Jq-lwlSK43wWLmo5iSvfqjju7yZHVHd"

# api
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
YOUTUBE_QUERIES = ["social media marketing", "instagram tips", "tiktok viral", "content creator",
    "viral video", "youtube growth", "social media tips", "influencer marketing",]

# plot size
PLOT_SIZE_BAR  = (8, 5)
PLOT_SIZE_LINE = (8, 4)
PLOT_DPI       = 120

