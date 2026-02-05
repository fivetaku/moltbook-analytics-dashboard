#!/usr/bin/env python3
"""
Data Collector for Moltbook Analytics Dashboard
Role: Fetch posts and comments from m/ai-pumasi via Moltbook API

Author: AI-PUMASI Project #1
"""

import requests
import json
import time
from datetime import datetime

# API Configuration
API_KEY = "moltbook_sk_dWUQ18VPeHbOnC3hevOvJ2r-Aw9ZBAnh"
BASE_URL = "https://www.moltbook.com/api/v1"
SUBMOLT = "ai-pumasi"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def fetch_submolt_info():
    """Fetch submolt basic info and stats"""
    url = f"{BASE_URL}/submolts/{SUBMOLT}"
    response = requests.get(url, headers=headers)
    return response.json()

def fetch_posts(limit=100):
    """Fetch posts from the submolt"""
    url = f"{BASE_URL}/submolts/{SUBMOLT}/posts"
    params = {"limit": limit}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def fetch_post_comments(post_id):
    """Fetch comments for a specific post"""
    url = f"{BASE_URL}/posts/{post_id}/comments"
    response = requests.get(url, headers=headers)
    return response.json()

def collect_all_data():
    """Main function to collect all data"""
    print("🦞 Starting data collection...")
    
    # 1. Get submolt info
    print("\n📊 Fetching submolt info...")
    submolt_info = fetch_submolt_info()
    
    # 2. Get all posts
    print(f"\n📝 Fetching posts from m/{SUBMOLT}...")
    posts_data = fetch_posts()
    posts = posts_data.get('posts', [])
    print(f"   Found {len(posts)} posts")
    
    # 3. Get comments for each post
    print("\n💬 Fetching comments for all posts...")
    all_comments = []
    for i, post in enumerate(posts, 1):
        post_id = post['id']
        print(f"   [{i}/{len(posts)}] Post: {post_id}")
        comments_data = fetch_post_comments(post_id)
        comments = comments_data.get('comments', [])
        
        # Add post_id to each comment for reference
        for comment in comments:
            comment['post_id'] = post_id
        
        all_comments.extend(comments)
        time.sleep(0.5)  # Be nice to the API
    
    print(f"   Total comments collected: {len(all_comments)}")
    
    # 4. Save to files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("\n💾 Saving data...")
    
    # Save submolt info
    with open(f'data/submolt_info_{timestamp}.json', 'w') as f:
        json.dump(submolt_info, f, indent=2)
    print(f"   ✅ Saved: data/submolt_info_{timestamp}.json")
    
    # Save posts
    with open(f'data/posts_{timestamp}.json', 'w') as f:
        json.dump(posts, f, indent=2)
    print(f"   ✅ Saved: data/posts_{timestamp}.json")
    
    # Save comments
    with open(f'data/comments_{timestamp}.json', 'w') as f:
        json.dump(all_comments, f, indent=2)
    print(f"   ✅ Saved: data/comments_{timestamp}.json")
    
    # Create summary
    summary = {
        "timestamp": timestamp,
        "submolt": SUBMOLT,
        "subscriber_count": submolt_info.get('submolt', {}).get('subscriber_count', 0),
        "total_posts": len(posts),
        "total_comments": len(all_comments),
        "collection_date": datetime.now().isoformat()
    }
    
    with open(f'data/summary_{timestamp}.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"   ✅ Saved: data/summary_{timestamp}.json")
    
    print("\n✅ Data collection complete!")
    print(f"\n📈 Summary:")
    print(f"   Subscribers: {summary['subscriber_count']}")
    print(f"   Posts: {summary['total_posts']}")
    print(f"   Comments: {summary['total_comments']}")
    
    return summary

if __name__ == "__main__":
    collect_all_data()
