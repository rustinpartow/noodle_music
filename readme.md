# Music-AI Song Production Toolkit

This repo hosts a **re-cyclable workflow** for writing math-/post-rock songs, from prompt → chart → quick audio mock-ups.

## ✨ Quick start

### One-liner quick-start (macOS)

```bash
# Install Homebrew if you don't have it already
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Clone repo and enter it
git clone <your-fork-url> music_ai && cd music_ai

# System binaries (fonts + renderers) – takes a few minutes
brew install lilypond fluidsynth ffmpeg

# Python env
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip && pip install -r requirements.txt

# Bootstrap first example
python3 scaffold_song.py my_first_song
curl -L -o my_first_song/sf2/GeneralUser.sf2 \
  https://github.com/urish/cgmusicbot/raw/master/soundfonts/GeneralUser_GS.sf2
cd my_first_song && make demo      # → chart_v3.pdf + demo.mp3
```

### Ubuntu / Debian equivalent

```bash
sudo apt update && sudo apt install -y lilypond fluidsynth ffmpeg python3-venv curl

# repo checkout …
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# …same scaffold_song.py + SoundFont + make demo flow…
```

### SoundFont
FluidSynth comes with a working SoundFont that we can use immediately:

```bash
# Copy the bundled SoundFont to your song
cp "/opt/homebrew/Cellar/fluid-synth/2.4.6/share/fluid-synth/sf2/VintageDreamsWaves-v2.sf2" \
   example_song/sf2/

# Point the Makefile at it
sed -i '' 's|^SOUNDFONT .*|SOUNDFONT      = sf2/VintageDreamsWaves-v2.sf2|' example_song/Makefile
```

Alternative: download FluidR3_GM (≈ 150 MB) for higher quality:
```bash
# Find a working download source and place in sf2/ folder
# Then update SOUNDFONT path in Makefile accordingly
```

### Troubleshooting
1. **`lilypond: command not found`** – verify Homebrew (or apt) install succeeded and `which lilypond` prints a path.
2. **`fluidsynth: No such file or directory`** – same: `which fluidsynth`.
3. **ValueError: message time must be int** – fixed in template; ensure your song was scaffolded after 2025-05-31.

Once the above runs cleanly, every new song is literally three commands:
```bash
source .venv/bin/activate
python3 scaffold_song.py new_song
make -C new_song demo
```

## 🗂️ Structure

```
/song-name/
├── song-prompt.md      # evolving brief
├── chart_v1.md         # skeletal chart
├── chart_v3.ly         # LilyPond score (final)
├── Makefile            # CLI render pipeline
├── scripts/            # utilities (split_midi.py …)
└── sf2/GeneralUser.sf2 # sample bank (user-provided)
```

## How it works

The Makefile orchestrates everything:
1. LilyPond compiles the score → `chart_v3.pdf` **+** multi-track MIDI.
2. A small Python helper splits the MIDI into guitar/bass/drum stems.
3. FluidSynth + SoundFont render each stem to audio.
4. FFmpeg aligns tracks, applies a brick-wall limiter (EBU **loudnorm**) and exports `demo.mp3`.

All targets are incremental – edit the score, re-run `make`, only the changed steps rebuild.

---

See `song_brief_template.md` for the collaborative songwriting framework.

## 🛠️ Environment setup

### First time on a given machine

```bash
# clone repo, then inside project root:
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt  # installs mido, midiutil, pydub

# system binaries (macOS)
brew install lilypond fluidsynth ffmpeg sfizz   # sfizz only if you want SFZ drums

# Ubuntu / Debian
sudo apt update && sudo apt install lilypond fluidsynth ffmpeg sfizz python3-venv
```

Place a GM SoundFont (e.g. `GeneralUser.sf2`) in each song's `sf2/` folder.  
Optional: point the `SOUNDFONT` variable in the Makefile to a different bank.

### Subsequent sessions

```bash
source .venv/bin/activate   # jump back into the virtualenv
# … work …
make -C my_song demo        # rebuild audio for «my_song»
```

Deactivate with `deactivate` when finished.

---



