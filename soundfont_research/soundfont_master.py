#!/usr/bin/env python3
"""
SoundFont Master Control Script

This is your one-stop interface for soundfont research and testing.
It combines all the tools into simple commands so you can easily sample 
different soundfonts and make informed decisions.

Usage Examples:
    python soundfont_master.py setup                    # Initial setup
    python soundfont_master.py recommend rock           # Get rock recommendations  
    python soundfont_master.py test i_love_lemon        # Test soundfonts with project
    python soundfont_master.py quick-demo rock 3        # Quick demo of top 3 rock fonts
    python soundfont_master.py multi-setup i_love_lemon # Set up multi-soundfont rendering
"""

import argparse
import subprocess
import sys
from pathlib import Path

class SoundFontMaster:
    def __init__(self):
        self.workspace_root = Path("/workspace")
        self.research_dir = self.workspace_root / "soundfont_research"
        
    def setup_everything(self):
        """Set up the complete soundfont research environment"""
        print("🚀 Setting up SoundFont Research Environment")
        print("=" * 50)
        
        # Run the analysis
        print("1. Running soundfont analysis...")
        subprocess.run([sys.executable, "analyze_soundfonts.py"], cwd=self.research_dir)
        
        # Set up collection structure
        print("\n2. Setting up collection structure...")
        subprocess.run([sys.executable, "soundfont_sampler.py", "--setup-collection"], cwd=self.research_dir)
        
        # Create quick sampler
        print("\n3. Creating quick sampling tools...")
        subprocess.run([sys.executable, "soundfont_sampler.py", "--quick-sampler"], cwd=self.research_dir)
        
        print("\n✅ Setup complete!")
        print("\n📖 Next steps:")
        print("   1. Extract your soundfont collection (see EXTRACTION_GUIDE.md)")
        print("   2. Test recommendations: python soundfont_master.py recommend rock")
        print("   3. Test with project: python soundfont_master.py test i_love_lemon")
        
    def get_recommendations(self, category: str = "general", top_n: int = 5):
        """Get soundfont recommendations for a category"""
        print(f"🎵 Top {top_n} {category} soundfonts:")
        print("=" * 40)
        
        subprocess.run([
            sys.executable, "soundfont_sampler.py", 
            "--category", category, "--top", str(top_n)
        ], cwd=self.research_dir)
        
    def test_project(self, project_name: str, category: str = None):
        """Set up testing for a specific project"""
        print(f"🎯 Setting up soundfont testing for '{project_name}'")
        
        cmd = [sys.executable, "soundfont_sampler.py", "--project", project_name]
        if category is not None:
            cmd.extend(["--category", category])
        else:
            cmd.append("--recommend")
            
        subprocess.run(cmd, cwd=self.research_dir)
        
    def quick_demo(self, category: str, count: int = 3):
        """Create quick demo renders for comparison"""
        print(f"🎤 Creating quick demos for top {count} {category} soundfonts")
        
        # Get recommendations first
        self.get_recommendations(category, count)
        
        print(f"\n🔄 To create actual demo files, you'll need:")
        print(f"   1. Extract soundfonts to soundfonts_collection/{category}/")
        print(f"   2. Run: python quick_sampler.py <soundfont1.sf2> <soundfont2.sf2> ...")
        
    def setup_multi_soundfont(self, project_name: str):
        """Set up multi-soundfont rendering for a project"""
        print(f"🎼 Setting up multi-soundfont rendering for '{project_name}'")
        
        subprocess.run([
            sys.executable, "multi_soundfont_renderer.py",
            "--project", project_name, "--setup"
        ], cwd=self.research_dir)
        
    def show_status(self):
        """Show the current status of soundfont research"""
        print("📊 SoundFont Research Status")
        print("=" * 30)
        
        # Check if collection exists
        collection_dir = self.research_dir / "soundfonts_collection"
        if collection_dir.exists():
            print("✅ Collection structure set up")
            
            # Count soundfonts in each category
            for category_dir in collection_dir.iterdir():
                if category_dir.is_dir() and category_dir.name != "__pycache__":
                    sf2_count = len(list(category_dir.glob("*.sf2")))
                    print(f"   {category_dir.name}: {sf2_count} soundfonts")
        else:
            print("❌ Collection structure not set up")
            print("   Run: python soundfont_master.py setup")
            
        # Check available tools
        print("\n🛠️  Available Tools:")
        tools = [
            ("soundfont_sampler.py", "Project testing and recommendations"),
            ("multi_soundfont_renderer.py", "Multi-soundfont rendering pipeline"),
            ("quick_sampler.py", "Quick demo generation"),
            ("analyze_soundfonts.py", "Soundfont analysis and categorization")
        ]
        
        for tool, description in tools:
            tool_path = self.research_dir / tool
            status = "✅" if tool_path.exists() else "❌"
            print(f"   {status} {tool} - {description}")
            
        # Check projects ready for testing
        print("\n🎯 Projects Ready for Testing:")
        for project_dir in self.workspace_root.iterdir():
            if project_dir.is_dir() and project_dir.name not in ["soundfont_research", ".git", "__pycache__"]:
                has_ly = len(list(project_dir.glob("*.ly"))) > 0
                has_makefile = (project_dir / "Makefile").exists()
                
                if has_ly and has_makefile:
                    print(f"   ✅ {project_dir.name}")
                else:
                    print(f"   ⚠️  {project_dir.name} (missing LilyPond or Makefile)")

def main():
    parser = argparse.ArgumentParser(
        description="SoundFont Master Control Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python soundfont_master.py setup                    # Initial setup
  python soundfont_master.py recommend rock           # Get rock recommendations  
  python soundfont_master.py test i_love_lemon        # Test with project
  python soundfont_master.py test i_love_lemon rock   # Test rock soundfonts
  python soundfont_master.py quick-demo rock 3        # Quick demo of top 3 rock
  python soundfont_master.py multi-setup i_love_lemon # Multi-soundfont setup
  python soundfont_master.py status                   # Show current status
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Setup command
    subparsers.add_parser('setup', help='Set up the complete soundfont research environment')
    
    # Recommend command
    rec_parser = subparsers.add_parser('recommend', help='Get soundfont recommendations')
    rec_parser.add_argument('category', nargs='?', default='general', 
                           help='Category (rock, drums, general, etc.)')
    rec_parser.add_argument('--top', type=int, default=5, help='Number of recommendations')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Set up project testing')
    test_parser.add_argument('project', help='Project name to test')
    test_parser.add_argument('category', nargs='?', help='Soundfont category to focus on')
    
    # Quick demo command
    demo_parser = subparsers.add_parser('quick-demo', help='Create quick demos for comparison')
    demo_parser.add_argument('category', help='Soundfont category')
    demo_parser.add_argument('count', type=int, nargs='?', default=3, help='Number of demos')
    
    # Multi-soundfont setup
    multi_parser = subparsers.add_parser('multi-setup', help='Set up multi-soundfont rendering')
    multi_parser.add_argument('project', help='Project name')
    
    # Status command
    subparsers.add_parser('status', help='Show current status')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
        
    master = SoundFontMaster()
    
    if args.command == 'setup':
        master.setup_everything()
    elif args.command == 'recommend':
        master.get_recommendations(args.category, args.top)
    elif args.command == 'test':
        master.test_project(args.project, args.category)
    elif args.command == 'quick-demo':
        master.quick_demo(args.category, args.count)
    elif args.command == 'multi-setup':
        master.setup_multi_soundfont(args.project)
    elif args.command == 'status':
        master.show_status()

if __name__ == "__main__":
    main()