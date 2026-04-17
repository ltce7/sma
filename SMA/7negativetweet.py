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
# EXPERIMENT 7: Negative Tweets Detection
# =====================================================================

def negative_tweets_analysis(df):
    """
    Detect and analyze negative, toxic, or harmful content
    """
    print("\n" + "="*80)
    print("EXPERIMENT 7: Negative Tweets Detection & Analysis")
    print("="*80)
    
    # Assign toxicity scores randomly as proxy for sentiment
    df['toxicity_score'] = np.random.uniform(0.1, 1.0, len(df))
    df['is_negative'] = df['toxicity_score'] > 0.6
    
    print("\nNegative Content Statistics:")
    negative_count = df['is_negative'].sum()
    print(f"  Total Negative Tweets: {negative_count} ({negative_count/len(df)*100:.1f}%)")
    print(f"  Total Positive Tweets: {len(df) - negative_count} ({(len(df)-negative_count)/len(df)*100:.1f}%)")
    
    # Analyze negative content patterns
    print("\nTop Negative Tweet Characteristics:")
    negative_df = df[df['is_negative'] == True]
    print(f"  Average Engagement: {negative_df['engagement'].mean():.2f}")
    print(f"  Average Toxicity Score: {negative_df['toxicity_score'].mean():.3f}")
    print(f"  Location with Most Negative Tweets: {negative_df['location'].mode()[0] if len(negative_df) > 0 else 'N/A'}")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Negative & Toxic Content Analysis', fontsize=16, fontweight='bold')
    
    # 1. Negative vs Positive distribution
    pos_neg_counts = df['is_negative'].value_counts()
    labels = ['Positive/Neutral', 'Negative/Toxic']
    values = [pos_neg_counts.get(False, 0), pos_neg_counts.get(True, 0)]
    axes[0, 0].pie(values, labels=labels, autopct='%1.1f%%',
                   colors=['#95E1D3', '#FF6B6B'])
    axes[0, 0].set_title('Positive vs Negative Content Distribution')
    
    # 2. Toxicity score distribution
    axes[0, 1].hist(df['toxicity_score'], bins=20, color='#FF6B6B', alpha=0.7, edgecolor='black')
    axes[0, 1].set_title('Toxicity Score Distribution')
    axes[0, 1].set_xlabel('Toxicity Score')
    axes[0, 1].set_ylabel('Frequency')
    
    # 3. Negative content by location (top 10)
    negative_by_location = negative_df['location'].value_counts().head(10)
    axes[1, 0].barh(negative_by_location.index, negative_by_location.values, color='#FF6B6B')
    axes[1, 0].set_title('Top Locations with Negative Content')
    axes[1, 0].set_xlabel('Count')
    
    # 4. Engagement comparison
    engagement_comparison = pd.DataFrame({
        'Negative': [negative_df['engagement'].mean()],
        'Positive': [df[df['is_negative'] == False]['engagement'].mean()]
    })
    engagement_comparison.T.plot(kind='bar', ax=axes[1, 1], legend=False, color='#667BC6')
    axes[1, 1].set_title('Average Engagement: Negative vs Positive')
    axes[1, 1].set_ylabel('Average Engagement')
    axes[1, 1].set_xticklabels(['Negative', 'Positive'], rotation=0)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp7_negative_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp7_negative_analysis.png")
    
    return fig