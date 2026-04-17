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
# EXPERIMENT 9: Dashboard Creation Concepts
# =====================================================================

def create_dashboard_mockup():
    """
    Create a mockup of Power BI-style dashboard
    """
    print("\n" + "="*80)
    print("EXPERIMENT 9: Dashboard Creation (Power BI Concepts)")
    print("="*80)
    
    # Generate sample dashboard data
    dates = pd.date_range(start='2025-03-17', periods=30)
    dashboard_data = pd.DataFrame({
        'date': dates,
        'total_posts': np.random.randint(50, 200, 30),
        'total_engagement': np.random.randint(500, 5000, 30),
        'avg_likes': np.random.randint(100, 1000, 30),
        'avg_sentiment': np.random.uniform(0.3, 1.0, 30),
        'reach': np.random.randint(10000, 100000, 30)
    })
    
    print("\nDashboard Metrics Summary:")
    print(f"  Total Posts (30 days): {dashboard_data['total_posts'].sum()}")
    print(f"  Total Engagement: {dashboard_data['total_engagement'].sum():,}")
    print(f"  Average Daily Reach: {dashboard_data['reach'].mean():,.0f}")
    print(f"  Average Sentiment Score: {dashboard_data['avg_sentiment'].mean():.3f}")
    
    # Create dashboard visualization
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)
    fig.suptitle('Social Media Analytics Dashboard (Real-time Mock)', fontsize=18, fontweight='bold')
    
    # 1. Total Posts Over Time
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.plot(dashboard_data['date'], dashboard_data['total_posts'], marker='o', 
             linewidth=2, color='#667BC6', label='Posts')
    ax1.fill_between(dashboard_data['date'], dashboard_data['total_posts'], alpha=0.3, color='#667BC6')
    ax1.set_title('Daily Posts Over Time', fontweight='bold')
    ax1.set_ylabel('Number of Posts')
    ax1.grid(True, alpha=0.3)
    
    # 2. Key Metrics (cards)
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.axis('off')
    metrics_text = f"""
    KEY METRICS
    ─────────────
    Total Posts: {dashboard_data['total_posts'].sum()}
    Total Reach: {dashboard_data['reach'].sum():,}
    Avg Engagement: {dashboard_data['total_engagement'].mean():.0f}
    Sentiment: {dashboard_data['avg_sentiment'].mean():.2f}
    """
    ax2.text(0.1, 0.5, metrics_text, fontsize=11, family='monospace', 
             bbox=dict(boxstyle='round', facecolor='#E3F2FD', alpha=0.8))
    
    # 3. Engagement Trend
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.plot(dashboard_data['date'], dashboard_data['total_engagement'], 
             marker='s', color='#FF6B6B', linewidth=2)
    ax3.fill_between(dashboard_data['date'], dashboard_data['total_engagement'], 
                     alpha=0.3, color='#FF6B6B')
    ax3.set_title('Engagement Trend', fontweight='bold')
    ax3.set_ylabel('Total Engagement')
    ax3.tick_params(axis='x', rotation=45)
    ax3.grid(True, alpha=0.3)
    
    # 4. Average Likes
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.bar(dashboard_data['date'].dt.day, dashboard_data['avg_likes'], color='#4ECDC4', alpha=0.8)
    ax4.set_title('Average Likes by Day', fontweight='bold')
    ax4.set_ylabel('Avg Likes')
    ax4.set_xlabel('Day of Month')
    
    # 5. Reach Distribution
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.plot(dashboard_data['date'], dashboard_data['reach'], marker='D', 
             color='#95E1D3', linewidth=2, markersize=5)
    ax5.fill_between(dashboard_data['date'], dashboard_data['reach'], alpha=0.3, color='#95E1D3')
    ax5.set_title('Reach Growth', fontweight='bold')
    ax5.set_ylabel('Reach')
    ax5.tick_params(axis='x', rotation=45)
    ax5.grid(True, alpha=0.3)
    
    # 6. Sentiment Trend
    ax6 = fig.add_subplot(gs[2, :2])
    ax6.plot(dashboard_data['date'], dashboard_data['avg_sentiment'], 
             marker='o', color='#FFE66D', linewidth=2.5)
    ax6.fill_between(dashboard_data['date'], dashboard_data['avg_sentiment'], 
                     alpha=0.4, color='#FFE66D')
    ax6.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Neutral Line')
    ax6.set_title('Sentiment Score Trend', fontweight='bold')
    ax6.set_ylabel('Sentiment Score')
    ax6.set_xlabel('Date')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # 7. Performance Summary
    ax7 = fig.add_subplot(gs[2, 2])
    ax7.axis('off')
    summary_text = """
    TOP PERFORMERS
    ───────────────
    Best Day: Day {0}
    Peak Engagement: {1}
    Highest Reach: {2:,}
    Avg Sentiment: {3:.2f}
    """.format(
        dashboard_data['total_engagement'].idxmax() + 1,
        dashboard_data['total_engagement'].max(),
        dashboard_data['reach'].max(),
        dashboard_data['avg_sentiment'].mean()
    )
    ax7.text(0.05, 0.5, summary_text, fontsize=10, family='monospace',
             bbox=dict(boxstyle='round', facecolor='#FFF9C4', alpha=0.8))
    
    plt.savefig('/home/claude/exp9_dashboard.png', dpi=300, bbox_inches='tight')
    print("\n✓ Dashboard visualization saved: exp9_dashboard.png")
    
    return fig