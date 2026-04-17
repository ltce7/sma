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
# EXPERIMENT 13: Creative Content Campaigns
# =====================================================================

def creative_campaigns_design():
    """
    Design creative campaigns for different purposes
    """
    print("\n" + "="*80)
    print("EXPERIMENT 13: Creative Content & Campaign Design")
    print("="*80)
    
    campaigns = {
        'Digital India': {
            'target_audience': 'Youth, Tech Enthusiasts',
            'message': 'Empower India through Digital Innovation',
            'platforms': ['Twitter', 'Instagram', 'LinkedIn'],
            'budget': 500000,
            'expected_reach': 5000000,
            'expected_ctr': 3.5
        },
        'AI Awareness': {
            'target_audience': 'Students, Professionals',
            'message': 'Understand AI: The Future is Here',
            'platforms': ['Twitter', 'YouTube', 'TikTok'],
            'budget': 300000,
            'expected_reach': 3000000,
            'expected_ctr': 2.8
        },
        'Sustainable Brands': {
            'target_audience': 'Eco-conscious Consumers',
            'message': 'Green Choices for a Better Tomorrow',
            'platforms': ['Instagram', 'Pinterest', 'Facebook'],
            'budget': 400000,
            'expected_reach': 4000000,
            'expected_ctr': 3.2
        },
        'Mental Health': {
            'target_audience': 'All Ages',
            'message': 'Your Mental Health Matters',
            'platforms': ['Twitter', 'TikTok', 'YouTube'],
            'budget': 250000,
            'expected_reach': 2500000,
            'expected_ctr': 4.1
        }
    }
    
    print("\nCampaign Strategy Summary:")
    for campaign, details in campaigns.items():
        print(f"\n  {campaign}:")
        print(f"    Target Audience: {details['target_audience']}")
        print(f"    Budget: ₹{details['budget']:,}")
        print(f"    Expected Reach: {details['expected_reach']:,}")
        print(f"    Expected CTR: {details['expected_ctr']:.1f}%")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Creative Campaign Strategy & Analysis', fontsize=16, fontweight='bold')
    
    campaign_names = list(campaigns.keys())
    
    # 1. Budget allocation
    budgets = [campaigns[c]['budget']/100000 for c in campaign_names]  # Convert to lakhs
    axes[0, 0].bar(campaign_names, budgets, color=['#FF6B6B', '#4ECDC4', '#95E1D3', '#FFE66D'])
    axes[0, 0].set_title('Campaign Budget Allocation (₹ in Lakhs)')
    axes[0, 0].set_ylabel('Budget (Lakhs)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Expected reach
    reaches = [campaigns[c]['expected_reach']/1000000 for c in campaign_names]  # Convert to millions
    axes[0, 1].barh(campaign_names, reaches, color=['#FF6B6B', '#4ECDC4', '#95E1D3', '#FFE66D'])
    axes[0, 1].set_title('Expected Reach (in Millions)')
    axes[0, 1].set_xlabel('Reach (Millions)')
    
    # 3. Click-through rate
    ctrs = [campaigns[c]['expected_ctr'] for c in campaign_names]
    axes[1, 0].plot(campaign_names, ctrs, marker='D', linewidth=2.5, 
                    markersize=10, color='#667BC6')
    axes[1, 0].set_title('Expected Click-Through Rate')
    axes[1, 0].set_ylabel('CTR (%)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # 4. ROI potential
    roi = [(campaigns[c]['expected_reach'] / (campaigns[c]['budget']/100000)) for c in campaign_names]
    axes[1, 1].bar(campaign_names, roi, color=['#FF6B6B', '#4ECDC4', '#95E1D3', '#FFE66D'])
    axes[1, 1].set_title('Reach per Lakh Budget (ROI Indicator)')
    axes[1, 1].set_ylabel('Reach per Lakh')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp13_campaigns.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp13_campaigns.png")
    
    return fig