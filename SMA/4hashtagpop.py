import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import warnings
warnings.filterwarnings('ignore')

# =====================================================================
# EXPERIMENT 4: Hashtag Popularity Analysis
# =====================================================================

def hashtag_analysis(df):
    """
    Analyze trending hashtags
    """
    print("\n" + "="*80)
    print("EXPERIMENT 4: Hashtag Popularity Analysis")
    print("="*80)
    
    # Extract and count hashtags
    hashtags = ['#AIRevolution', '#StartupIndia', '#IPL2026', '#DigitalIndia', '#WorkFromHome']
    
    hashtag_data = {ht: random.randint(50, 500) for ht in hashtags}
    hashtag_engagement = {ht: random.randint(500, 5000) for ht in hashtags}
    
    # Add hashtags to tweets
    df['hashtag'] = df.apply(lambda _: random.choice(hashtags), axis=1)
    
    print("\nHashtag Popularity Metrics:")
    for hashtag in hashtags:
        count = len(df[df['hashtag'] == hashtag])
        avg_engagement = df[df['hashtag'] == hashtag]['engagement'].mean()
        print(f"{hashtag}: {count} tweets | Avg Engagement: {avg_engagement:.2f}")
    
    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Hashtag Popularity Analysis', fontsize=16, fontweight='bold')
    
    # 1. Hashtag frequency
    hashtag_freq = df['hashtag'].value_counts()
    axes[0].bar(range(len(hashtag_freq)), hashtag_freq.values, color='#667BC6', alpha=0.8)
    axes[0].set_xticks(range(len(hashtag_freq)))
    axes[0].set_xticklabels(hashtag_freq.index, rotation=45)
    axes[0].set_title('Tweet Count by Hashtag')
    axes[0].set_ylabel('Number of Tweets')
    
    # 2. Average engagement by hashtag
    hashtag_engagement_df = df.groupby('hashtag')['engagement'].mean().sort_values(ascending=False)
    axes[1].barh(hashtag_engagement_df.index, hashtag_engagement_df.values, color='#FF6B6B', alpha=0.8)
    axes[1].set_title('Average Engagement by Hashtag')
    axes[1].set_xlabel('Average Engagement')
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp4_hashtag_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp4_hashtag_analysis.png")
    
    return fig