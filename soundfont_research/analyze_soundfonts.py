#!/usr/bin/env python3

import re

# Read the catalog
with open('soundfont_catalog_raw.txt', 'r') as f:
    lines = f.readlines()

# Parse and categorize
soundfonts = []
for line in lines:
    if '\t' in line:
        size_str, name = line.strip().split('\t', 1)
        size = int(size_str)
        soundfonts.append((size, name))

# Size categories (in MB)
def size_category(size_bytes):
    mb = size_bytes / (1024 * 1024)
    if mb < 5:
        return 'Small (<5MB)'
    elif mb < 20:
        return 'Medium (5-20MB)'
    elif mb < 100:
        return 'Large (20-100MB)'
    else:
        return 'XLarge (>100MB)'

# Pattern-based categories
def categorize_by_name(name):
    name_lower = name.lower()
    
    # Genre categories
    if any(x in name_lower for x in ['rock', 'metal', 'distort', 'guitar']):
        return 'Rock/Guitar'
    elif any(x in name_lower for x in ['drum', 'kit', 'percussion']):
        return 'Drums'
    elif any(x in name_lower for x in ['orchestra', 'symphony', 'classical', 'violin', 'piano']):
        return 'Classical/Orchestral'
    elif any(x in name_lower for x in ['synth', 'electronic', 'techno', 'dance']):
        return 'Electronic/Synth'
    elif any(x in name_lower for x in ['jazz', 'blues', 'funk']):
        return 'Jazz/Blues'
    elif any(x in name_lower for x in ['vintage', 'retro', '8bit', '16bit', 'chip']):
        return 'Retro/Chiptune'
    elif any(x in name_lower for x in ['bass', 'acoustic']):
        return 'Bass/Acoustic'
    elif any(x in name_lower for x in ['general', 'gm', 'gs', 'xg', 'complete', 'full']):
        return 'General Purpose'
    else:
        return 'Other'

# Quality indicators based on web research
def get_quality_score(name, size):
    name_lower = name.lower()
    mb = size / (1024 * 1024)
    
    score = 0
    
    # High-quality indicators from community
    if 'arachno' in name_lower:
        score += 10  # Community favorite
    elif 'timbres' in name_lower or 'heaven' in name_lower:
        score += 8   # Orchestral favorite
    elif 'merlin' in name_lower:
        score += 7   # Good for gaming
    elif 'airfont' in name_lower:
        score += 6   # High-end general
    
    # Size-based quality hints
    if 50 < mb < 200:
        score += 3   # Sweet spot for quality/performance
    elif mb > 200:
        score += 5   # Likely high quality
    elif mb < 2:
        score -= 2   # Likely low quality
    
    # Negative indicators
    if any(x in name_lower for x in ['test', 'demo', 'beta', 'wip']):
        score -= 3
    
    return score

# Analyze
categories = {}
size_dist = {}
recommended = []

for size, name in soundfonts:
    # Categorize by pattern
    cat = categorize_by_name(name)
    if cat not in categories:
        categories[cat] = []
    categories[cat].append((size, name))
    
    # Size distribution
    size_cat = size_category(size)
    if size_cat not in size_dist:
        size_dist[size_cat] = 0
    size_dist[size_cat] += 1
    
    # Quality scoring
    quality = get_quality_score(name, size)
    if quality >= 5:
        recommended.append((quality, size, name))

# Print analysis
print('=== SOUNDFONT COLLECTION SYSTEMATIC ANALYSIS ===')
print(f'Total soundfonts: {len(soundfonts)}')
print()

print('=== SIZE DISTRIBUTION ===')
for size_cat, count in sorted(size_dist.items()):
    print(f'{size_cat}: {count} soundfonts')
print()

print('=== CATEGORY BREAKDOWN ===')
for cat, items in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'{cat}: {len(items)} soundfonts')
    # Show top 3 by size in each category
    top_items = sorted(items, key=lambda x: x[0], reverse=True)[:3]
    for size, name in top_items:
        mb = size / (1024 * 1024)
        print(f'  - {name} ({mb:.1f}MB)')
    print()

print('=== TOP RECOMMENDATIONS (Community + Quality Score) ===')
recommended.sort(reverse=True)
for i, (quality, size, name) in enumerate(recommended[:15]):
    mb = size / (1024 * 1024)
    print(f'{i+1:2d}. {name} ({mb:.1f}MB) [Score: {quality}]')
print()

print('=== QUICK REFERENCE BY USE CASE ===')
print()

# Rock/Guitar optimized
rock_items = categories.get('Rock/Guitar', [])
if rock_items:
    rock_sorted = sorted(rock_items, key=lambda x: get_quality_score(x[1], x[0]), reverse=True)[:5]
    print('ROCK/GUITAR PRODUCTION:')
    for size, name in rock_sorted:
        mb = size / (1024 * 1024)
        print(f'  - {name} ({mb:.1f}MB)')
    print()

# Drum alternatives
drum_items = categories.get('Drums', [])
if drum_items:
    drum_sorted = sorted(drum_items, key=lambda x: x[0], reverse=True)[:5]
    print('DRUM KIT VARIETY:')
    for size, name in drum_sorted:
        mb = size / (1024 * 1024)
        print(f'  - {name} ({mb:.1f}MB)')
    print()

# High-quality general purpose
general_items = categories.get('General Purpose', [])
if general_items:
    general_sorted = sorted(general_items, key=lambda x: get_quality_score(x[1], x[0]), reverse=True)[:5]
    print('HIGH-QUALITY GENERAL:')
    for size, name in general_sorted:
        mb = size / (1024 * 1024)
        print(f'  - {name} ({mb:.1f}MB)')
    print()

# Performance optimized (small but good)
small_quality = [(s, n) for s, n in soundfonts if 2 < s/(1024*1024) < 15 and get_quality_score(n, s) > 3]
small_sorted = sorted(small_quality, key=lambda x: get_quality_score(x[1], x[0]), reverse=True)[:5]
if small_sorted:
    print('PERFORMANCE OPTIMIZED (<15MB):')
    for size, name in small_sorted:
        mb = size / (1024 * 1024)
        print(f'  - {name} ({mb:.1f}MB)') 