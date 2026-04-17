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
# EXPERIMENT 11: Brand Analysis
# =====================================================================

def brand_analysis():
    """
    Analyze social media presence and sentiment of brands
    """
    print("\n" + "="*80)
    print("EXPERIMENT 11: Brand Analysis (Social Media Sentiment)")
    print("="*80)
    
    brands = {
        'Apple': {'posts': 450, 'followers': 5000000, 'engagement_rate': 8.5},
        'Samsung': {'posts': 380, 'followers': 3200000, 'engagement_rate': 6.2},
        'Tesla': {'posts': 290, 'followers': 4800000, 'engagement_rate': 12.3},
        'Zomato': {'posts': 650, 'followers': 1800000, 'engagement_rate': 7.8},
        'Swiggy': {'posts': 580, 'followers': 1500000, 'engagement_rate': 6.9},
    }
    
    brand_sentiment = {}
    for brand in brands.keys():
        brand_sentiment[brand] = {
            'positive': np.random.uniform(50, 85),
            'neutral': np.random.uniform(10, 30),
            'negative': np.random.uniform(5, 20)
        }
    
    print("\nBrand Performance Summary:")
    for brand, metrics in brands.items():
        print(f"\n  {brand}:")
        print(f"    Total Posts: {metrics['posts']}")
        print(f"    Followers: {metrics['followers']:,}")
        print(f"    Engagement Rate: {metrics['engagement_rate']:.1f}%")
        print(f"    Sentiment - Positive: {brand_sentiment[brand]['positive']:.1f}%, "
              f"Negative: {brand_sentiment[brand]['negative']:.1f}%")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Brand Analysis & Social Media Sentiment', fontsize=16, fontweight='bold')
    
    # 1. Followers comparison
    followers = {b: v['followers']/1000000 for b, v in brands.items()}
    axes[0, 0].bar(followers.keys(), followers.values(), color='#667BC6')
    axes[0, 0].set_title('Follower Count (in Millions)')
    axes[0, 0].set_ylabel('Followers (M)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Engagement rate
    engagement = {b: v['engagement_rate'] for b, v in brands.items()}
    axes[0, 1].barh(list(engagement.keys()), list(engagement.values()), color='#FF6B6B')
    axes[0, 1].set_title('Engagement Rate (%)')
    axes[0, 1].set_xlabel('Engagement Rate')
    
    # 3. Sentiment distribution (stacked bar)
    brand_names = list(brand_sentiment.keys())
    positive = [brand_sentiment[b]['positive'] for b in brand_names]
    neutral = [brand_sentiment[b]['neutral'] for b in brand_names]
    negative = [brand_sentiment[b]['negative'] for b in brand_names]
    
    x = np.arange(len(brand_names))
    axes[1, 0].bar(x, positive, label='Positive', color='#95E1D3')
    axes[1, 0].bar(x, neutral, bottom=positive, label='Neutral', color='#FFE66D')
    axes[1, 0].bar(x, negative, bottom=np.array(positive)+np.array(neutral), 
                   label='Negative', color='#FF6B6B')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(brand_names, rotation=45)
    axes[1, 0].set_title('Brand Sentiment Distribution')
    axes[1, 0].set_ylabel('Percentage')
    axes[1, 0].legend()
    
    # 4. Posts vs Engagement
    posts = {b: v['posts'] for b, v in brands.items()}
    axes[1, 1].scatter(list(posts.values()), list(engagement.values()), s=200, 
                       c=range(len(brands)), cmap='viridis', alpha=0.7)
    for i, brand in enumerate(brand_names):
        axes[1, 1].annotate(brand, (posts[brand], engagement[brand]), 
                           fontsize=9, ha='right')
    axes[1, 1].set_title('Posts vs Engagement Rate')
    axes[1, 1].set_xlabel('Number of Posts')
    axes[1, 1].set_ylabel('Engagement Rate (%)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp11_brand_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp11_brand_analysis.png")
    
    return fig