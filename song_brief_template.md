Recyclable Song Brief Template

0 · Overview 🗺️

A living framework for co‑writing math‑rock / post‑rock songs in three iterative passes (plus lyrics) and distributing crystal‑clear practice material to a three‑piece band (gtr + bass + drums).  Every song lives in its own sub‑folder and travels through the same life‑cycle:

Draft prompt ⇢ 2–3 back‑and‑forths to lock vibe + scaffolding

MVP chart (guitar‑only structure)

Pass 2 – add bass, riffs, strumming, drum roadmap

Pass 3 – polished PDF chart (multi‑layer detail)

Lyrics + vocal melody

Optional audio mock‑up (see §5)

Throughout the process both the prompt and the charts get updated together.

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

1 · House Style / Aesthetic North‑Star 🎨

Aspect

Detailed colour palette

Melodic DNA

Early Foals (tapped‑arpeggio urgency) meets Radiohead (In Rainbows‑era spaciousness) with JP/UK post‑rock polish.

Textural references

Hikes – “Crown Shyness” ➜ wispy, fluttering twin‑guitar motifs.

Stage Kids – “Welcome to the Jungle” ➜ “jungle‑jazz” layering, lush percussive piano and delayed guitar over a 180 BPM B‑minor pocket.

Brontide – “Tonitro” ➜ thunderous dynamic lift at ≈3:00, syncopated punches over polymetric accents.

Mandatory traits

• Noodly but purposeful phrases

• Seamless, “buttery” transitions

• Surprise metre flips (tasteful, not gimmicky)

• Breakdowns that explode then resolve back into airiness

• Guitar + bass complement (no copy‑pasting)

• Drums intermediate‑friendly (ghost‑note groove > blast‑beat heroics)

Player skill‑ceilings

Rustin (gtr): upper‑intermediate (tapping & partial‑barre ok).

Dani (bass): intermediate, melodic lines ok, slap minimal.

Chris (drums): intermediate, comfy with syncopation & odd bars, no double‑kick.

Tempo & key defaultsUnless otherwise specified, gravitate towards 120–190 BPM and modal minor keys (B‑, E‑, F#‑) to suit the moody‑energetic blend. Short burst passages up to ~200 BPM are fair game (≤ 2 bars) if they serve a dynamic punch and remain comfortable for Dani & Chris.

2 · Song‑Specific Prompt (iterative)

Fill as much as you know; leave blanks for later refinement.

Field

Notes / Examples

Working title

e.g. “Starlit Static”

Elevator vibe

One‑liner mood description

Tempo / reference track

"140 BPM – Foals ‘Red Socks Pugie’."

Key / tuning

Standard, Drop D, etc.

Time‑sig map

4/4 main, 2‑bar 7/8 tag in chorus.

Length & structure

Intro 8b → Verse 16b → …

Guitar difficulty cap

Max fret, techniques allowed.

Bass role

Counter‑melody, root‑drive, etc.

Drum feel

Ghost‑note shuffle, halftime chorus…

Tone palette & FX

Delay, fuzz, trem‑picking…

Lyrical seed (opt.)

Imagery or phrase bucket.

3 · Iteration Workflow ⚙️

Prompt draft together here in chat → save /song‑name/song‑prompt.md

MVP chart: skeletal chord sheet (gtr), markers: {RIFF‑A}, {BREAK}

Add bass & drums: riff tabs, strumming, drum groove shorthand (e.g., x‑h‑hh‑|).

Final PDF (two layers):Layer 1 Nashville‑style overview; Layer 2 staff/TAB + groove notation.

Lyrics & top‑line added on separate PDF.

Mock‑up (optional) – see §5.

Feedback cadence: drop comments in‑line (<>), or plain‑language notes in chat.I integrate, bump version, & we rinse‑repeat.

4 · File‑generation & Tech Stack 🛠️

Output

Toolchain

PDF charts

LilyPond → PDF (or MuseScore export); renders embedded in chat.

MIDI + MP3 demo

1️⃣ MuseScore / Guitar Pro MIDI export  2️⃣ FreeConvert or built‑in SoundFont render → MP3.

Tab snippets in chat

Vextab or fenced code blocks for quick previews.

Audio iteration

If quick feedback needed: Tiny 4‑bar loops generated via Tone.js & shared as MP3.

5 · Audio Mock‑up Options 🎧

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

B – SoundFont MP3

MIDI rendered through high‑quality GM SoundFont

<1 h

more realistic kit & bass

generic guitar tone

C – Amp‑sim bounce

Guitar & bass re‑amped (Amp Lion / ToneLib), EZ‑Drummer kit

~1 day

nearly mix‑ready

heavier file sizes

D – Full DAW sketch

Re‑amped + automation, basic mix

≈ 15–30 min (AI‑render) + optional manual polish

vibe feels real

heavier CPU + additional libraries

Pick the tier per song; we can escalate if needed.  I’ll supply source MIDI so you can import into Logic/Live later.

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

👆 Modify the SoundFont / SFZ paths per project in the song folder’s local `.env`.

6 · Audio & Production Glossary 📖

Term

Quick definition

DAW

Digital Audio Workstation – software like Logic, Ableton Live, or Reaper where tracks are recorded, edited, and mixed.

SoundFont MP3

An MP3 rendered from MIDI using a high‑quality SoundFont (a sample‑based instrument bank) for more realistic playback than the default “General MIDI” sounds.

Drum VST

A Virtual Studio Technology plug‑in that emulates drums (e.g., EZ‑Drummer, Superior Drummer). Feeds on MIDI and outputs multitrack drum audio.

FX automation

Drawing parameter curves (e.g., delay mix, filter cutoff) over time so effects move dynamically during the song.

7 · Your Next Steps 🚦

Review & tweak this template – nudge any table headers or defaults.

Answer / start filling the Song‑Specific Prompt table for Song #1.

Choose an audio mock‑up tier (A–D). (You’ve indicated Tier 4 is ideal – see note below.)

Drop any fresh influences you’re currently spinning.

Tier 4 feasibility – Yes, doable. Expect ~2–3‑day turnaround per song for a rough‑mix MP3 (re‑amped guitars, EZ‑Drummer kit, basic bus compression, no fancy mastering).

I’ll then spin up song‑prompt.md and the MVP chart in the correct folder and we’re off.

7 · Glossary 📖

Term

Quick definition

DAW

Digital Audio Workstation – software like Logic, Ableton Live, Reaper that lets you record, arrange, and mix audio/MIDI.

SoundFont MP3

An MP3 bounced from a MIDI file that’s been rendered through a SoundFont—a lightweight sample bank giving instruments more realistic timbres than default General MIDI.

Drum VST

A plug‑in drum instrument (e.g., EZDrummer, Superior Drummer) that triggers high‑quality multi‑sampled kits from MIDI.

FX automation

Moving parameters (e.g., delay feedback, filter cutoff) over time in the DAW so they evolve dynamically in the mix.

Amp sim

Software that emulates guitar/bass amplifiers and cabs, turning DI tracks into lifelike tones.