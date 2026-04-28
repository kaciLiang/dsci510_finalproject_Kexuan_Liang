import os
from config import (DATA_DIR, RESULTS_DIR,
    INSTAGRAM_CSV, VIRAL_TRENDS_CSV, YOUTUBE_CSV,INSTAGRAM_URL, VIRAL_TRENDS_URL,)
from load import (load_local_csv, get_youtube_data, save_data,download_from_drive,)
from process import process_instagram, process_viral_trends
from analyze import run_full_analysis

def main():
    print("Running social media analysis")
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

# download csv
    download_from_drive(INSTAGRAM_URL, INSTAGRAM_CSV)
    download_from_drive(VIRAL_TRENDS_URL, VIRAL_TRENDS_CSV)
    print("Instagram Analytics")
    ig_raw = load_local_csv(INSTAGRAM_CSV)
    if ig_raw is not None:
        ig = process_instagram(ig_raw)
        run_full_analysis(ig, "Instagram")

    print("Viral Social Media Trends")
    vt_raw = load_local_csv(VIRAL_TRENDS_CSV)
    if vt_raw is not None:
        vt = process_viral_trends(vt_raw)
        run_full_analysis(vt, "ViralTrends")

    print("YouTube API")
    yt_raw = get_youtube_data()
    if yt_raw is not None:
        save_data(yt_raw, YOUTUBE_CSV)
        run_full_analysis(yt_raw, "YouTube")

    print("Done. Check results folder.")


if __name__ == "__main__":
    main()
