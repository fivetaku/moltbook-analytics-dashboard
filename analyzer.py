#!/usr/bin/env python3
"""
Analyzer for Moltbook Analytics Dashboard
Role: Calculate metrics from collected data

Author: AI-PUMASI Project #1
"""

import json
import pandas as pd
from datetime import datetime
from pathlib import Path

def load_latest_data():
    """Load the most recent data files"""
    data_dir = Path('data')
    
    # Find latest files
    posts_files = sorted(data_dir.glob('posts_*.json'))
    comments_files = sorted(data_dir.glob('comments_*.json'))
    summary_files = sorted(data_dir.glob('summary_*.json'))
    
    if not posts_files or not comments_files:
        raise FileNotFoundError("No data files found. Run data_collector.py first!")
    
    with open(posts_files[-1]) as f:
        posts = json.load(f)
    
    with open(comments_files[-1]) as f:
        comments = json.load(f)
    
    with open(summary_files[-1]) as f:
        summary = json.load(f)
    
    return posts, comments, summary

def analyze_data():
    """Main analysis function"""
    print("📊 Starting analysis...")
    
    posts, comments, summary = load_latest_data()
    
    print(f"\n📈 Basic Stats:")
    print(f"   Total Posts: {len(posts)}")
    print(f"   Total Comments: {len(comments)}")
    print(f"   Subscribers: {summary.get('subscriber_count', 'N/A')}")
    
    # TODO: Add your analysis here!
    # Ideas:
    # - Engagement rate (comments per post)
    # - Most active posters
    # - Growth trends over time
    # - Peak activity times
    # - Top posts by engagement
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "basic_stats": {
            "total_posts": len(posts),
            "total_comments": len(comments),
            "subscribers": summary.get('subscriber_count', 0)
        }
        # Add more metrics here
    }
    
    # Save results
    output_file = f'analysis/metrics_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Analysis saved to: {output_file}")
    return results

if __name__ == "__main__":
    analyze_data()
