Recyclable Song Brief Template

0 · Overview 🗺️

A living framework for co‑writing math‑rock / post‑rock songs in three iterative passes (plus lyrics) and distributing crystal‑clear practice material to a three‑piece band (gtr + bass + drums).  Every song lives in its own sub‑folder and travels through the same life‑cycle:

Draft prompt ⇢ 2–3 back‑and‑forths to lock vibe + scaffolding

MVP chart (guitar‑only structure)

Pass 2 – add bass, riffs, strumming, drum roadmap

Pass 3 – polished PDF chart (multi‑layer detail) + **instrument voicing verification**

Lyrics + vocal melody

Optional audio mock‑up (see §5)

Throughout the process both the prompt and the charts get updated together. **Critically: always verify instrument voicings in audio renders to ensure they sound like the intended instruments, not sound effects.**

Folder layout (w/in current project files):

```bash
/song-name/
├── song-prompt.md     # evolves every round
├── chart_v1.md        # MVP chord sheet  
├── chart_v2.md        # bass + drums added
├── chart_v3.pdf       # final layered PDF
├── lyrics_melody.pdf
└── mockup-demo.mp3    # optional
```

File naming: chart_v#.ext, zero‑indexed iterations, ISO dates optional when helpful.

**0.1 · Instrument Voicing Determination 🎛️**

**What controls instrument sound in our pipeline:**

| Factor | Impact | Examples |
|--------|--------|----------|
| **midiInstrument setting** | Primary sound selection | `"acoustic guitar (nylon)"` = fairy sound, `"electric guitar (clean)"` = math rock |
| **Volume/presence in mix** | **CRITICAL: Can instrument be heard?** | `"synth bass 1"` = too quiet, `"electric bass (pick)"` = audible |
| **SoundFont file** | **Sample quality & drum kit variety** | **New:** `Arachno_SoundFont_v1.sf2` (premium), `8Rock11e.sf2` (rock), `Drumm GM.sf2` (drum variety) |
| **Playing technique** | Articulation & attack | Staccato rests (`r`) for punch, sustained notes for drones |
| **Register/octave** | Timbral character | Low bass vs high bass, guitar chord voicings |

**Common voicing fixes:**
- **Fairy guitar** → Change from `"acoustic guitar (nylon)"` to `"electric guitar (clean)"`
- **Inaudible bass** → Avoid `"synth bass 1"` (too quiet), try `"electric bass (pick)"`, `"fretless bass"`, `"slap bass 1"`
- **Weak drums** → Ensure proper `\drummode` and standard kit mapping
- **Math rock punch** → Add staccato rests (`r`) between chord hits

**Bass consistency goal:** Establish one reliable bass sound across all songs for workflow efficiency.

**🎵 SoundFont Collection (2025 Update)**

We now have access to a **comprehensive 495-soundfont collection** that dramatically expands our audio capabilities:

**Recommended SoundFonts by Use Case:**
- **High-Quality General:** `Arachno_SoundFont_v1.sf2` (148MB) - Premium across all instruments
- **Rock-Optimized:** `8Rock11e.sf2` (8.1MB) - Specialized for guitar-driven rock music
- **Drum Kit Variety:** `Drumm GM.sf2`, `Drums_Alex_GM_old_drumkits.sf2` - Solves standard kit limitation
- **Quick Iteration:** `TimGM6mb.sf2` (6MB) - Fast loading, good quality

**Integration Process:**
1. Copy desired soundfont to project's `sf2/` directory
2. Update `SOUNDFONT` variable in `Makefile`
3. Test render with `make demo`
4. Document choice in project's "Insights" section

See `soundfont_collection_guide.md` for complete documentation and quality assessments.

**Voicing verification checklist:**
- [ ] Guitar sounds electric, not acoustic/fairy
- [ ] Bass is **audible and present** in the mix
- [ ] Bass sounds like actual bass, not sound effects
- [ ] Drums sound like drums, not bleeps
- [ ] Math rock sections have proper punch/articulation

**🤖 MIDI Humanization Checklist (2025 - UPDATED):**
- [ ] **Rhythmic variety:** Strategic rests break mechanical patterns (`r16`, `r8`)
- [ ] **Pattern variation:** Sections have musical differences, no copy-paste repetition
- [ ] **Instrumental interaction:** Guitar/bass offset timing creates ensemble feel
- [ ] **Textural contrast:** Mix of staccato (crisp) and legato (sustained) sections
- [ ] **Musical dynamics:** Use crescendos/diminuendos for arc (these work)
- [ ] **Drum variation:** Ghost notes, fills, accent patterns support musical phrase

**NOTE:** Technical velocity/timing micro-adjustments don't work audibly in our LilyPond→FluidSynth pipeline. Focus on **musical variety** over **technical humanization tricks**.

**0.2 · Key Insights 💡**

**Critical discoveries from song development:**

| Insight | Technical Detail | Impact |
|---------|------------------|--------|
| **Math rock punch = staccato + electric** | Add `r` (rests) between chord hits + `"electric guitar (clean)"` | Transforms flowing arpeggios into crispy, articulated attacks |
| **"Fairy guitar" problem** | `"acoustic guitar (nylon)"` sounds like little fairies, not rock | Always use `"electric guitar (clean)"` for math/post-rock |
| **Bass voicing hierarchy** | `"electric bass (finger)"` = cheap → `"synth bass 1"` = too quiet → `"synth bass 2"` = awful plane noise → `"electric bass (pick)"` = best | Avoid synth bass for rock genres - electric bass (pick) most reliable |
| **Bass octave matters** | Bass too high = muddy mix, competes with guitar | Use `,,` and `,,,` for proper bass register |
| **Bass role: complement, don't copy** | Bass copying guitar = muddy, amateur sound | Bass = sustained roots/counter-rhythms while guitar is busy |
| **Guitar chord voicings** | Wide voicings sound like single notes in MIDI | Use compact voicings: `<b, fis b>` not `<b fis' b''>` |
| **Sustained vs staccato context** | Staccato everywhere = choppy, gaps; sustained everywhere = muddy | Staccato for math rock punch, sustained for drones/chords |
| **Arrangement fullness critical** | Excessive rests = awkward gaps, amateur sound | Fill arrangements with sustained notes, ties, fuller patterns |
| **Drum intensity matches genre** | Minimal drums = boring, doesn't support energy | Math rock needs intense, complex drum patterns throughout |
| **Distortion for electric feel** | Clean tones = fairy/acoustic feel even with electric instruments | Use "distorted guitar" and edgy bass for rock genres |
| **Drum kit selection matters** | Default drums vs rock kit = different character | Use "rock kit" for rock genres, not default percussion |
| **Articulation defines genre** | Same notes + different spacing = different genre feel | Sustained = post-rock, staccato = math rock, mixed = dynamic |
| **midiInstrument is primary** | This setting overrides everything else in sound character | Check this FIRST when instrument doesn't sound right |
| **DrumStaff requires no midiInstrument** | `\new DrumStaff` auto-routes to MIDI channel 10, setting `midiInstrument` causes weird sounds | Never set midiInstrument for drums - channel 10 handles all drum sounds |
| **Bass voicing hierarchy updated** | `"electric bass (pick)"` = decent → `"slap bass 1"` = more aggressive rock sound | Slap bass variants better for rock than electric bass |
| **Named drum kits often unavailable** | MIDI spec includes power kit, room kit, etc. but SoundFonts may not include them | Stick with default DrumStaff (no midiInstrument) for reliable drum sounds |
| **Acoustic bass more natural** | `"acoustic bass"` sounds more natural than electric/slap variants for rock | Acoustic bass less synthy, more organic than electric bass options |
| **Overdriven vs distorted guitar** | `"overdriven guitar"` sounds more human/angry, `"distorted guitar"` more robotic | For aggressive human feel, use overdriven guitar over distorted |
| **Human feel via imperfect timing** | Adding rests and broken patterns prevents robotic/mechanical sound | Use `r` rests and irregular spacing to add human imperfection |
| **Math rock = snare-heavy drums** | Math rock needs more snare hits than kick for proper drive and aggression | Prioritize snare patterns over hi-hat/kick for math rock feel |
| **Slap bass more aggressive** | `"slap bass 1"` more aggressive than `"acoustic bass"` for rock | When user wants "rock bass," slap bass > acoustic bass |
| **SoundFont corruption common** | Multiple SoundFonts (TimGM6mb.sf2, MiniSoft.sf2, example.sf2) had RIFF chunk corruption | Only use VintageDreamsWaves-v2.sf2, download fresh SoundFonts for drum alternatives |
| **Electronic drum problem** | VintageDreamsWaves-v2.sf2 drums sound robotic/electronic for math rock | Consider: different SoundFont download, sample replacement, or velocity variation |
| **Crispy guitar intro technique** | Remove sustains (~) and add staccato rests for crispy math rock attack | `<chord>8 r <chord>8 r` pattern instead of `<chord>4~ <chord>4` for crispness |
| **SoundFont Collection (2025)** | 495-soundfont collection vastly improves instrument realism and drum variety | `Arachno_SoundFont_v1.sf2` = premium quality, `8Rock11e.sf2` = rock-optimized, dedicated drum soundfonts solve kit variety issue |

**Proven techniques:**
- **Math rock crisp**: `<chord>8 r <chord>16 <chord>` (eighth + rest + sixteenths)
- **Punchy bass**: Match guitar's rest patterns, don't just play roots
- **Genre consistency**: All instruments should use same articulation approach
- **Sound verification**: Always listen immediately after instrument changes

1 · House Style / Aesthetic North‑Star 🎨

Aspect

Detailed colour palette

Melodic DNA

Early Foals (tapped‑arpeggio urgency) meets Radiohead (In Rainbows‑era spaciousness) with JP/UK post‑rock polish.

Textural references

Hikes – "Crown Shyness" ➜ wispy, fluttering twin‑guitar motifs.

Stage Kids – "Welcome to the Jungle" ➜ "jungle‑jazz" layering, lush percussive piano and delayed guitar over a 180 BPM B‑minor pocket.

Brontide – "Tonitro" ➜ thunderous dynamic lift at ≈3:00, syncopated punches over polymetric accents.

Mandatory traits

• Noodly but purposeful phrases

• Seamless, "buttery" transitions

• Surprise metre flips (tasteful, not gimmicky)

• Breakdowns that explode then resolve back into airiness

• Guitar + bass complement (no copy‑pasting)

• Drums intermediate‑friendly (ghost‑note groove > blast‑beat heroics)

• **Instruments must sound like their intended instruments** (bass = bass, not haunted house effects)

Player skill‑ceilings

Guitar: Intermediate / upper‑intermediate (tapping & partial‑barre ok).

Bass: intermediate, melodic lines ok, slap minimal.

Drums: intermediate, comfy with occasional syncopation & odd bars, occasional double‑kick. Complex counting is challenging unless we provide secret tricks within a song.

Tempo & key defaultsUnless otherwise specified, gravitate towards 120–190 BPM and modal minor keys (B‑, E‑, F#‑) to suit the moody‑energetic blend. Short burst passages up to ~200 BPM are fair game (≤ 2 bars) if they serve a dynamic punch and remain comfortable for rhythm section.

2 · Song‑Specific Prompt (iterative)

Fill as much as you know; leave blanks for later refinement.

Field

Notes / Examples

Working title

e.g. "Starlit Static"

Elevator vibe

One‑liner mood description

Tempo / reference track

"140 BPM – Foals 'Red Socks Pugie'."

Key / tuning

Standard, Drop D, etc.

Time‑sig map

4/4 main, 2‑bar 7/8 tag in chorus.

Length & structure

Intro 8b → Verse 16b → …

Guitar difficulty cap

Max fret, techniques allowed.

Bass role

Counter‑melody, root‑drive, etc.

Drum feel

Ghost‑note shuffle, halftime chorus…

Tone palette & FX

Delay, fuzz, trem‑picking…

**Instrument voicing notes**

**Track specific timbral expectations: crispy guitar, warm bass, tight drums**

**Include volume/presence requirements: bass must be audible and punchy, guitar should cut through, drums supportive but present**

Lyrical seed (opt.)

Imagery or phrase bucket.

3 · Iteration Workflow ⚙️

Prompt draft together here in chat → save /song‑name/song‑prompt.md

MVP chart: skeletal chord sheet (gtr), markers: {RIFF‑A}, {BREAK}

Add bass & drums: riff tabs, strumming, drum groove shorthand (e.g., x‑h‑hh‑|).

**Audio verification pass**: Render demo, verify all instruments sound correct (bass = bass, drums = drums, guitar = guitar)

Final PDF (two layers):Layer 1 Nashville‑style overview; Layer 2 staff/TAB + groove notation.

Lyrics & top‑line added on separate PDF.

Mock‑up (optional) – see §5.

Feedback cadence: drop comments in‑line (<>), or plain‑language notes in chat.I integrate, bump version, & we rinse‑repeat. **Always mention instrument voicing issues immediately upon hearing demo.**

4 · File‑generation & Tech Stack 🛠️

Output

Toolchain

PDF charts

LilyPond → PDF (or MuseScore export); renders embedded in chat.

MIDI + MP3 demo

1️⃣ MuseScore / Guitar Pro MIDI export  2️⃣ FreeConvert or built‑in SoundFont render → MP3.

Tab snippets in chat

Vextab or fenced code blocks for quick previews.

Audio iteration

If quick feedback needed: Tiny 4‑bar loops generated via Tone.js & shared as MP3.

5 · Audio Mock‑up Options 🎧

Level

What you get

Turn‑time

Pros

Cons

A – Raw MIDI

.mid with each instrument channelled

minutes

tiny, editable

sterile playback

B – SoundFont MP3

MIDI rendered through high‑quality GM SoundFont

<1 h

more realistic kit & bass

generic guitar tone

C – Amp‑sim bounce

Guitar & bass re‑amped (Amp Lion / ToneLib), EZ‑Drummer kit

~1 day

nearly mix‑ready

heavier file sizes

D – Full DAW sketch

Re‑amped + automation, basic mix

≈ 15–30 min (AI‑render) + optional manual polish

vibe feels real

heavier CPU + additional libraries

Pick the tier per song; we can escalate if needed.  I'll supply source MIDI so you can import into Logic/Live later.

5.1 · Local CLI Render Pipeline 🖥️

When working on a macOS (or Linux) workstation we can skip online converters and run an **end-to-end bounce** in one command:

```bash
cd /song-name
make demo       # renders PDF chart, exports MIDI stems, re-amps + mixes to demo.mp3
```

What the default `Makefile` does:

1. **Score ⇢ chart** – Compiles `chart_v3.ly` with LilyPond, emitting PDF + a multi-track MIDI.
2. **Split MIDI** – Uses a short Python helper (`scripts/split_midi.py`) to fan-out guitar, bass & drum tracks into `midi/`.
3. **Re-amp & sample**
   • Guitar/Bass → `fluidsynth` + hi-gain/clean SoundFonts _or_ ToneLib GFX CLI if installed.
   • Drums → `sfizz` running an SFZ kit (e.g. **SM MegaReaper**).
4. **Mixdown** – `ffmpeg` aligns stems, applies a safety limiter (`loudnorm`) and spits `demo.wav` + `demo.mp3`.
5. **Quality tiers** – Changing a single variable lets us bump from Tier B to C / D by swapping SoundFonts for amp-sim IRs or even external VST renders.

All commands are declarative – the Makefile only (re)builds what is missing or out-of-date, so iterating is instant after the first bounce.

Dependencies (macOS example):
```bash
brew install lilypond fluidsynth sfizz ffmpeg python
pip install mido python-lilypond-parser pydub
```

👆 Modify the SoundFont / SFZ paths per project in the song folder's local `.env`.

6 · Audio & Production Glossary 📖

Term

Quick definition

DAW

Digital Audio Workstation – software like Logic, Ableton Live, or Reaper where tracks are recorded, edited, and mixed.

SoundFont MP3

An MP3 rendered from MIDI using a high‑quality SoundFont (a sample‑based instrument bank) for more realistic playback than the default "General MIDI" sounds.

Drum VST

A Virtual Studio Technology plug‑in that emulates drums (e.g., EZ‑Drummer, Superior Drummer). Feeds on MIDI and outputs multitrack drum audio.

FX automation

Drawing parameter curves (e.g., delay mix, filter cutoff) over time so effects move dynamically during the song.

7 · Your Next Steps 🚦

Review & tweak this template – nudge any table headers or defaults.

Answer / start filling the Song‑Specific Prompt table for Song #1.

Choose an audio mock‑up tier (A–D). (You've indicated Tier 4 is ideal – see note below.)

Drop any fresh influences you're currently spinning.

Tier 4 feasibility – Yes, doable. Expect ~2–3‑day turnaround per song for a rough‑mix MP3 (re‑amped guitars, EZ‑Drummer kit, basic bus compression, no fancy mastering).

I'll then spin up song‑prompt.md and the MVP chart in the correct folder and we're off.

7 · Glossary 📖

Term

Quick definition

DAW

Digital Audio Workstation – software like Logic, Ableton Live, Reaper that lets you record, arrange, and mix audio/MIDI.

SoundFont MP3

An MP3 bounced from a MIDI file that's been rendered through a SoundFont—a lightweight sample bank giving instruments more realistic timbres than default General MIDI.

Drum VST

A plug‑in drum instrument (e.g., EZDrummer, Superior Drummer) that triggers high‑quality multi‑sampled kits from MIDI.

FX automation

Moving parameters (e.g., delay feedback, filter cutoff) over time in the DAW so they evolve dynamically in the mix.

Amp sim

Software that emulates guitar/bass amplifiers and cabs, turning DI tracks into lifelike tones.