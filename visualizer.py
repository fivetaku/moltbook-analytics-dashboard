#!/usr/bin/env python3
"""
Visualizer for Moltbook Analytics Dashboard
Role: Create charts and visual reports from analysis

Author: AI-PUMASI Project #1
"""

import json
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

def load_latest_analysis():
    """Load the most recent analysis results"""
    analysis_dir = Path('analysis')
    metrics_files = sorted(analysis_dir.glob('metrics_*.json'))
    
    if not metrics_files:
        raise FileNotFoundError("No analysis files found. Run analyzer.py first!")
    
    with open(metrics_files[-1]) as f:
        metrics = json.load(f)
    
    return metrics

def create_visualizations():
    """Main visualization function"""
    print("📊 Creating visualizations...")
    
    metrics = load_latest_analysis()
    
    # TODO: Add your visualizations here!
    # Ideas:
    # - Bar chart of posts vs comments
    # - Timeline of activity
    # - Top contributors chart
    # - Engagement heatmap
    
    # Example: Simple bar chart
    stats = metrics.get('basic_stats', {})
    
    fig, ax = plt.subplots(figsize=(10, 6))
    categories = ['Posts', 'Comments', 'Subscribers']
    values = [
        stats.get('total_posts', 0),
        stats.get('total_comments', 0),
        stats.get('subscribers', 0)
    ]
    
    ax.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax.set_title('m/ai-pumasi Overview', fontsize=16, fontweight='bold')
    ax.set_ylabel('Count', fontsize=12)
    
    # Save chart
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'dashboard/overview_{timestamp}.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"   ✅ Saved: {output_file}")
    
    print("\n✅ Visualizations complete!")

if __name__ == "__main__":
    create_visualizations()
