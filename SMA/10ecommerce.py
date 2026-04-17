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
# EXPERIMENT 10: E-commerce Reviews Analysis
# =====================================================================

def ecommerce_reviews_analysis():
    """
    Analyze reviews for e-commerce platforms
    """
    print("\n" + "="*80)
    print("EXPERIMENT 10: E-commerce & Food Delivery Reviews Analysis")
    print("="*80)
    
    # Generate mock review data
    platforms = {
        'Amazon': np.random.randint(100, 500, 100),
        'Flipkart': np.random.randint(80, 450, 100),
        'Zomato': np.random.randint(50, 400, 100),
        'Swiggy': np.random.randint(60, 420, 100),
    }
    
    review_data = []
    for platform, ratings in platforms.items():
        for i, rating in enumerate(ratings):
            review_data.append({
                'platform': platform,
                'rating': rating / 100.0 * 5,
                'review_count': len(ratings),
                'customer_satisfaction': (rating / 100.0) * 100
            })
    
    df_reviews = pd.DataFrame(review_data)
    
    print("\nPlatform Review Summary:")
    for platform in df_reviews['platform'].unique():
        platform_data = df_reviews[df_reviews['platform'] == platform]
        print(f"\n  {platform}:")
        print(f"    Avg Rating: {platform_data['rating'].mean():.2f}/5")
        print(f"    Total Reviews: {len(platform_data)}")
        print(f"    Satisfaction: {platform_data['customer_satisfaction'].mean():.1f}%")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('E-commerce & Food Delivery Reviews Analysis', fontsize=16, fontweight='bold')
    
    # 1. Average ratings by platform
    avg_ratings = df_reviews.groupby('platform')['rating'].mean()
    colors_bars = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181']
    axes[0, 0].bar(avg_ratings.index, avg_ratings.values, color=colors_bars)
    axes[0, 0].set_title('Average Rating by Platform')
    axes[0, 0].set_ylabel('Average Rating (out of 5)')
    axes[0, 0].set_ylim([0, 5])
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Rating distribution for each platform
    for i, (platform, group) in enumerate(df_reviews.groupby('platform')):
        axes[0, 1].hist(group['rating'], bins=20, alpha=0.5, label=platform)
    axes[0, 1].set_title('Rating Distribution by Platform')
    axes[0, 1].set_xlabel('Rating')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].legend()
    
    # 3. Customer satisfaction
    satisfaction = df_reviews.groupby('platform')['customer_satisfaction'].mean()
    axes[1, 0].barh(satisfaction.index, satisfaction.values, color=colors_bars)
    axes[1, 0].set_title('Customer Satisfaction Score')
    axes[1, 0].set_xlabel('Satisfaction (%)')
    
    # 4. Platform comparison
    platform_stats = df_reviews.groupby('platform').agg({
        'rating': ['mean', 'std'],
        'customer_satisfaction': 'mean'
    })
    
    x_pos = np.arange(len(avg_ratings))
    axes[1, 1].bar(x_pos - 0.2, avg_ratings.values, 0.4, label='Avg Rating', color='#667BC6')
    axes[1, 1].bar(x_pos + 0.2, satisfaction.values/5, 0.4, label='Satisfaction/5', color='#FF6B6B')
    axes[1, 1].set_xticks(x_pos)
    axes[1, 1].set_xticklabels(avg_ratings.index, rotation=45)
    axes[1, 1].set_title('Platform Comparison')
    axes[1, 1].set_ylabel('Score')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp10_ecommerce_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp10_ecommerce_analysis.png")
    
    return fig