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
# EXPERIMENT 2: Content Analysis (Topic Modeling)
# =====================================================================

def topic_modeling_analysis(df):
    """
    Perform topic modeling on tweet content
    """
    print("\n" + "="*80)
    print("EXPERIMENT 2: Content Analysis (Topic Modeling)")
    print("="*80)
    
    # Extract topics from text
    all_text = ' '.join(df['text'].str.lower())
    words = all_text.split()
    
    # Filter meaningful words
    stopwords = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'or', 'but', 'about'}
    meaningful_words = [w for w in words if len(w) > 3 and w not in stopwords]
    
    word_freq = Counter(meaningful_words)
    top_topics = word_freq.most_common(10)
    
    print("\nTop 10 Topics/Keywords:")
    for i, (topic, freq) in enumerate(top_topics, 1):
        print(f"{i}. {topic}: {freq} mentions")
    
    # Human vs AI content detection
    ai_keywords = ['ai', 'machine learning', 'chatgpt', 'claude', 'gemini', 'neural', 'algorithm']
    df['content_type'] = df['text'].str.lower().apply(
        lambda x: 'AI-Generated' if any(kw in x for kw in ai_keywords) else 'Human-Generated'
    )
    
    print("\nContent Distribution:")
    print(df['content_type'].value_counts())
    
    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Content Analysis & Topic Modeling', fontsize=16, fontweight='bold')
    
    # Top topics bar chart
    topics, counts = zip(*top_topics)
    axes[0].barh(topics, counts, color='#667BC6')
    axes[0].set_title('Top 10 Topics/Keywords')
    axes[0].set_xlabel('Frequency')
    
    # Content type pie chart
    content_counts = df['content_type'].value_counts()
    axes[1].pie(content_counts, labels=content_counts.index, autopct='%1.1f%%',
                colors=['#FF6B6B', '#4ECDC4'], startangle=90)
    axes[1].set_title('AI-Generated vs Human-Generated Content')
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp2_topic_modeling.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp2_topic_modeling.png")
    
    return fig