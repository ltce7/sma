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
# EXPERIMENT 1: Twitter (X) Data Analysis and Visualization
# =====================================================================

def generate_twitter_data(topic='AI Tools', num_tweets=500):
    """
    Generate mock Twitter/X data for analysis
    """
    topics_keywords = {
        'AI Tools': ['ChatGPT', 'Claude', 'Gemini', 'AI', 'machine learning', 'LLM'],
        'EV': ['Tesla', 'electric vehicle', 'EV', 'charging', 'sustainability'],
        'IPL 2026': ['IPL', 'cricket', 'T20', 'Mumbai Indians', 'CSK'],
        'Startups': ['startup', 'unicorn', 'funding', 'innovation', 'entrepreneur'],
    }
    
    locations = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 
                 'Kolkata', 'US', 'UK', 'Singapore', 'Dubai', 'Toronto']
    
    users = [f'user_{i}' for i in range(1, 100)]
    
    data = []
    keywords = topics_keywords.get(topic, topics_keywords['AI Tools'])
    
    for i in range(num_tweets):
        tweet_date = datetime.now() - timedelta(days=random.randint(0, 30))
        keywords_count = random.randint(1, 3)
        selected_keywords = random.sample(keywords, min(keywords_count, len(keywords)))
        
        data.append({
            'tweet_id': i + 1,
            'username': random.choice(users),
            'text': f"Tweet about {' '.join(selected_keywords)} - this is awesome! #{selected_keywords[0]}",
            'likes': random.randint(10, 10000),
            'retweets': random.randint(5, 5000),
            'replies': random.randint(0, 1000),
            'location': random.choice(locations),
            'date': tweet_date,
            'is_verified': random.choice([True, False, False, False]),
            'followers': random.randint(100, 100000),
        })
    
    return pd.DataFrame(data)

def twitter_data_analysis(df, topic='AI Tools'):
    """
    Perform Twitter data analysis and create visualizations
    """
    print("\n" + "="*80)
    print(f"EXPERIMENT 1: Twitter (X) Data Analysis - Topic: {topic}")
    print("="*80)
    
    # Basic Statistics
    print(f"\nTotal Tweets Analyzed: {len(df)}")
    print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
    print(f"Average Likes: {df['likes'].mean():.2f}")
    print(f"Average Retweets: {df['retweets'].mean():.2f}")
    
    # Top engaged tweets
    print("\nTop 5 Most Engaged Tweets:")
    df['engagement'] = df['likes'] + df['retweets'] + df['replies']
    top_tweets = df.nlargest(5, 'engagement')[['username', 'likes', 'retweets', 'engagement']]
    print(top_tweets.to_string())
    
    # Location-wise distribution
    location_stats = df['location'].value_counts()
    print(f"\nTop Locations: \n{location_stats.head()}")
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'Twitter Analytics: {topic}', fontsize=16, fontweight='bold')
    
    # 1. Engagement Metric Distribution
    metrics = ['Likes', 'Retweets', 'Replies']
    means = [df['likes'].mean(), df['retweets'].mean(), df['replies'].mean()]
    axes[0, 0].bar(metrics, means, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    axes[0, 0].set_title('Average Engagement Metrics')
    axes[0, 0].set_ylabel('Average Count')
    
    # 2. Top 10 Locations
    location_stats.head(10).plot(kind='barh', ax=axes[0, 1], color='#95E1D3')
    axes[0, 1].set_title('Top 10 Locations')
    axes[0, 1].set_xlabel('Number of Tweets')
    
    # 3. Likes vs Retweets
    axes[1, 0].scatter(df['likes'], df['retweets'], alpha=0.6, color='#F38181', s=50)
    axes[1, 0].set_title('Likes vs Retweets Correlation')
    axes[1, 0].set_xlabel('Likes')
    axes[1, 0].set_ylabel('Retweets')
    
    # 4. Verified vs Non-Verified Engagement
    verified_engagement = df.groupby('is_verified')['engagement'].mean()
    verified_engagement.plot(kind='bar', ax=axes[1, 1], color=['#AA96DA', '#FCBAD3'])
    axes[1, 1].set_title('Engagement: Verified vs Non-Verified Users')
    axes[1, 1].set_xticklabels(['Non-Verified', 'Verified'], rotation=0)
    axes[1, 1].set_ylabel('Average Engagement')
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp1_twitter_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp1_twitter_analysis.png")
    
    return df, fig