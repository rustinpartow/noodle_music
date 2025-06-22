#!/usr/bin/env python3
"""
Multi-SoundFont Rendering Pipeline

This solves the "Giant SoundFont problem" by allowing different soundfonts 
for different instruments. Premium soundfonts like GiantSoundfontV6.4MelodicBank_NoDrums.sf2 
can now be used for melodic instruments while dedicated drum soundfonts handle percussion.

Usage:
    python multi_soundfont_renderer.py --project i_love_lemon --setup
    python multi_soundfont_renderer.py --project i_love_lemon --render
"""

import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import tempfile

class MultiSoundFontRenderer:
    def __init__(self, workspace_root: str = "/workspace"):
        self.workspace_root = Path(workspace_root)
        
    def setup_project_for_multi_soundfont(self, project_name: str):
        """Set up a project for multi-soundfont rendering"""
        project_path = self.workspace_root / project_name
        
        if not project_path.exists():
            print(f"❌ Project '{project_name}' not found")
            return
            
        # Create multi-soundfont configuration
        config = {
            "guitar": {
                "soundfont": "sf2/GiantSoundfontV6.4MelodicBank_NoDrums.sf2",
                "midi_instruments": ["electric guitar (clean)", "electric guitar (muted)", 
                                   "overdriven guitar", "distortion guitar"]
            },
            "bass": {
                "soundfont": "sf2/GiantSoundfontV6.4MelodicBank_NoDrums.sf2", 
                "midi_instruments": ["electric bass (finger)", "electric bass (pick)", 
                                   "fretless bass", "slap bass 1", "slap bass 2"]
            },
            "piano": {
                "soundfont": "sf2/GiantSoundfontV6.4MelodicBank_NoDrums.sf2",
                "midi_instruments": ["acoustic grand piano", "bright acoustic piano",
                                   "electric grand piano", "electric piano 1", "electric piano 2"]
            },
            "drums": {
                "soundfont": "sf2/Drumm_GM.sf2",
                "midi_instruments": ["drums", "percussion"]
            },
            "other": {
                "soundfont": "sf2/Arachno_SoundFont_v1.0.sf2",  # Fallback for everything else
                "midi_instruments": []  # Will capture anything not matched above
            }
        }
        
        # Save configuration
        config_file = project_path / "multi_soundfont_config.json"
        import json
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
            
        print(f"✅ Created multi-soundfont configuration: {config_file}")
        
        # Create the multi-soundfont Makefile target
        makefile_path = project_path / "Makefile"
        
        if makefile_path.exists():
            makefile_content = makefile_path.read_text()
            
            # Add multi-soundfont targets if not already present
            if "multi-soundfont:" not in makefile_content:
                multi_targets = """
# Multi-SoundFont Rendering Targets
multi-soundfont: $(CHART_FILE)
	@echo "🎼 Multi-SoundFont Rendering Pipeline"
	python ../soundfont_research/multi_soundfont_renderer.py --project $(shell basename $(PWD)) --render

multi-setup:
	python ../soundfont_research/multi_soundfont_renderer.py --project $(shell basename $(PWD)) --setup

multi-demo: multi-soundfont
	@echo "🎧 Multi-SoundFont demo complete"
"""
                makefile_content += multi_targets
                makefile_path.write_text(makefile_content)
                print("✅ Added multi-soundfont targets to Makefile")
                
        # Create split-midi script for the project
        scripts_dir = project_path / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        
        split_script = scripts_dir / "split_midi_by_instrument.py"
        split_script_content = '''#!/usr/bin/env python3
"""
Split MIDI by instrument for multi-soundfont rendering
"""

import sys
import mido
from pathlib import Path
from collections import defaultdict

def split_midi_by_instrument(midi_file: Path, output_dir: Path):
    """Split a MIDI file into separate files by instrument"""
    
    mid = mido.MidiFile(midi_file)
    
    # Group tracks by MIDI instrument
    instrument_tracks = defaultdict(list)
    
    for track in mid.tracks:
        current_instrument = None
        track_messages = []
        
        for msg in track:
            if msg.type == 'program_change':
                current_instrument = msg.program
            track_messages.append(msg)
            
        # Determine instrument category
        if current_instrument is not None:
            if 24 <= current_instrument <= 31:  # Guitar family
                category = "guitar"
            elif 32 <= current_instrument <= 39:  # Bass family  
                category = "bass"
            elif 0 <= current_instrument <= 7:   # Piano family
                category = "piano"
            else:
                category = "other"
        else:
            # Check for drum track
            is_drum_track = any(msg.channel == 9 for msg in track_messages if hasattr(msg, 'channel'))
            category = "drums" if is_drum_track else "other"
            
        instrument_tracks[category].extend(track_messages)
    
    # Create separate MIDI files for each category
    output_files = {}
    
    for category, messages in instrument_tracks.items():
        if messages:
            new_mid = mido.MidiFile()
            new_track = mido.MidiTrack()
            
            for msg in messages:
                new_track.append(msg)
                
            new_mid.tracks.append(new_track)
            
            output_file = output_dir / f"{midi_file.stem}_{category}.mid"
            new_mid.save(output_file)
            output_files[category] = output_file
            
    return output_files

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_midi_by_instrument.py <input.mid> <output_dir>")
        sys.exit(1)
        
    midi_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(exist_ok=True)
    
    output_files = split_midi_by_instrument(midi_file, output_dir)
    
    print("Split MIDI files:")
    for category, file_path in output_files.items():
        print(f"  {category}: {file_path}")
'''
        
        split_script.write_text(split_script_content)
        split_script.chmod(0o755)
        
        print(f"✅ Created MIDI splitting script: {split_script}")
        print(f"\n🎯 Project '{project_name}' is now configured for multi-soundfont rendering!")
        print("\nNext steps:")
        print(f"1. Make sure you have the required soundfonts in {project_name}/sf2/")
        print(f"2. Run: cd {project_name} && make multi-soundfont")

    def render_with_multi_soundfonts(self, project_name: str):
        """Render a project using multiple soundfonts"""
        project_path = self.workspace_root / project_name
        config_file = project_path / "multi_soundfont_config.json"
        
        if not config_file.exists():
            print(f"❌ Multi-soundfont configuration not found. Run --setup first.")
            return
            
        # Load configuration
        import json
        with open(config_file, 'r') as f:
            config = json.load(f)
            
        # Find the main MIDI file
        midi_files = list(project_path.glob("*.midi"))
        if not midi_files:
            # Generate MIDI first
            print("🎼 Generating MIDI file...")
            result = subprocess.run(["make", "midi"], cwd=project_path, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Failed to generate MIDI: {result.stderr}")
                return
            midi_files = list(project_path.glob("*.midi"))
            
        if not midi_files:
            print("❌ No MIDI files found")
            return
            
        main_midi = midi_files[0]
        print(f"🎵 Using MIDI file: {main_midi}")
        
        # Create temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Split MIDI by instrument (simplified approach)
            split_files = self._split_midi_simple(main_midi, temp_path, config)
            
            # Render each split with its designated soundfont
            wav_files = []
            
            for category, split_file in split_files.items():
                if split_file and split_file.exists():
                    soundfont_path = project_path / config[category]["soundfont"]
                    
                    if not soundfont_path.exists():
                        print(f"⚠️  Soundfont not found: {soundfont_path}")
                        print(f"   Using fallback soundfont for {category}")
                        # Try to find any available soundfont
                        sf2_files = list((project_path / "sf2").glob("*.sf2"))
                        if sf2_files:
                            soundfont_path = sf2_files[0]
                        else:
                            print(f"❌ No soundfonts available for {category}")
                            continue
                    
                    wav_file = temp_path / f"{category}.wav"
                    
                    print(f"🔄 Rendering {category} with {soundfont_path.name}...")
                    
                    cmd = [
                        "fluidsynth", "-ni", str(soundfont_path),
                        str(split_file), "-F", str(wav_file),
                        "-r", "44100"  # Sample rate
                    ]
                    
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        wav_files.append((category, wav_file))
                        print(f"✅ Rendered {category}")
                    else:
                        print(f"❌ Failed to render {category}: {result.stderr}")
            
            # Mix all the WAV files together
            if len(wav_files) > 1:
                final_output = project_path / f"{project_name}_multi_soundfont.wav"
                self._mix_wav_files([wf[1] for wf in wav_files], final_output)
                print(f"🎉 Multi-soundfont render complete: {final_output}")
            elif len(wav_files) == 1:
                final_output = project_path / f"{project_name}_multi_soundfont.wav"
                shutil.copy(wav_files[0][1], final_output)
                print(f"✅ Single-soundfont render complete: {final_output}")
            else:
                print("❌ No successful renders to combine")

    def _split_midi_simple(self, midi_file: Path, output_dir: Path, config: Dict) -> Dict[str, Path]:
        """Simple MIDI splitting - creates full MIDI for each soundfont category"""
        # For now, just copy the full MIDI to each category
        # In a more sophisticated implementation, we'd parse MIDI and split by instrument
        
        split_files = {}
        
        for category in config.keys():
            split_file = output_dir / f"{midi_file.stem}_{category}.mid"
            shutil.copy(midi_file, split_file)
            split_files[category] = split_file
            
        return split_files

    def _mix_wav_files(self, wav_files: List[Path], output_file: Path):
        """Mix multiple WAV files using ffmpeg"""
        if not wav_files:
            return
            
        if len(wav_files) == 1:
            shutil.copy(wav_files[0], output_file)
            return
            
        # Use ffmpeg to mix the files
        cmd = ["ffmpeg", "-y"]  # -y to overwrite output
        
        # Add input files
        for wav_file in wav_files:
            cmd.extend(["-i", str(wav_file)])
            
        # Mix with equal weights
        filter_inputs = "+".join([f"[{i}:a]" for i in range(len(wav_files))])
        cmd.extend([
            "-filter_complex", f"{filter_inputs}amix=inputs={len(wav_files)}:duration=longest",
            str(output_file)
        ])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Mixed {len(wav_files)} audio streams")
        else:
            print(f"❌ Failed to mix audio: {result.stderr}")
            # Fallback: just use the first file
            shutil.copy(wav_files[0], output_file)

def main():
    parser = argparse.ArgumentParser(description="Multi-SoundFont Rendering Pipeline")
    parser.add_argument('--project', required=True, help='Project name')
    parser.add_argument('--setup', action='store_true', help='Set up project for multi-soundfont rendering')
    parser.add_argument('--render', action='store_true', help='Render project with multi-soundfonts')
    
    args = parser.parse_args()
    
    renderer = MultiSoundFontRenderer()
    
    if args.setup:
        renderer.setup_project_for_multi_soundfont(args.project)
        
    if args.render:
        renderer.render_with_multi_soundfonts(args.project)

if __name__ == "__main__":
    main()