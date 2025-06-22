# SoundFont Collection Setup

## Quick Setup (if you have the ZIP archive)

1. **Extract the archive:**
   ```bash
   # If you have 500_Soundfonts_Full_GM_Sets.zip
   unzip -q 500_Soundfonts_Full_GM_Sets.zip -d temp_extraction/
   ```

2. **Organize by category:**
   ```bash
   # Move soundfonts to appropriate categories
   python soundfont_sampler.py --organize-collection temp_extraction/
   ```

3. **Test with existing project:**
   ```bash
   python soundfont_sampler.py --project i_love_lemon --recommend
   ```

## Manual Organization

If organizing manually, use these guidelines:

- **general/**: Arachno*, Merlin*, Timbres*, MuseScore_General*, *GM*.sf2
- **rock/**: *Rock*, *Guitar*, *Metal*, *Distort*
- **drums/**: *Drum*, *Kit*, *Percussion*
- **orchestral/**: *Orchestra*, *Symphony*, *Classical*, *Piano*
- **performance/**: Files under 15MB with quality score > 3
- **top_quality/**: Files over 100MB with quality score > 7

## Testing Workflow

1. Copy soundfont to project: `cp soundfonts_collection/category/font.sf2 project/sf2/`
2. Update Makefile: `SOUNDFONT = sf2/font.sf2`
3. Test render: `make demo`
4. Document results in project's README or Insights section
