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
# EXPERIMENT 6: Sentiment Analysis
# =====================================================================

def sentiment_analysis(df):
    """
    Perform sentiment analysis on tweets
    """
    print("\n" + "="*80)
    print("EXPERIMENT 6: Sentiment Analysis")
    print("="*80)
    
    # Assign sentiments based on engagement proxy
    df['sentiment_score'] = (df['engagement'] - df['engagement'].min()) / (df['engagement'].max() - df['engagement'].min())
    
    def assign_sentiment(score):
        if score > 0.6:
            return 'Positive'
        elif score > 0.3:
            return 'Neutral'
        else:
            return 'Negative'
    
    df['sentiment'] = df['sentiment_score'].apply(assign_sentiment)
    
    print("\nSentiment Distribution:")
    sentiment_counts = df['sentiment'].value_counts()
    for sentiment, count in sentiment_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  {sentiment}: {count} tweets ({percentage:.1f}%)")
    
    # Topics sentiment analysis
    print("\nSentiment Distribution by Topic:")
    topic_sentiment = pd.crosstab(df['topic'], df['sentiment'])
    print(topic_sentiment)
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Sentiment Analysis Results', fontsize=16, fontweight='bold')
    
    # 1. Overall sentiment distribution
    colors = {'Positive': '#95E1D3', 'Neutral': '#FFE66D', 'Negative': '#FF6B6B'}
    sentiment_colors = [colors.get(s, '#95E1D3') for s in sentiment_counts.index]
    axes[0, 0].pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%',
                   colors=sentiment_colors, startangle=90)
    axes[0, 0].set_title('Overall Sentiment Distribution')
    
    # 2. Sentiment by topic (stacked bar)
    topic_sentiment.T.plot(kind='bar', stacked=True, ax=axes[0, 1], 
                           color=['#FF6B6B', '#95E1D3', '#FFE66D', '#F38181', '#FCBAD3'])
    axes[0, 1].set_title('Sentiment Distribution by Topic')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. Sentiment score distribution
    axes[1, 0].hist(df['sentiment_score'], bins=20, color='#667BC6', edgecolor='black', alpha=0.7)
    axes[1, 0].set_title('Sentiment Score Distribution')
    axes[1, 0].set_xlabel('Sentiment Score')
    axes[1, 0].set_ylabel('Frequency')
    
    # 4. Sentiment vs Engagement
    sentiment_engagement = df.groupby('sentiment')['engagement'].mean()
    axes[1, 1].bar(sentiment_engagement.index, sentiment_engagement.values, 
                   color=['#FF6B6B', '#FFE66D', '#95E1D3'])
    axes[1, 1].set_title('Average Engagement by Sentiment')
    axes[1, 1].set_ylabel('Average Engagement')
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp6_sentiment_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp6_sentiment_analysis.png")
    
    return fig