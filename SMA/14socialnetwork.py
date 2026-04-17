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
# EXPERIMENT 14: Social Network Analysis
# =====================================================================

def social_network_analysis():
    """
    Perform social network analysis using graph concepts
    """
    print("\n" + "="*80)
    print("EXPERIMENT 14: Social Network Data Analysis")
    print("="*80)
    
    # Simulate network metrics
    users_count = 500
    connections_count = 1500
    
    network_metrics = {
        'Total Users': users_count,
        'Total Connections': connections_count,
        'Network Density': connections_count / (users_count * (users_count - 1) / 2),
        'Avg Connections per User': connections_count / users_count,
        'Clustering Coefficient': round(np.random.uniform(0.3, 0.7), 3),
    }
    
    # Identify influencers (top 10% by degree centrality proxy)
    influencer_count = int(users_count * 0.1)
    
    # Community detection simulation
    communities = {
        'Tech Enthusiasts': influencer_count // 2,
        'Content Creators': influencer_count // 4,
        'Casual Users': users_count - influencer_count,
        'Brands': influencer_count // 4,
    }
    
    print("\nNetwork Analysis Metrics:")
    for metric, value in network_metrics.items():
        if isinstance(value, float):
            print(f"  {metric}: {value:.4f}")
        else:
            print(f"  {metric}: {value}")
    
    print(f"\nInfluencer Identification:")
    print(f"  Top Influencers Detected: {influencer_count}")
    print(f"  Influence Score Range: 0.65 - 0.98")
    
    print(f"\nCommunity Detection:")
    for community, count in communities.items():
        percentage = (count / users_count) * 100
        print(f"  {community}: {count} users ({percentage:.1f}%)")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Social Network Analysis', fontsize=16, fontweight='bold')
    
    # 1. Network metrics
    metrics_names = ['Density', 'Avg\nConnections', 'Clustering\nCoeff']
    metrics_values = [
        network_metrics['Network Density'] * 100,
        network_metrics['Avg Connections per User'],
        network_metrics['Clustering Coefficient'] * 100
    ]
    axes[0, 0].bar(metrics_names, metrics_values, color=['#667BC6', '#FF6B6B', '#95E1D3'])
    axes[0, 0].set_title('Network Metrics Overview')
    axes[0, 0].set_ylabel('Value')
    
    # 2. Community distribution
    communities_names = list(communities.keys())
    communities_sizes = list(communities.values())
    axes[0, 1].pie(communities_sizes, labels=communities_names, autopct='%1.1f%%',
                   colors=['#667BC6', '#FF6B6B', '#95E1D3', '#FFE66D'])
    axes[0, 1].set_title('Community Distribution')
    
    # 3. Degree centrality distribution (simulated)
    centrality_scores = np.random.exponential(0.3, 100)
    centrality_scores = np.clip(centrality_scores, 0, 1)
    axes[1, 0].hist(centrality_scores, bins=20, color='#667BC6', edgecolor='black', alpha=0.7)
    axes[1, 0].set_title('Degree Centrality Distribution')
    axes[1, 0].set_xlabel('Centrality Score')
    axes[1, 0].set_ylabel('Frequency')
    
    # 4. Influencer vs Regular Users
    influencer_engagement = [
        np.random.uniform(5000, 50000) for _ in range(influencer_count)
    ]
    regular_engagement = [
        np.random.uniform(10, 1000) for _ in range(users_count - influencer_count)
    ]
    
    axes[1, 1].boxplot([influencer_engagement, regular_engagement],
                       labels=['Influencers', 'Regular Users'],
                       patch_artist=True)
    axes[1, 1].set_title('Engagement: Influencers vs Regular Users')
    axes[1, 1].set_ylabel('Engagement Count')
    
    # Color the boxes
    for patch, color in zip(axes[1, 1].artists, ['#FF6B6B', '#95E1D3']):
        patch.set_facecolor(color)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp14_network_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp14_network_analysis.png")
    
    return fig