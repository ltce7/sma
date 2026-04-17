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
# EXPERIMENT 12: Short-form vs Traditional Content
# =====================================================================

def content_type_comparison():
    """
    Compare short-form content (Reels/Shorts) vs traditional posts
    """
    print("\n" + "="*80)
    print("EXPERIMENT 12: Short-form vs Traditional Content Analysis")
    print("="*80)
    
    content_comparison = {
        'Reels': {
            'avg_views': 125000,
            'avg_likes': 2500,
            'avg_shares': 800,
            'avg_comments': 450,
            'save_rate': 15.2,
            'engagement_rate': 2.8
        },
        'Shorts': {
            'avg_views': 95000,
            'avg_likes': 1800,
            'avg_shares': 600,
            'avg_comments': 320,
            'save_rate': 12.3,
            'engagement_rate': 2.1
        },
        'Traditional Posts': {
            'avg_views': 45000,
            'avg_likes': 900,
            'avg_shares': 150,
            'avg_comments': 200,
            'save_rate': 5.1,
            'engagement_rate': 1.2
        },
        'Memes': {
            'avg_views': 180000,
            'avg_likes': 4200,
            'avg_shares': 2100,
            'avg_comments': 1200,
            'save_rate': 22.5,
            'engagement_rate': 4.1
        }
    }
    
    print("\nContent Type Performance Metrics:")
    for content_type, metrics in content_comparison.items():
        print(f"\n  {content_type}:")
        print(f"    Avg Views: {metrics['avg_views']:,}")
        print(f"    Avg Engagement Rate: {metrics['engagement_rate']:.1f}%")
        print(f"    Save Rate: {metrics['save_rate']:.1f}%")
        print(f"    Total Interactions: {metrics['avg_likes'] + metrics['avg_shares'] + metrics['avg_comments']}")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Short-form vs Traditional Content Performance', fontsize=16, fontweight='bold')
    
    content_types = list(content_comparison.keys())
    
    # 1. Average views
    views = [content_comparison[c]['avg_views'] for c in content_types]
    axes[0, 0].bar(content_types, views, color=['#667BC6', '#FF6B6B', '#95E1D3', '#FFE66D'])
    axes[0, 0].set_title('Average Views by Content Type')
    axes[0, 0].set_ylabel('Views')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Engagement rate
    engagement = [content_comparison[c]['engagement_rate'] for c in content_types]
    axes[0, 1].barh(content_types, engagement, color=['#667BC6', '#FF6B6B', '#95E1D3', '#FFE66D'])
    axes[0, 1].set_title('Engagement Rate by Content Type')
    axes[0, 1].set_xlabel('Engagement Rate (%)')
    
    # 3. Interaction breakdown
    interaction_data = {
        c: {
            'Likes': content_comparison[c]['avg_likes'],
            'Shares': content_comparison[c]['avg_shares'],
            'Comments': content_comparison[c]['avg_comments']
        }
        for c in content_types
    }
    
    x = np.arange(len(content_types))
    width = 0.25
    
    likes = [interaction_data[c]['Likes'] for c in content_types]
    shares = [interaction_data[c]['Shares'] for c in content_types]
    comments = [interaction_data[c]['Comments'] for c in content_types]
    
    axes[1, 0].bar(x - width, likes, width, label='Likes', color='#FF6B6B')
    axes[1, 0].bar(x, shares, width, label='Shares', color='#4ECDC4')
    axes[1, 0].bar(x + width, comments, width, label='Comments', color='#95E1D3')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(content_types, rotation=45)
    axes[1, 0].set_title('Interaction Metrics by Content Type')
    axes[1, 0].set_ylabel('Average Count')
    axes[1, 0].legend()
    
    # 4. Save rate comparison
    save_rates = [content_comparison[c]['save_rate'] for c in content_types]
    axes[1, 1].plot(content_types, save_rates, marker='o', linewidth=2.5, 
                    markersize=10, color='#667BC6')
    axes[1, 1].fill_between(range(len(content_types)), save_rates, alpha=0.3, color='#667BC6')
    axes[1, 1].set_title('Save Rate by Content Type')
    axes[1, 1].set_ylabel('Save Rate (%)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp12_content_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp12_content_comparison.png")
    
    return fig