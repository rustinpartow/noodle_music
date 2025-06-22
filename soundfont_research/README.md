# SoundFont Research

This folder contains research and tooling for a collection of **495 high-quality SoundFonts** extracted from the `500_Soundfonts_Full_GM_Sets.zip` archive.

## Quick Start

**For immediate use:**
- Check `soundfont_systematic_catalog.md` for curated recommendations by use case
- Copy proven SoundFonts from `soundfonts_collection/` to your project's `sf2/` folder
- Update your project's Makefile to use the new SoundFont

**For development:**
- See `todo.md` for prioritized tasks to make this collection more useful
- Focus on multi-SoundFont rendering to unlock premium melodic-only fonts

## Key Files

- **`todo.md`** - Prioritized roadmap for future development
- **`soundfont_systematic_catalog.md`** - Curated recommendations and usage guide
- **`soundfonts_collection/`** - 495 SoundFonts organized by category
- **`analyze_soundfonts.py`** - Basic analysis tool (needs expansion)

## Current Limitations

1. **Giant SoundFont Problem:** Premium fonts like `GiantSoundfontV6.4MelodicBank_NoDrums.sf2` (569MB) can't be used because they lack drums and FluidSynth can't easily mix multiple SoundFonts

2. **Manual Testing Required:** No automated quality assessment pipeline exists

3. **Poor Integration:** Requires manual file copying and Makefile editing to test options

## Proven Solutions

- **Arachno SoundFont v1.0** (148MB) - Excellent all-around choice, GM-complete
- **8Rock11e.sf2** (8.1MB) - Good for quick rock iterations
- **Drumm GM.sf2** (97MB) - Superior drum samples, fixes robotic issues

See the systematic catalog for detailed recommendations by genre and use case.

---

**Status:** Research phase - practical implementation needed 