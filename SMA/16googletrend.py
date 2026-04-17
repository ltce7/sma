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
# EXPERIMENT 16: Google Trends Analysis
# =====================================================================

def google_trends_analysis():
    """
    Analyze Google Trends data
    """
    print("\n" + "="*80)
    print("EXPERIMENT 16: Google Trends Analysis")
    print("="*80)
    
    # Simulated Google Trends data
    trends_data = {
        'ChatGPT': np.array([45, 52, 58, 65, 72, 78, 85, 88, 90, 92, 91, 89]),
        'Gemini': np.array([20, 25, 35, 45, 55, 68, 75, 82, 85, 87, 86, 84]),
        'Claude': np.array([15, 18, 22, 28, 35, 42, 50, 58, 65, 72, 78, 82]),
    }
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    print("\nGoogle Trends Summary (AI Tools):")
    for tool, values in trends_data.items():
        print(f"\n  {tool}:")
        print(f"    Peak Interest: {values.max()} (Month {months[values.argmax()]})")
        print(f"    Current Interest: {values[-1]}")
        print(f"    Average Interest: {values.mean():.1f}")
        print(f"    Growth Rate: {((values[-1] - values[0]) / values[0] * 100):.1f}%")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Google Trends Analysis', fontsize=16, fontweight='bold')
    
    # 1. Trends comparison over time
    for tool, values in trends_data.items():
        axes[0, 0].plot(months, values, marker='o', linewidth=2.5, label=tool)
    axes[0, 0].set_title('AI Tools Search Interest Over Time')
    axes[0, 0].set_ylabel('Search Interest')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Current interest comparison
    current_interest = {tool: values[-1] for tool, values in trends_data.items()}
    axes[0, 1].bar(current_interest.keys(), current_interest.values(), 
                   color=['#FF6B6B', '#4ECDC4', '#95E1D3'])
    axes[0, 1].set_title('Current Search Interest (December)')
    axes[0, 1].set_ylabel('Interest Score')
    
    # 3. Growth rate comparison
    growth_rates = {tool: ((values[-1] - values[0]) / values[0] * 100) 
                    for tool, values in trends_data.items()}
    axes[1, 0].barh(growth_rates.keys(), growth_rates.values(), 
                    color=['#FF6B6B', '#4ECDC4', '#95E1D3'])
    axes[1, 0].set_title('Year-over-Year Growth Rate')
    axes[1, 0].set_xlabel('Growth Rate (%)')
    
    # 4. Trend volatility
    volatility = {tool: np.std(values) for tool, values in trends_data.items()}
    axes[1, 1].bar(volatility.keys(), volatility.values(), 
                   color=['#FF6B6B', '#4ECDC4', '#95E1D3'])
    axes[1, 1].set_title('Search Trend Volatility')
    axes[1, 1].set_ylabel('Standard Deviation')
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp16_google_trends.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp16_google_trends.png")
    
    return fig