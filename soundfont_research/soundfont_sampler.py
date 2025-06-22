#!/usr/bin/env python3
"""
SoundFont Sampling Tool

This tool helps you quickly test different soundfonts with your existing songs
so you can make informed decisions about which soundfonts work best for different genres and use cases.

Usage:
    python soundfont_sampler.py --project i_love_lemon --category rock --top 5
    python soundfont_sampler.py --project example_song --recommend
    python soundfont_sampler.py --setup-collection
"""

import os
import sys
import argparse
import shutil
import subprocess
from pathlib import Path
import json
from typing import List, Dict, Tuple, Optional

# Import the existing analysis
sys.path.append('.')
from analyze_soundfonts import soundfonts, categorize_by_name, get_quality_score

class SoundFontSampler:
    def __init__(self, workspace_root: str = "/workspace"):
        self.workspace_root = Path(workspace_root)
        self.soundfont_research = self.workspace_root / "soundfont_research"
        self.soundfonts_collection = self.soundfont_research / "soundfonts_collection"
        self.catalog_file = self.soundfont_research / "soundfont_catalog_raw.txt"
        
        # Load soundfont data
        self.soundfonts_data = self._load_soundfonts()
        
    def _load_soundfonts(self) -> List[Tuple[int, str]]:
        """Load soundfont data from catalog"""
        try:
            with open(self.catalog_file, 'r') as f:
                lines = f.readlines()
            
            soundfonts = []
            for line in lines:
                if '\t' in line:
                    size_str, name = line.strip().split('\t', 1)
                    size = int(size_str)
                    soundfonts.append((size, name))
            return soundfonts
        except FileNotFoundError:
            print(f"❌ Could not find catalog file: {self.catalog_file}")
            return []

    def get_recommendations_by_category(self, category: str, top_n: int = 5) -> List[Dict]:
        """Get top soundfont recommendations for a specific category"""
        categorized = []
        
        for size, name in self.soundfonts_data:
            sf_category = categorize_by_name(name)
            if category.lower() in sf_category.lower() or sf_category.lower() in category.lower():
                quality_score = get_quality_score(name, size)
                mb_size = size / (1024 * 1024)
                
                categorized.append({
                    'name': name,
                    'size_bytes': size,
                    'size_mb': round(mb_size, 1),
                    'quality_score': quality_score,
                    'category': sf_category
                })
        
        # Sort by quality score then by size (bigger is often better for quality)
        categorized.sort(key=lambda x: (x['quality_score'], x['size_bytes']), reverse=True)
        
        return categorized[:top_n]

    def get_smart_recommendations(self, project_name: str) -> Dict[str, List[Dict]]:
        """Get smart recommendations based on project analysis"""
        project_path = self.workspace_root / project_name
        
        # Analyze project for genre/instrumentation hints
        genre_hints = self._analyze_project_genre(project_path)
        
        recommendations = {
            'rock_guitar': self.get_recommendations_by_category('rock', 3),
            'drums': self.get_recommendations_by_category('drums', 3),
            'general': self.get_recommendations_by_category('general', 3),
            'performance': self._get_performance_optimized(3)
        }
        
        # Add genre-specific recommendations
        if 'math_rock' in genre_hints or 'rock' in genre_hints:
            recommendations['recommended_primary'] = self.get_recommendations_by_category('rock', 1)
        else:
            recommendations['recommended_primary'] = self.get_recommendations_by_category('general', 1)
            
        return recommendations

    def _analyze_project_genre(self, project_path: Path) -> List[str]:
        """Analyze project files to determine likely genre/style"""
        hints = []
        
        # Check for LilyPond files
        ly_files = list(project_path.glob("*.ly"))
        for ly_file in ly_files:
            try:
                content = ly_file.read_text().lower()
                if any(word in content for word in ['rock', 'metal', 'distort']):
                    hints.append('rock')
                if any(word in content for word in ['jazz', 'swing', 'blues']):
                    hints.append('jazz')
                if any(word in content for word in ['math', 'complex', 'syncopat']):
                    hints.append('math_rock')
                if 'drummode' in content:
                    hints.append('needs_drums')
            except:
                pass
                
        # Check song prompts
        prompt_files = list(project_path.glob("*prompt*.md"))
        for prompt_file in prompt_files:
            try:
                content = prompt_file.read_text().lower()
                if any(word in content for word in ['rock', 'math rock', 'metal']):
                    hints.append('rock')
                if any(word in content for word in ['jazz', 'blues', 'swing']):
                    hints.append('jazz')
            except:
                pass
                
        return hints

    def _get_performance_optimized(self, top_n: int) -> List[Dict]:
        """Get performance-optimized soundfonts (<15MB but good quality)"""
        performance_fonts = []
        
        for size, name in self.soundfonts_data:
            mb_size = size / (1024 * 1024)
            if 2 < mb_size < 15:  # Sweet spot for performance
                quality_score = get_quality_score(name, size)
                if quality_score >= 3:  # Minimum quality threshold
                    performance_fonts.append({
                        'name': name,
                        'size_bytes': size,
                        'size_mb': round(mb_size, 1),
                        'quality_score': quality_score,
                        'category': 'Performance Optimized'
                    })
        
        performance_fonts.sort(key=lambda x: x['quality_score'], reverse=True)
        return performance_fonts[:top_n]

    def setup_collection_structure(self):
        """Set up the soundfont collection directory structure for easy organization"""
        print("🔧 Setting up soundfont collection structure...")
        
        categories = {
            'general': "High-quality general-purpose GM soundfonts",
            'rock': "Rock, guitar, and metal-optimized soundfonts", 
            'drums': "Drum-specific soundfonts and kits",
            'orchestral': "Classical and orchestral soundfonts",
            'performance': "Small but high-quality soundfonts for fast iteration",
            'top_quality': "Premium large soundfonts (>100MB)"
        }
        
        for category, description in categories.items():
            category_dir = self.soundfonts_collection / category
            category_dir.mkdir(parents=True, exist_ok=True)
            
            readme_file = category_dir / "README.md"
            readme_file.write_text(f"# {category.title()} SoundFonts\n\n{description}\n\n")
            
        print(f"✅ Created collection structure at: {self.soundfonts_collection}")
        
        # Create extraction guide
        guide_file = self.soundfonts_collection / "EXTRACTION_GUIDE.md"
        guide_content = """# SoundFont Collection Setup

## Quick Setup (if you have the ZIP archive)

1. **Extract the archive:**
   ```bash
   # If you have 500_Soundfonts_Full_GM_Sets.zip
   unzip -q 500_Soundfonts_Full_GM_Sets.zip -d temp_extraction/
   ```

2. **Organize by category:**
   ```bash
   # Move soundfonts to appropriate categories
   python soundfont_sampler.py --organize-collection temp_extraction/
   ```

3. **Test with existing project:**
   ```bash
   python soundfont_sampler.py --project i_love_lemon --recommend
   ```

## Manual Organization

If organizing manually, use these guidelines:

- **general/**: Arachno*, Merlin*, Timbres*, MuseScore_General*, *GM*.sf2
- **rock/**: *Rock*, *Guitar*, *Metal*, *Distort*
- **drums/**: *Drum*, *Kit*, *Percussion*
- **orchestral/**: *Orchestra*, *Symphony*, *Classical*, *Piano*
- **performance/**: Files under 15MB with quality score > 3
- **top_quality/**: Files over 100MB with quality score > 7

## Testing Workflow

1. Copy soundfont to project: `cp soundfonts_collection/category/font.sf2 project/sf2/`
2. Update Makefile: `SOUNDFONT = sf2/font.sf2`
3. Test render: `make demo`
4. Document results in project's README or Insights section
"""
        guide_file.write_text(guide_content)
        
        print(f"📖 Created extraction guide at: {guide_file}")

    def create_project_tester(self, project_name: str, soundfont_category: str = None, top_n: int = 3):
        """Create a testing script for a specific project"""
        project_path = self.workspace_root / project_name
        
        if not project_path.exists():
            print(f"❌ Project '{project_name}' not found at {project_path}")
            return
            
        # Ensure sf2 directory exists
        sf2_dir = project_path / "sf2"
        sf2_dir.mkdir(exist_ok=True)
        
        # Get recommendations
        if soundfont_category:
            recommendations = self.get_recommendations_by_category(soundfont_category, top_n)
            category_name = soundfont_category
        else:
            smart_recs = self.get_smart_recommendations(project_name)
            recommendations = smart_recs.get('recommended_primary', [])
            if not recommendations:
                recommendations = smart_recs.get('general', [])
            category_name = "smart recommendations"
        
        # Create test script
        test_script = project_path / "test_soundfonts.sh"
        script_content = f"""#!/bin/bash
# SoundFont Testing Script for {project_name}
# Generated by soundfont_sampler.py

PROJECT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"
SOUNDFONT_COLLECTION="{self.soundfonts_collection}"
BACKUP_MAKEFILE="$PROJECT_DIR/Makefile.backup"

echo "🎵 Testing soundfonts for {project_name} ({category_name})"
echo "Project: $PROJECT_DIR"
echo

# Backup original Makefile
if [ ! -f "$BACKUP_MAKEFILE" ]; then
    cp "$PROJECT_DIR/Makefile" "$BACKUP_MAKEFILE"
    echo "✅ Backed up original Makefile"
fi

# Test each recommended soundfont
"""

        for i, rec in enumerate(recommendations[:top_n], 1):
            soundfont_name = rec['name']
            size_mb = rec['size_mb']
            quality_score = rec['quality_score']
            
            script_content += f"""
echo "--- Testing {i}/{len(recommendations[:top_n])}: {soundfont_name} ({size_mb}MB, Score: {quality_score}) ---"

# Check if soundfont exists
SOUNDFONT_PATH="$SOUNDFONT_COLLECTION/*/{soundfont_name}"
if ls $SOUNDFONT_PATH 1> /dev/null 2>&1; then
    # Copy soundfont to project
    cp $SOUNDFONT_PATH "$PROJECT_DIR/sf2/"
    
    # Update Makefile
    sed -i.tmp 's|SOUNDFONT = .*|SOUNDFONT = sf2/{soundfont_name}|' "$PROJECT_DIR/Makefile"
    
    # Test render
    echo "🔄 Rendering with {soundfont_name}..."
    cd "$PROJECT_DIR"
    make demo
    
    if [ $? -eq 0 ]; then
        echo "✅ Render successful with {soundfont_name}"
        echo "🎧 Listen to the result and rate the quality"
        echo
        read -p "Rate this soundfont (1-10, or 's' to skip): " rating
        echo "Rating for {soundfont_name}: $rating" >> soundfont_test_results.txt
    else
        echo "❌ Render failed with {soundfont_name}"
        echo "FAILED: {soundfont_name}" >> soundfont_test_results.txt
    fi
    
    echo
else
    echo "⚠️  Soundfont not found: {soundfont_name}"
    echo "   Expected at: $SOUNDFONT_PATH"
    echo "   Make sure soundfonts are extracted and organized"
fi
"""

        script_content += """
# Restore original Makefile
cp "$BACKUP_MAKEFILE" "$PROJECT_DIR/Makefile"
echo "🔄 Restored original Makefile"

echo
echo "✅ Testing complete!"
echo "📊 Results saved to: soundfont_test_results.txt"
echo "🎯 Best options based on your ratings:"
sort -k2 -nr soundfont_test_results.txt | head -3
"""

        test_script.write_text(script_content)
        test_script.chmod(0o755)
        
        print(f"✅ Created test script: {test_script}")
        print(f"🎯 Testing {len(recommendations)} {category_name} soundfonts")
        print("\nTo run the test:")
        print(f"   cd {project_name}")
        print("   ./test_soundfonts.sh")

    def create_quick_sampler(self):
        """Create a quick sampler that generates short demos with different soundfonts"""
        sampler_script = self.soundfont_research / "quick_sampler.py"
        
        sampler_content = '''#!/usr/bin/env python3
"""
Quick SoundFont Sampler

Generates short demo MIDIs with different soundfonts so you can quickly
hear the differences without full song renders.
"""

import os
import subprocess
from pathlib import Path

def create_demo_midi():
    """Create a short demo MIDI for testing"""
    demo_ly = """
\\version "2.24.0"

% Quick demo for soundfont testing
\\score {
  <<
    % Guitar part
    \\new Staff \\with {
      midiInstrument = "electric guitar (clean)"
    } {
      \\time 4/4
      \\key g \\major
      g8 b d' g' d' b g4 |
      e8 g b e' b g e4 |
      g8 b d' g' d' b g4 |
      c'8 e' g' c'' g' e' c'4 |
    }
    
    % Bass part  
    \\new Staff \\with {
      midiInstrument = "electric bass (finger)"
      \\clef bass
    } {
      g,4 g,8 g, g,4 g,8 g, |
      e,4 e,8 e, e,4 e,8 e, |
      g,4 g,8 g, g,4 g,8 g, |
      c4 c8 c c4 c8 c |
    }
    
    % Drums
    \\new DrumStaff {
      \\drummode {
        bd4 sn8 bd sn4 bd8 sn |
        bd4 sn8 bd sn4 bd8 sn |
        bd4 sn8 bd sn4 bd8 sn |
        bd4 sn8 bd sn4 bd8 sn |
      }
    }
  >>
  
  \\layout { }
  \\midi {
    \\tempo 4=120
  }
}
"""
    
    demo_file = Path("demo_test.ly")
    demo_file.write_text(demo_ly)
    return demo_file

def test_soundfont(sf2_path, output_name):
    """Test a single soundfont with the demo"""
    demo_file = create_demo_midi()
    
    print(f"🎵 Testing: {sf2_path.name}")
    
    # Render MIDI
    subprocess.run(["lilypond", "--silent", str(demo_file)])
    
    # Convert to audio with soundfont
    midi_file = demo_file.with_suffix('.midi')
    wav_file = Path(f"demo_{output_name}.wav")
    
    cmd = [
        "fluidsynth", "-ni", str(sf2_path), 
        str(midi_file), "-F", str(wav_file)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Created: {wav_file}")
        return wav_file
    else:
        print(f"❌ Failed to render {sf2_path.name}")
        print(result.stderr)
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python quick_sampler.py <soundfont1.sf2> [soundfont2.sf2] ...")
        sys.exit(1)
    
    print("🎤 Quick SoundFont Sampler")
    print("=" * 40)
    
    for sf2_file in sys.argv[1:]:
        sf2_path = Path(sf2_file)
        if sf2_path.exists():
            output_name = sf2_path.stem.lower().replace(' ', '_')
            test_soundfont(sf2_path, output_name)
        else:
            print(f"❌ Not found: {sf2_file}")
    
    print("\\n🎧 Listen to the demo_*.wav files to compare soundfonts")
'''
        
        sampler_script.write_text(sampler_content)
        sampler_script.chmod(0o755)
        
        print(f"✅ Created quick sampler: {sampler_script}")

def main():
    parser = argparse.ArgumentParser(description="SoundFont Sampling Tool")
    parser.add_argument('--project', help='Project name to test with')
    parser.add_argument('--category', help='SoundFont category (rock, drums, general, etc.)')
    parser.add_argument('--top', type=int, default=3, help='Number of top recommendations')
    parser.add_argument('--recommend', action='store_true', help='Get smart recommendations')
    parser.add_argument('--setup-collection', action='store_true', help='Set up collection structure')
    parser.add_argument('--quick-sampler', action='store_true', help='Create quick sampling tool')
    
    args = parser.parse_args()
    
    sampler = SoundFontSampler()
    
    if args.setup_collection:
        sampler.setup_collection_structure()
        
    if args.quick_sampler:
        sampler.create_quick_sampler()
        
    if args.project:
        if args.recommend:
            recommendations = sampler.get_smart_recommendations(args.project)
            print(f"🎯 Smart recommendations for '{args.project}':")
            print("=" * 50)
            
            for category, recs in recommendations.items():
                if recs:
                    print(f"\n{category.upper().replace('_', ' ')}:")
                    for rec in recs:
                        print(f"  • {rec['name']} ({rec['size_mb']}MB, Score: {rec['quality_score']})")
        else:
            category = args.category or 'general'
            sampler.create_project_tester(args.project, category, args.top)
    
    elif args.category:
        recommendations = sampler.get_recommendations_by_category(args.category, args.top)
        print(f"🎵 Top {args.top} {args.category} soundfonts:")
        print("=" * 40)
        
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['name']}")
            print(f"   Size: {rec['size_mb']}MB | Score: {rec['quality_score']} | Category: {rec['category']}")
            print()

if __name__ == "__main__":
    main()