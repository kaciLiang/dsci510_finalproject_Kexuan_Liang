import os
import pandas as pd
import matplotlib.pyplot as plt
from config import RESULTS_DIR, PLOT_SIZE_BAR, PLOT_SIZE_LINE, PLOT_DPI

def ensure_results_dir():
    os.makedirs(RESULTS_DIR, exist_ok=True)

# Correlation
def compute_correlations(df, target="engagement_rate"):
    numeric_df = df.select_dtypes(include="number")
    if target not in numeric_df.columns:
        print(f"Warning: '{target}' not found.")
        return pd.Series(dtype=float)
    corr = numeric_df.corr()
    corr_target = corr[target]
    corr_target = corr_target.drop(target)
    corr_target = corr_target.sort_values(ascending=False)
    print(f"Correlations with '{target}':{corr_target}")
    return corr_target

# correlation
def plot_correlation_bar(correlations, dataset_name, notebook_plot=False):
    ensure_results_dir()
    if correlations.empty:
        return
    fig, ax = plt.subplots(figsize=PLOT_SIZE_BAR)

    colors = []
    for v in correlations.values:
        if v >= 0:
            colors.append("blue")
        else:
            colors.append("red")

    correlations.plot(kind="bar", color=colors, ax=ax)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title(f"{dataset_name} - Correlation with Engagement Rate")
    ax.set_ylabel("Pearson r")
    ax.set_xlabel("Feature")
    plt.tight_layout()

    path = os.path.join(RESULTS_DIR, f"{dataset_name}_correlation.png")
    fig.savefig(path, dpi=PLOT_DPI)
    print(f"Saved -> {path}")

    if notebook_plot:
        plt.show()
    else:
        plt.close(fig)


# timing
def plot_engagement_by_hour(df, dataset_name, engagement_col="engagement_rate", notebook_plot=False):
    ensure_results_dir()
    if "post_hour" not in df.columns or engagement_col not in df.columns:
        print(f"Skipping hour plot for {dataset_name} (missing columns).")
        return

    hourly = df.groupby("post_hour")[engagement_col].mean()

    fig, ax = plt.subplots(figsize=PLOT_SIZE_LINE)
    hourly.plot(ax=ax, marker="o", color="steelblue")
    ax.set_title(f"{dataset_name} - Avg Engagement by Posting Hour")
    ax.set_xlabel("Hour of Day (0-23)")
    ax.set_ylabel(f"Mean {engagement_col}")
    ax.set_xticks(range(0, 24))
    plt.tight_layout()

    path = os.path.join(RESULTS_DIR, f"{dataset_name}_by_hour.png")
    fig.savefig(path, dpi=PLOT_DPI)
    print(f"Saved -> {path}")

    if notebook_plot:
        plt.show()
    else:
        plt.close(fig)


# platform
def plot_engagement_by_platform(df, dataset_name, platform_col="platform", engagement_col="engagement_rate", notebook_plot=False):
    ensure_results_dir()
    if platform_col not in df.columns or engagement_col not in df.columns:
        print(f"  Skipping platform plot for {dataset_name} (missing columns).")
        return

    # platform engagement rate mean
    means = df.groupby(platform_col)[engagement_col].mean()

    fig, ax = plt.subplots(figsize=PLOT_SIZE_BAR)
    means.plot(kind="bar", color="steelblue", ax=ax)
    ax.set_title(f"{dataset_name} - Avg Engagement Rate by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel(f"Mean {engagement_col}")
    plt.tight_layout()

    path = os.path.join(RESULTS_DIR, f"{dataset_name}_by_platform.png")
    fig.savefig(path, dpi=PLOT_DPI)
    print(f"Saved -> {path}")

    if notebook_plot:
        plt.show()
    else:
        plt.close(fig)

def run_full_analysis(df, dataset_name, engagement_col="engagement_rate", notebook_plot=False):
    print(f"Analysing: {dataset_name}")
    correlations = compute_correlations(df, target=engagement_col)
    plot_correlation_bar(correlations, dataset_name, notebook_plot=notebook_plot)
    plot_engagement_by_hour(df, dataset_name, engagement_col, notebook_plot=notebook_plot)
    plot_engagement_by_platform(df, dataset_name, engagement_col=engagement_col, notebook_plot=notebook_plot)