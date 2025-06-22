#!/usr/bin/env python3
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
\version "2.24.0"

% Quick demo for soundfont testing
\score {
  <<
    % Guitar part
    \new Staff \with {
      midiInstrument = "electric guitar (clean)"
    } {
      \time 4/4
      \key g \major
      g8 b d' g' d' b g4 |
      e8 g b e' b g e4 |
      g8 b d' g' d' b g4 |
      c'8 e' g' c'' g' e' c'4 |
    }
    
    % Bass part  
    \new Staff \with {
      midiInstrument = "electric bass (finger)"
      \clef bass
    } {
      g,4 g,8 g, g,4 g,8 g, |
      e,4 e,8 e, e,4 e,8 e, |
      g,4 g,8 g, g,4 g,8 g, |
      c4 c8 c c4 c8 c |
    }
    
    % Drums
    \new DrumStaff {
      \drummode {
        bd4 sn8 bd sn4 bd8 sn |
        bd4 sn8 bd sn4 bd8 sn |
        bd4 sn8 bd sn4 bd8 sn |
        bd4 sn8 bd sn4 bd8 sn |
      }
    }
  >>
  
  \layout { }
  \midi {
    \tempo 4=120
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
    
    print("\n🎧 Listen to the demo_*.wav files to compare soundfonts")
