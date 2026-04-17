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
# EXPERIMENT 8: User Engagement Analysis
# =====================================================================

def user_engagement_analysis(df):
    """
    Analyze engagement patterns across different metrics
    """
    print("\n" + "="*80)
    print("EXPERIMENT 8: User Engagement Analysis")
    print("="*80)
    
    # Add content type
    df['content_type'] = df.apply(lambda _: random.choice(['Reels', 'Posts', 'Tweets']), axis=1)
    
    print("\nEngagement Analysis:")
    print(f"  Total Posts: {len(df)}")
    print(f"  Average Likes: {df['likes'].mean():.2f}")
    print(f"  Average Retweets: {df['retweets'].mean():.2f}")
    print(f"  Average Replies: {df['replies'].mean():.2f}")
    print(f"  Average Total Engagement: {df['engagement'].mean():.2f}")
    
    # Content type analysis
    print("\nContent Performance Analysis:")
    content_metrics = df.groupby('content_type').agg({
        'likes': 'mean',
        'retweets': 'mean',
        'engagement': 'mean',
        'tweet_id': 'count'
    }).rename(columns={'tweet_id': 'count'})
    print(content_metrics)
    
    # User type comparison (Influencer vs Brand)
    df['user_type'] = df.apply(lambda row: 'Influencer' if row['followers'] > 50000 else 'Brand/Regular',
                               axis=1)
    
    print("\nInfluencer vs Brand Engagement:")
    user_comparison = df.groupby('user_type')[['likes', 'retweets', 'engagement']].mean()
    print(user_comparison)
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('User Engagement Analysis', fontsize=16, fontweight='bold')
    
    # 1. Content type performance
    content_perf = df.groupby('content_type')['engagement'].mean().sort_values(ascending=False)
    axes[0, 0].bar(content_perf.index, content_perf.values, color=['#95E1D3', '#F38181', '#FCBAD3'])
    axes[0, 0].set_title('Average Engagement by Content Type')
    axes[0, 0].set_ylabel('Average Engagement')
    
    # 2. Likes vs Retweets vs Replies
    engagement_types = df[['likes', 'retweets', 'replies']].mean()
    axes[0, 1].bar(engagement_types.index, engagement_types.values, 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    axes[0, 1].set_title('Average Engagement Metrics')
    axes[0, 1].set_ylabel('Average Count')
    
    # 3. Influencer vs Brand engagement
    user_engagement_comp = df.groupby('user_type')['engagement'].mean()
    axes[1, 0].bar(user_engagement_comp.index, user_engagement_comp.values, 
                   color=['#667BC6', '#F38181'])
    axes[1, 0].set_title('Engagement: Influencer vs Brand')
    axes[1, 0].set_ylabel('Average Engagement')
    
    # 4. Content type distribution
    content_dist = df['content_type'].value_counts()
    axes[1, 1].pie(content_dist.values, labels=content_dist.index, autopct='%1.1f%%',
                   colors=['#95E1D3', '#F38181', '#FCBAD3'])
    axes[1, 1].set_title('Content Type Distribution')
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp8_engagement_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp8_engagement_analysis.png")
    
    return fig