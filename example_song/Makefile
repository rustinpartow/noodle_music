# Auto-bounce pipeline for example_song
# Usage: make demo

SCORE          = chart_v3.ly
PDF            = $(SCORE:.ly=.pdf)
MIDI           = $(SCORE:.ly=.midi)
MIDI_DIR       = midi
SOUNDFONT      = sf2/VintageDreamsWaves-v2.sf2
GUITAR_MID     = $(MIDI_DIR)/guitar.mid
BASS_MID       = $(MIDI_DIR)/bass.mid
DRUMS_MID      = $(MIDI_DIR)/drums.mid
WAV            = demo.wav
MP3            = demo.mp3

.PHONY: all demo clean

all: demo

################################################################################
# Chart + MIDI
################################################################################

$(PDF) $(MIDI): $(SCORE)
	lilypond -dno-point-and-click -o $(basename $<) $<

################################################################################
# Split multi-track MIDI into stems (requires python -m pip install mido)
################################################################################

$(MIDI_DIR):
	mkdir -p $@

$(GUITAR_MID): $(MIDI) | $(MIDI_DIR)
	python3 scripts/split_midi.py $< guitar 0 $@

$(BASS_MID): $(MIDI) | $(MIDI_DIR)
	python3 scripts/split_midi.py $< bass 1 $@

$(DRUMS_MID): $(MIDI) | $(MIDI_DIR)
	python3 scripts/split_midi.py $< drums 9 $@

################################################################################
# Render audio (Fluidsynth) & mix (ffmpeg)
################################################################################

$(WAV): $(MIDI) $(SOUNDFONT)
	fluidsynth -ni $(SOUNDFONT) $(MIDI) -F $@ -r 44100

$(MP3): $(WAV)
	ffmpeg -y -i $< -af loudnorm $@

demo: $(MP3)

clean:
	rm -rf $(PDF) $(MIDI) $(MIDI_DIR) $(WAV) $(MP3) 