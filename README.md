# What Content and Timing Factors Drive Social Media Engagement?

**DSCI 510 - Spring 2026 | University of Southern California**  
**Author:** Kexuan Liang  

---

## Introduction
This project investigates what content and timing factors drive social media engagement. As a Communication Data Science major, I wanted to understand whether engagement is mainly influenced by content characteristics (such as caption length or hashtag count) or by posting time. I used data from three different sources to explore this question.

---

## Data Sources

| # | Name | Type | Format | Link |
|---|------|------|--------|------|
| 1 | Instagram Engagement Analytics | File (Kaggle, hosted on Google Drive) | CSV | https://drive.google.com/uc?export=download&id=1kFbRKn3x2SVt6eo6XElhePFKiKBMDKbw |
| 2 | Viral Social Media Trends | File (Kaggle, hosted on Google Drive) | CSV | https://drive.google.com/uc?export=download&id=16Jq-lwlSK43wWLmo5iSvfqjju7yZHVHd |
| 3 | YouTube Data API v3 | API | JSON | https://developers.google.com/youtube/v3 |

The two CSV datasets are hosted on my public Google Drive.  
`main.py` downloads them automatically when the program is run.

---

## Features Explained

### Instagram
| Feature | What it means |
|---------|--------------|
| likes | Number of likes on the post |
| saves | Number of times the post was saved |
| shares | Number of times the post was shared |
| comments | Number of comments |
| impressions | Total number of times the post was seen |
| caption_length | Length of the caption (number of characters) |
| hashtags_count | Number of hashtags used |
| post_hour | Hour of posting (0–23) |
| follower_count | Number of followers |

### YouTube
| Feature | What it means |
|---------|--------------|
| title_length | Length of the video title |
| tags_count | Number of tags |
| post_hour | Upload hour (0–23) |
| view_count | Total views |
| like_count | Number of likes |
| comment_count | Number of comments |

### Viral Trends
| Feature | What it means |
|---------|--------------|
| likes | Number of likes |
| shares | Number of shares |
| comments | Number of comments |
| views | Total number of views |
| platform | Platform (Instagram, TikTok, Twitter, YouTube) |

---

## Engagement Rate Definition

Each dataset defines engagement rate differently, so they are analyzed separately.

| Dataset | Formula |
|---------|---------|
| Instagram | Pre-calculated in the dataset |
| Viral Trends | (likes + comments + shares) / views |
| YouTube | (likes + comments) / views |

---

## Analysis

- **Correlation**: Pearson correlation between each numeric feature and engagement rate  
- **Timing**: Average engagement rate by posting hour  
- **Platform**: Comparison of average engagement across platforms  

---

## Summary of Results

### Correlation
- **Instagram**: Likes, saves, shares, and comments are most correlated with engagement rate (r ≈ 0.45–0.51). Caption length and hashtag count have little impact. Impressions show a slight negative relationship, likely due to broader audience exposure.
- **YouTube**: Shorter titles tend to perform better. Posting hour has a small positive correlation.
- **Viral Trends**: Views are negatively correlated (r ≈ -0.69), suggesting that reach and engagement are not the same.

### Timing
- **Instagram**: Engagement rate is very stable across the day (range ≈ 0.0024).
- **YouTube**: Engagement varies significantly, with peaks around 1pm, 5pm, and 8pm.

### Platform
- All platforms (Instagram, TikTok, Twitter, YouTube) have similar engagement rates (≈ 0.17–0.19). Switching platforms alone does not significantly impact engagement.

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 2. Set up your YouTube API key

Create a `.env` file inside the `src/` folder and add:

```
YOUTUBE_API_KEY=your_youtube_api_key_here
```

You can get a key from:  
https://console.cloud.google.com/apis/credentials

---

### 3. Run the full pipeline

From the project root:

```bash
python src/main.py
```

### 4. Run tests

From the project root:

```bash
python src/tests.py
```

### 5. View results

From the project root:

```bash
jupyter notebook results.ipynb
```
---

## AI Usage

I used Claude as a coding assistant during this project. I designed the overall project structure, selected datasets, and conducted all analysis and interpretation independently.

AI assistance was used for:
- implementing the Google Drive download function (`download_from_drive`)
- implementing the YouTube Data API v3 request logic (`get_youtube_data`)
- minor debugging support (e.g., fixing import paths and environment setup issues)

These sections are marked with `# AI generated` comments in the code.

For all AI-assisted code, I reviewed it line-by-line, ensured I understood its functionality, and verified the results through my own testing.
