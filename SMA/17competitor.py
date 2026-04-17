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
# EXPERIMENT 17: Competitor Analysis
# =====================================================================

def competitor_analysis():
    """
    Analyze competitors using social media metrics
    """
    print("\n" + "="*80)
    print("EXPERIMENT 17: Competitor Analysis Using Social Media")
    print("="*80)
    
    competitors = {
        'Mamaearth vs Himalaya': {
            'Mamaearth': {'followers': 2150000, 'engagement_rate': 3.2, 'posts_per_month': 24, 
                         'avg_likes': 35000, 'sentiment': 4.2},
            'Himalaya': {'followers': 1850000, 'engagement_rate': 2.1, 'posts_per_month': 18,
                        'avg_likes': 22000, 'sentiment': 4.0},
        },
        'IndiGo vs Air India': {
            'IndiGo': {'followers': 3200000, 'engagement_rate': 2.8, 'posts_per_month': 32,
                      'avg_likes': 18000, 'sentiment': 3.8},
            'Air India': {'followers': 2800000, 'engagement_rate': 1.9, 'posts_per_month': 20,
                         'avg_likes': 12000, 'sentiment': 3.5},
        },
        'Coursera vs Udemy': {
            'Coursera': {'followers': 1200000, 'engagement_rate': 2.5, 'posts_per_month': 28,
                        'avg_likes': 15000, 'sentiment': 4.1},
            'Udemy': {'followers': 980000, 'engagement_rate': 3.1, 'posts_per_month': 35,
                     'avg_likes': 22000, 'sentiment': 3.9},
        }
    }
    
    print("\nCompetitor Comparison Analysis:")
    for category, brands in competitors.items():
        print(f"\n  {category}:")
        for brand, metrics in brands.items():
            print(f"    {brand}:")
            print(f"      Followers: {metrics['followers']:,}")
            print(f"      Engagement Rate: {metrics['engagement_rate']:.1f}%")
            print(f"      Posts/Month: {metrics['posts_per_month']}")
            print(f"      Avg Sentiment: {metrics['sentiment']:.1f}/5")
    
    # Create visualization for one category
    category_to_visualize = 'Coursera vs Udemy'
    brands_data = competitors[category_to_visualize]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'Competitor Analysis: {category_to_visualize}', fontsize=16, fontweight='bold')
    
    brand_names = list(brands_data.keys())
    
    # 1. Follower comparison
    followers = [brands_data[b]['followers']/1000000 for b in brand_names]
    axes[0, 0].bar(brand_names, followers, color=['#667BC6', '#FF6B6B'])
    axes[0, 0].set_title('Follower Count (in Millions)')
    axes[0, 0].set_ylabel('Followers (M)')
    
    # 2. Engagement rate
    engagement_rates = [brands_data[b]['engagement_rate'] for b in brand_names]
    axes[0, 1].barh(brand_names, engagement_rates, color=['#667BC6', '#FF6B6B'])
    axes[0, 1].set_title('Engagement Rate')
    axes[0, 1].set_xlabel('Engagement Rate (%)')
    
    # 3. Content frequency
    posts_per_month = [brands_data[b]['posts_per_month'] for b in brand_names]
    axes[1, 0].bar(brand_names, posts_per_month, color=['#667BC6', '#FF6B6B'])
    axes[1, 0].set_title('Posts per Month')
    axes[1, 0].set_ylabel('Number of Posts')
    
    # 4. Sentiment comparison
    sentiments = [brands_data[b]['sentiment'] for b in brand_names]
    axes[1, 1].bar(brand_names, sentiments, color=['#667BC6', '#FF6B6B'])
    axes[1, 1].set_title('Average Sentiment Score')
    axes[1, 1].set_ylabel('Sentiment (out of 5)')
    axes[1, 1].set_ylim([0, 5])
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp17_competitor_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp17_competitor_analysis.png")
    
    return fig