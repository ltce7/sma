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
# EXPERIMENT 3: Location Analysis
# =====================================================================

def location_analysis(df):
    """
    Analyze geographical data and engagement
    """
    print("\n" + "="*80)
    print("EXPERIMENT 3: Location Analysis")
    print("="*80)
    
    # Region-wise trend distribution
    location_engagement = df.groupby('location').agg({
        'likes': 'mean',
        'retweets': 'mean',
        'tweet_id': 'count'
    }).rename(columns={'tweet_id': 'tweet_count'})
    
    location_engagement = location_engagement.sort_values('tweet_count', ascending=False)
    
    print("\nLocation-wise Tweet Distribution:")
    print(location_engagement.to_string())
    
    # Classify as urban/rural based on characteristics
    urban_locations = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'US', 'UK', 'Singapore']
    df['area_type'] = df['location'].apply(lambda x: 'Urban' if x in urban_locations else 'Rural')
    
    print("\nUrban vs Rural Engagement:")
    print(df.groupby('area_type')[['likes', 'retweets', 'replies']].mean())
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Location Analysis & Engagement', fontsize=16, fontweight='bold')
    
    # 1. Top locations
    location_engagement.head(10)['tweet_count'].plot(kind='bar', ax=axes[0, 0], color='#FF6B6B')
    axes[0, 0].set_title('Tweet Count by Top 10 Locations')
    axes[0, 0].set_ylabel('Number of Tweets')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Urban vs Rural Engagement
    area_engagement = df.groupby('area_type')['likes'].mean()
    area_engagement.plot(kind='bar', ax=axes[0, 1], color=['#4ECDC4', '#95E1D3'])
    axes[0, 1].set_title('Average Likes: Urban vs Rural')
    axes[0, 1].set_ylabel('Average Likes')
    axes[0, 1].set_xticklabels(['Rural', 'Urban'], rotation=0)
    
    # 3. Location-based popularity heatmap
    top_locations = location_engagement.head(8).index
    location_popularity = df[df['location'].isin(top_locations)].groupby('location')['likes'].mean().sort_values(ascending=False)
    axes[1, 0].barh(location_popularity.index, location_popularity.values, color='#F38181')
    axes[1, 0].set_title('Average Likes by Location')
    axes[1, 0].set_xlabel('Average Likes')
    
    # 4. Engagement distribution by area type
    df.boxplot(column='engagement', by='area_type', ax=axes[1, 1])
    axes[1, 1].set_title('Engagement Distribution by Area Type')
    axes[1, 1].set_xlabel('Area Type')
    axes[1, 1].set_ylabel('Total Engagement')
    plt.sca(axes[1, 1])
    plt.xticks(rotation=0)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp3_location_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp3_location_analysis.png")
    
    return fig