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
# EXPERIMENT 15: Amazon Product Reviews
# =====================================================================

def amazon_product_analysis():
    """
    Analyze Amazon product reviews
    """
    print("\n" + "="*80)
    print("EXPERIMENT 15: Amazon Product Review Analytics")
    print("="*80)
    
    products = {
        'AI Smart Speaker': {
            'total_reviews': 5234,
            'avg_rating': 4.3,
            'verified_purchases': 4892,
            '5_star': 2800,
            '4_star': 1500,
            '3_star': 650,
            '2_star': 180,
            '1_star': 104,
        },
        'Advanced Smartwatch': {
            'total_reviews': 3456,
            'avg_rating': 4.1,
            'verified_purchases': 3212,
            '5_star': 1800,
            '4_star': 1100,
            '3_star': 380,
            '2_star': 120,
            '1_star': 56,
        },
        'EV Charging Cable': {
            'total_reviews': 2145,
            'avg_rating': 4.5,
            'verified_purchases': 2010,
            '5_star': 1500,
            '4_star': 450,
            '3_star': 150,
            '2_star': 35,
            '1_star': 10,
        },
        'Laptop Stand': {
            'total_reviews': 4521,
            'avg_rating': 4.2,
            'verified_purchases': 4187,
            '5_star': 2400,
            '4_star': 1300,
            '3_star': 600,
            '2_star': 180,
            '1_star': 41,
        }
    }
    
    print("\nProduct Review Summary:")
    for product, data in products.items():
        verified_percent = (data['verified_purchases'] / data['total_reviews']) * 100
        print(f"\n  {product}:")
        print(f"    Total Reviews: {data['total_reviews']:,}")
        print(f"    Average Rating: {data['avg_rating']:.1f}/5")
        print(f"    Verified Purchases: {verified_percent:.1f}%")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Amazon Product Review Analytics', fontsize=16, fontweight='bold')
    
    product_names = list(products.keys())
    
    # 1. Average ratings
    avg_ratings = [products[p]['avg_rating'] for p in product_names]
    axes[0, 0].bar(product_names, avg_ratings, color=['#FF6B6B', '#4ECDC4', '#95E1D3', '#FFE66D'])
    axes[0, 0].set_title('Average Product Rating')
    axes[0, 0].set_ylabel('Rating (out of 5)')
    axes[0, 0].set_ylim([0, 5])
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Total reviews
    total_reviews = [products[p]['total_reviews'] for p in product_names]
    axes[0, 1].barh(product_names, total_reviews, color=['#FF6B6B', '#4ECDC4', '#95E1D3', '#FFE66D'])
    axes[0, 1].set_title('Total Number of Reviews')
    axes[0, 1].set_xlabel('Review Count')
    
    # 3. Rating distribution for first product
    first_product = product_names[0]
    rating_dist = {
        '5★': products[first_product]['5_star'],
        '4★': products[first_product]['4_star'],
        '3★': products[first_product]['3_star'],
        '2★': products[first_product]['2_star'],
        '1★': products[first_product]['1_star'],
    }
    axes[1, 0].barh(list(rating_dist.keys()), list(rating_dist.values()),
                    color=['#95E1D3', '#FFE66D', '#FF6B6B', '#FF6B6B', '#FF6B6B'])
    axes[1, 0].set_title(f'Rating Distribution: {first_product}')
    axes[1, 0].set_xlabel('Number of Reviews')
    
    # 4. Verified purchase percentage
    verified_percent = [(products[p]['verified_purchases'] / products[p]['total_reviews']) * 100 
                        for p in product_names]
    axes[1, 1].bar(product_names, verified_percent, color=['#FF6B6B', '#4ECDC4', '#95E1D3', '#FFE66D'])
    axes[1, 1].set_title('Verified Purchase Percentage')
    axes[1, 1].set_ylabel('Percentage (%)')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('/home/claude/exp15_amazon_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: exp15_amazon_analysis.png")
    
    return fig