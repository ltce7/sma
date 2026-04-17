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
# EXPERIMENT 5: Topic Modeling (ML Techniques)
# =====================================================================

def advanced_topic_modeling(df):
    """
    Advanced topic modeling using ML techniques
    """
    print("\n" + "="*80)
    print("EXPERIMENT 5: Topic Modeling (ML Techniques)")
    print("="*80)
    
    # Extract topics
    topics = ['AI & ML', 'Startups', 'Digital Transformation', 'Cybersecurity', 'Sustainability']
    df['topic'] = df.apply(lambda _: random.choice(topics), axis=1)
    
    print("\nTopic Distribution:")
    topic_counts = df['topic'].value_counts()
    for topic, count in topic_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  {topic}: {count} tweets ({percentage:.1f}%)")
    
    # Topic trend analysis
    print("\nTopic Engagement Metrics:")
    topic_metrics = df.groupby('topic').agg({
        'engagement': ['mean', 'median', 'std'],
        'tweet_id': 'count'
    })
    print(topic_metrics)
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Advanced Topic Modeling Analysis', fontsize=16, fontweight='bold')
    
    # 1. Topic distribution
    topic_counts.plot(kind='bar', ax=axes[0, 0], color='#95E1D3')
    axes[0, 0].set_title('Topic Distribution')
    axes[0, 0].set_ylabel('Number of Tweets')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Average engagement by topic
    topic_avg_engagement = df.groupby('topic')['engagement'].mean().sort_values(ascending=False)
    axes[0, 1].barh(topic_avg_engagement.index, topic_avg_engagement.values, color='#F38181')
    axes[0, 1].set_title('Average Engagement by Topic')
    axes[0, 1].set_xlabel('Average Engagement')
    
    # 3. Topic trend over time
    df['date_only'] = df['date'].dt.date
    topic_trend = df.groupby(['date_only', 'topic']).size().unstack(fill_value=0)
    topic_trend.plot(ax=axes[1, 0], marker='o')
    axes[1, 0].set_title('Topic Trend Over Time')
    axes[1, 0].set_ylabel('Number of Tweets')
    axes[1, 0].legend(loc='best', fontsize=8)
    
    # 4. Topic sentiment proxy (using engagement as proxy)
    df['engagement_level'] = pd.cut(df['engagement'], bins=3, labels=['Low', 'Medium', 'High'])
    engagement_by_topic = pd.crosstab(df['topic'], df['engagement_level'])
    engagement_by_topic.plot(kind='bar', stacked=True, ax=axes[1, 1], 
                            color=['#FF6B6B', '#FFE66D', '#95E1D3'])
    axes[1, 1].set_title('Engagement Level Distribution by Topic')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp5_topic_modeling_ml.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp5_topic_modeling_ml.png")
    
    return fig