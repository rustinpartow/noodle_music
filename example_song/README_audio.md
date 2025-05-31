# Tier D Audio Render Guide · **example_song**

## 1 · Install dependencies

### macOS
```bash
brew install python fluidsynth ffmpeg
pip install midiutil pydub
```

### Ubuntu/Debian
```bash
sudo apt update && sudo apt install python3-pip fluidsynth ffmpeg
pip3 install midiutil pydub
```

Download a free GM SoundFont (e.g. `GeneralUser.sf2` from S. Christian Collins) and place it in:
```
example_song/sf2/GeneralUser.sf2
```

## 2 · Run renderer
```bash
cd example_song
python render.py
```
WAV (and MP3 if `ffmpeg` is present) will appear in the same folder.

---

## 3 · Makefile one-liner (Tier B→D)
```bash
make demo  # builds chart PDF, splits MIDI, bounces demo.mp3
```
The Makefile is self-documented – open it to swap kits (SFZ) or point the SOUNDFONT variable to a different bank.

> Tip: remember to `source ../../.venv/bin/activate` (or similar) before running `make demo` so Python helpers and `mido` are available.
