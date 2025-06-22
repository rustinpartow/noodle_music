# Guitar Humanization Technique

## **Problem:** LilyPond Guitar Sounds "Robotic"

**Root cause:** Block chord attacks sound like piano, not guitar.

## **Solution: 6-Step Fix**

### **1. Guitar Strumming (Not Block Chords)**
```lilypond
% ❌ ROBOTIC: Block chords
<b, fis b>8 r <b, fis b>8 r

% ✅ HUMAN: Guitar strumming  
\arpeggioArrowUp
<b, fis b>8\arpeggio\mf r     % Down-strum (bass→treble)
\arpeggioArrowDown 
<b, fis b>8\arpeggio\p r      % Up-strum (treble→bass)
```

**CRITICAL:** LilyPond arrows are counterintuitive:
- `\arpeggioArrowUp` = **DOWN-STRUM** (bass to treble)
- `\arpeggioArrowDown` = **UP-STRUM** (treble to bass)

### **2. Dynamic Expression**
```lilypond
% Add velocity variation
<chord>8\arpeggio\f r    % Forte (loud)
<chord>8\arpeggio\mf r   % Medium forte
<chord>8\arpeggio\p r    % Piano (soft)
```

### **3. Human Timing Variation**
```lilypond
% Mix different rest values for imperfection
<chord>8\arpeggio r      % Standard
<chord>8\arpeggio r16    % Shorter gap
<chord>16\arpeggio r8    % Different timing
```

### **4. Pattern Variation**
```lilypond
% Never use identical repetition
% Pattern A
\arpeggioArrowUp <chord>8\arpeggio\f r
% Pattern A variation (slightly different)
\arpeggioArrowDown <chord>8\arpeggio\mf r16
```

### **5. Proper Instrument Voicing**
```lilypond
\new Staff \with {
  midiInstrument = #"electric guitar (clean)"  % Better than "overdriven"
  midiMinimumVolume = #0.3
  midiMaximumVolume = #0.9
} { \global \guitarMusic }
```

### **6. Fix Sustain Issues - CRITICAL**
**Problem:** Short chords cut off abruptly (like yanking the power cord), not the duration being too short.

**Solution:** Let the soundfont handle natural decay - don't artificially extend with ties.

```lilypond
% ❌ WRONG: Making notes longer with ties
<chord>8\arpeggio\f~ <chord>16\arpeggio r16

% ✅ RIGHT: Short notes with natural release
<chord>8\arpeggio\f r    % SoundFont handles the decay naturally
```

**Key insight:** The issue is **abrupt termination**, not **insufficient duration**. Real guitar chords fade out naturally even when short. Don't fight the soundfont's natural release envelope.

## **Result**
Guitar sounds like a human playing guitar, not a robot playing piano.

## **Warning**
Technical MIDI post-processing can make things worse ("baby playing synth" effect). Musical humanization is primary. 