# Auto-bounce pipeline for i_love_lemon
# Usage: make demo

SCORE          = chart.ly
PDF            = $(SCORE:.ly=.pdf)
MIDI           = $(SCORE:.ly=.midi)
MIDI_DIR       = midi
SOUNDFONT      = sf2/Arachno_SoundFont_v1.sf2
GUITAR_MID     = $(MIDI_DIR)/guitar.mid
BASS_MID       = $(MIDI_DIR)/bass.mid
DRUMS_MID      = $(MIDI_DIR)/drums.mid
WAV            = demo.wav
MP3            = demo.mp3

# Premium SoundFont options
ARACHNO_SF     = sf2/Arachno_SoundFont_v1.sf2
AIRFONT_SF     = sf2/Airfont_380_Final.sf2
DRUMM_SF       = sf2/Drumm_GM.sf2

# Humanization tool (requires mido: python3 -m pip install --break-system-packages mido)
HUMANIZE_TOOL  = python3 ../humanize_midi.py

.PHONY: all demo clean demo-premium demo-humanized test-humanization-levels test-guitar

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

# Premium SoundFont demos for A/B comparison
demo-premium: $(MIDI)
	@echo "🎵 Rendering with premium SoundFonts for comparison..."
	fluidsynth -ni $(ARACHNO_SF) $(MIDI) -F demo_arachno.wav -r 44100
	ffmpeg -y -i demo_arachno.wav -af loudnorm demo_arachno.mp3
	@echo "✅ Arachno demo: demo_arachno.mp3"
	@if [ -f $(AIRFONT_SF) ]; then \
		fluidsynth -ni $(AIRFONT_SF) $(MIDI) -F demo_airfont.wav -r 44100; \
		ffmpeg -y -i demo_airfont.wav -af loudnorm demo_airfont.mp3; \
		echo "✅ Airfont demo: demo_airfont.mp3"; \
	fi

# Refined MIDI humanization focused on instrument realism
demo-humanized: $(MIDI) $(ARACHNO_SF)
	@echo "🎵 Applying refined instrument humanization..."
	$(HUMANIZE_TOOL) $(MIDI) chart_v3_humanized.midi --velocity 8 --timing 5 --passes 2 --verbose
	fluidsynth -ni $(ARACHNO_SF) chart_v3_humanized.midi -F demo_real_humanized.wav -r 44100
	ffmpeg -y -i demo_real_humanized.wav -af loudnorm demo_real_humanized.mp3
	@echo "✅ Refined humanization complete: demo_real_humanized.mp3"
	@echo "🎧 Compare: demo.mp3 (robotic) vs demo_real_humanized.mp3 (humanized)"

# Test different levels of humanization for fine-tuning
test-humanization-levels: $(MIDI) $(ARACHNO_SF)
	@echo "🔬 Testing refined humanization levels..."
	@echo "Subtle (instrument-focused)..."
	$(HUMANIZE_TOOL) $(MIDI) chart_v3_subtle.midi -v 3 -t 2 -p 1
	fluidsynth -ni $(ARACHNO_SF) chart_v3_subtle.midi -F demo_subtle.wav -r 44100
	ffmpeg -y -i demo_subtle.wav -af loudnorm demo_subtle.mp3
	@echo "Natural (balanced realism)..."
	$(HUMANIZE_TOOL) $(MIDI) chart_v3_natural.midi -v 8 -t 5 -p 2
	fluidsynth -ni $(ARACHNO_SF) chart_v3_natural.midi -F demo_natural.wav -r 44100
	ffmpeg -y -i demo_natural.wav -af loudnorm demo_natural.mp3
	@echo "Expressive (performance-style)..."
	$(HUMANIZE_TOOL) $(MIDI) chart_v3_expressive.midi -v 15 -t 8 -p 2
	fluidsynth -ni $(ARACHNO_SF) chart_v3_expressive.midi -F demo_expressive.wav -r 44100
	ffmpeg -y -i demo_expressive.wav -af loudnorm demo_expressive.mp3
	@echo "✅ Refined humanization test complete!"
	@echo "🎧 Compare levels:"
	@echo "   🤖 Robotic:    demo.mp3"
	@echo "   🎵 Subtle:     demo_subtle.mp3"
	@echo "   🎵 Natural:    demo_natural.mp3"
	@echo "   🎵 Expressive: demo_expressive.mp3"

# Test guitar sounds to ensure they don't sound like piano!
test-guitar: test_guitar_fix.midi $(SOUNDFONT)
	@echo "🎸 Testing guitar sounds with rock-optimized soundfont..."
	fluidsynth -ni $(SOUNDFONT) test_guitar_fix.midi -F test_guitar_8rock.wav -r 44100
	ffmpeg -y -i test_guitar_8rock.wav -af loudnorm test_guitar_8rock.mp3
	@echo "✅ Guitar test with 8Rock11e: test_guitar_8rock.mp3"
	@if [ -f $(ARACHNO_SF) ]; then \
		fluidsynth -ni $(ARACHNO_SF) test_guitar_fix.midi -F test_guitar_arachno.wav -r 44100; \
		ffmpeg -y -i test_guitar_arachno.wav -af loudnorm test_guitar_arachno.mp3; \
		echo "✅ Guitar test with Arachno: test_guitar_arachno.mp3"; \
	fi

# Test guitar strumming patterns - block chords vs realistic strums
test-strumming: guitar_strum_test.midi $(ARACHNO_SF)
	@echo "🎸 Testing guitar strumming patterns..."
	fluidsynth -ni $(ARACHNO_SF) guitar_strum_test.midi -F strum_comparison.wav -r 44100
	ffmpeg -y -i strum_comparison.wav -af loudnorm strum_comparison.mp3
	@echo "✅ Strumming comparison: strum_comparison.mp3"
	@echo "🎧 Listen to the difference between:"
	@echo "   📋 Staff 1: Block chords (sounds like piano)"
	@echo "   🎸 Staff 2: Down-strums (bass→treble)"
	@echo "   🎸 Staff 3: Up-strums (treble→bass)"
	@echo "   🔥 Staff 4: Realistic mixed pattern"
	
test_guitar_fix.midi: test_guitar_fix.ly
	lilypond -dno-point-and-click -o test_guitar_fix test_guitar_fix.ly

guitar_strum_test.midi: guitar_strum_test.ly
	lilypond -dno-point-and-click -o guitar_strum_test guitar_strum_test.ly

chart_v3_strummed.midi: chart_v3_strummed.ly
	lilypond -dno-point-and-click -o chart_v3_strummed chart_v3_strummed.ly

# Compare original block chords vs realistic guitar strumming
compare-strumming: $(MIDI) chart_v3_strummed.midi $(ARACHNO_SF)
	@echo "🎸 Rendering ORIGINAL (block chords)..."
	fluidsynth -ni $(ARACHNO_SF) $(MIDI) -F demo_original.wav -r 44100
	ffmpeg -y -i demo_original.wav -af loudnorm demo_original.mp3
	@echo "🎸 Rendering STRUMMED (realistic guitar)..."
	fluidsynth -ni $(ARACHNO_SF) chart_v3_strummed.midi -F demo_strummed.wav -r 44100
	ffmpeg -y -i demo_strummed.wav -af loudnorm demo_strummed.mp3
	@echo "✅ Guitar comparison complete!"
	@echo "🎧 A/B Test Results:"
	@echo "   🤖 ORIGINAL (sounds like piano): demo_original.mp3"
	@echo "   🎸 STRUMMED (sounds like guitar): demo_strummed.mp3"

clean:
	rm -rf $(PDF) $(MIDI) $(MIDI_DIR) $(WAV) $(MP3) 
	rm -rf chart_v3_*.midi demo_*.wav demo_*.mp3 velocity_*.pdf velocity_*.midi velocity_*.wav velocity_*.mp3 humanized_chart.pdf humanized_chart.midi
	rm -rf test_guitar_*.midi test_guitar_*.wav test_guitar_*.mp3 test_guitar_*.pdf 
	rm -rf guitar_strum_test.midi guitar_strum_test.pdf strum_comparison.wav strum_comparison.mp3
	rm -rf chart_v3_strummed.midi chart_v3_strummed.pdf 