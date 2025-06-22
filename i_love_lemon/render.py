#!/usr/bin/env python3
"""Tier D quick render for **i_love_lemon**.

Creates simple MIDI stems (if absent) and then calls FluidSynth
to bounce a demo WAV and MP3 using a stock SoundFont.

Requires:
    pip install midiutil pydub
    brew install fluidsynth   # macOS
    sudo apt-get install fluidsynth   # Ubuntu

Usage:
    python render.py
"""

import os, subprocess, sys
from midiutil import MIDIFile
import shutil

HERE = os.path.dirname(__file__)
MIDI_DIR = os.path.join(HERE, "midi")
os.makedirs(MIDI_DIR, exist_ok=True)

def simple_midi(path, pitches):
    mf = MIDIFile(1)
    track = 0
    time = 0
    mf.addTrackName(track, time, "track")
    mf.addTempo(track, time, 140)
    for i, p in enumerate(pitches):
        mf.addNote(track, 0, p, i, 1, 100)
    with open(path, 'wb') as f:
        mf.writeFile(f)

# Stub stems -------------------------------------------------
if not os.path.exists(os.path.join(MIDI_DIR, 'guitar.mid')):
    simple_midi(os.path.join(MIDI_DIR, 'guitar.mid'), [59, 55, 50, 45, 59, 55, 50, 45, 59])
if not os.path.exists(os.path.join(MIDI_DIR, 'bass.mid')):
    simple_midi(os.path.join(MIDI_DIR, 'bass.mid'), [35, 38, 40, 42, 35, 38, 40, 42, 35])
if not os.path.exists(os.path.join(MIDI_DIR, 'drums.mid')):
    simple_midi(os.path.join(MIDI_DIR, 'drums.mid'), [36, 38, 42, 38, 36, 38, 42, 38, 49])

SOUNDFONT = os.path.join(HERE, "sf2", "GeneralUser.sf2")
if not os.path.isfile(SOUNDFONT):
    print("!! Download a GM SoundFont (e.g. GeneralUser) into i_love_lemon/sf2/")
    sys.exit(1)

mix_wav = os.path.join(HERE, "demo.wav")
cmd = ["fluidsynth", "-ni", SOUNDFONT,
       os.path.join(MIDI_DIR, "guitar.mid"),
       os.path.join(MIDI_DIR, "bass.mid"),
       os.path.join(MIDI_DIR, "drums.mid"),
       "-F", mix_wav, "-r", "44100"]
subprocess.check_call(cmd)

# Convert to mp3 if ffmpeg exists
if shutil.which("ffmpeg"):
    subprocess.check_call(["ffmpeg", "-y", "-i", mix_wav, os.path.join(HERE, "demo.mp3")])
    print("Rendered --> demo.mp3")
else:
    print("Rendered --> demo.wav")
