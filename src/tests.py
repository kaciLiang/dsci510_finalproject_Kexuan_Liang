from load import load_local_csv, get_youtube_data
from process import process_viral_trends


# test loading csv data
def test_load_data():
    print("Testing CSV loading")

    df = load_local_csv("Cleaned_Viral_Social_Media_Trends.csv")

    if df is None or len(df) == 0:
        print("FAIL: data not loaded")
    else:
        print(f"PASS: loaded {len(df)} rows")


# test processing function
def test_processing():
    print("Testing data processing")

    df = load_local_csv("Cleaned_Viral_Social_Media_Trends.csv")

    if df is None:
        print("FAIL: no data")
        return

    processed = process_viral_trends(df)

    if len(processed) == 0:
        print("FAIL: processing returned empty")
    else:
        print(f"PASS: processed {len(processed)} rows")


# test youtube api (optional)
def test_youtube_api():
    print("Testing YouTube API")

    df = get_youtube_data(max_results=5)

    if df is None:
        print("SKIP: API not available")
        return

    if len(df) == 0:
        print("FAIL: no data returned")
    else:
        print(f"PASS: got {len(df)} rows")


if __name__ == "__main__":
    test_load_data()
    test_processing()
    test_youtube_api()