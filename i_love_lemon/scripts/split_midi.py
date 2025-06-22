#!/usr/bin/env python3
"""Split a multi-channel MIDI file into single-channel stem.

Usage: python split_midi.py SOURCE "stem_name" CHANNEL OUTPUT.mid
"""

import sys
from pathlib import Path
import mido

if len(sys.argv) != 5:
    print("Usage: split_midi.py SOURCE stem_name CHANNEL OUTPUT.mid")
    sys.exit(1)

src, name, channel_str, out = sys.argv[1:]
channel = int(channel_str)

ticks_per_beat = mido.MidiFile(src).ticks_per_beat
out_mid = mido.MidiFile(ticks_per_beat=ticks_per_beat)
track = mido.MidiTrack()
track.name = name
out_mid.tracks.append(track)

for msg in mido.MidiFile(src):
    if msg.type in ("note_on", "note_off") and msg.channel == channel:
        track.append(msg.copy(time=int(msg.time)))
    elif msg.is_meta:
        track.append(msg)

out_mid.save(out)
print(f"Wrote {out}") 