# Makefile for "I. love. lemon." - RICH MATH ROCK VERSION

# Use the GIANT SoundFont for maximum richness
SOUNDFONT = sf2/GiantSoundfontV6.4MelodicBank_NoDrums.sf2
# Alternative: specialized guitar distortion SoundFont
GUITAR_SOUNDFONT = sf2/Guitar_Kamac_Distortion_400k.sf2

# High quality audio settings for rich sound
AUDIO_QUALITY = -r 48000 -g 0.8

all: chart.midi chart.wav

chart.midi: chart.ly
	lilypond --output=. chart.ly

chart.wav: chart.midi
	fluidsynth -ni $(SOUNDFONT) chart.midi -F chart.wav $(AUDIO_QUALITY)

# Alternative version with guitar distortion SoundFont
chart_guitar.wav: chart.midi
	fluidsynth -ni $(GUITAR_SOUNDFONT) chart.midi -F chart_guitar.wav $(AUDIO_QUALITY)

# Test both versions
test: chart.wav chart_guitar.wav
	@echo "Generated rich versions:"
	@echo "  chart.wav - Using GIANT SoundFont (569MB)"
	@echo "  chart_guitar.wav - Using specialized guitar distortion"

clean:
	rm -f *.midi *.wav *.pdf

.PHONY: all test clean 