\version "2.24.0"

\header {
  title = "I. love. lemon."
  composer = "Vienna Lager Vibes"
}

%%%% Global settings
global = {
  \tempo 4 = 120
  \time 7/4
  \key b \minor
}

%%%% LEAD GUITAR - REFINED, NO SLOPPY SHIT
leadGuitarMusic = {
  % INTRO - Math rocky and mysterious - TIGHT TIMING
  \repeat unfold 2 {
    % THE CENTRAL THEME - confident, precise timing
    \arpeggioArrowUp
    <b, fis b>4\mp\arpeggio r2 r4 |
    \arpeggioArrowDown
    <fis, cis fis>4\p\arpeggio r2 r4 |
    % LISTENING to rhythm guitar's response - musical conversation
    \arpeggioArrowUp
    <e, b, e>4\mp\arpeggio r2 r4 |
    
    % TIGHT melodic statement - NO SLOPPY TIMING
    b4\mp d4\p fis4\pp a4\ppp |
  }
  
  % 0:35 - FIXED SLOPPY LICK! Tight, coordinated timing
  \repeat unfold 4 {
    % TIGHT B minor theme - NO SLOPPY SHIT
    \arpeggioArrowUp
    <b, d fis>4\mp\arpeggio r4 <d fis a>4\p\arpeggio r4 |
    <g b d'>4\mp\arpeggio r4 <a cis' e'>4\p\arpeggio r4 |
    
    % REFINED tapping - precise 16th notes, not sloppy
    b16\mf d16\mp fis16\mf a16\mp b16\mf d'16\mp fis'16\mf a'16\mp b'16\mf d''16\mp fis''16\mf a''16\mp b''16\mf r8 |
  }
  
  % 0:50 - COMPLETION MOMENT (not 0:45 shitty bridge!)
  \repeat unfold 4 {
    % PROPER KEY - staying in B minor, no out-of-key shit
    <b, d fis>4\p~ <b, d fis>8\pp r8 <d fis a>4\p~ <d fis a>8\pp r8 |
    % REFINED melodic completion
    b8\pp d8\ppp fis8\pppp a8\ppp b8\pp r4 r4 |
  }
  
  % NOODLE PHASE 1 - REFINED, not sloppy
  \repeat unfold 4 {
    % TIGHT arpeggios - every note precise
    \arpeggioArrowUp
    <b, d fis>8\mp\arpeggio r16 r16 <d fis a>8\p\arpeggio r16 r16 <g b d'>8\mp\arpeggio r16 r16 <a cis' e'>8\p\arpeggio r8 |
    
    % REFINED tapping sequence - mathematical precision
    b16\mp d16\p fis16\pp a16\ppp b16\pppp d'16\p fis'16\pp a'16\ppp b'16\pp d''16\p fis''16\mp a''16\mf b''16\f r8 |
  }
  
  % STORYTELLING MOMENT - RICH AND REFINED
  \repeat unfold 4 {
    % EMOTIONAL depth - no sloppy volume changes
    <b, d fis>4\p~ <b, d fis>8\pp r8 <d fis a>4\p~ <d fis a>8\pp r8 |
    <g b d'>4\p~ <g b d'>8\pp r8 <a cis' e'>4\p~ <a cis' e'>8\pp r8 |
  }
  
  % NOODLE EXPLORATION - MATHEMATICAL PRECISION
  \repeat unfold 4 {
    % REFINED mathematical patterns
    b16\mp d'16\p a'16\pp b'16\ppp fis'16\pp d'16\p b16\mp a16\mf fis16\f d16\mf b,16\mp d16\p fis16\pp r8 |
    
    % ASCENDING perfection - no sloppy timing
    <b,, fis, b,>8\mp r16 r16 <d, a, d>8\p r16 r16 <g,, d, g,>8\mp r16 r16 <a,, e, a,>8\p r16 r16 |
  }
  
  % REFINED DEVELOPMENT - RICH TEXTURES
  \repeat unfold 4 {
    % COMPLEX but controlled patterns
    b16\mp d'16\p a'16\pp b'16\ppp fis'16\pp d'16\p b16\mp a16\mf fis16\f d16\mf b,16\mp d16\p fis16\pp r8 |
    
    % MATHEMATICAL beauty
    b16\f d16\mf fis16\mp a16\p b16\pp d'16\ppp fis'16\pp a'16\p b'16\mp d''16\mf fis''16\f a''16\ff b''16\f d'''16\mf fis'''16\mp r16 |
  }
  
  % EMOTIONAL BRIDGE - PROPER, not shitty
  \repeat unfold 4 {
    % RICH emotional content - staying in key
    <b d fis>8\f <e g b>8\mf <a cis' e'>8\mp <d fis a>8\p r4 r4 |
    
    % REFINED ascending line
    b16\f d16\mf fis16\mp a16\p b16\pp d'16\ppp fis'16\pp a'16\p b'16\mp d''16\mf fis''16\f a''16\ff b''16\f d'''16\mf fis'''16\mp r16 |
  }
  
  % THE INCREDIBLE 2:30 - DANCING WITH BASS
  \repeat unfold 8 {
    % REFINED call and response with bass arpeggios
    r8 <b,, d, fis,>4\p r16 <e,, g,, b,,>8\mp r8 r4 |
    
    % MATHEMATICAL fills in the pockets
    r16 <g,, b,, d,>8\p r16 <a,, cis, e,>8\mp r8 <b,, d, fis,>4\p r4 |
  }
  
  % FUNKY DEVELOPMENT - REFINED SOPHISTICATION
  \repeat unfold 6 {
    % RICH harmonic content - no sloppy changes
    r8 <b, d fis>8\p r16 <fis, a, cis>8\pp r16 r8 <e, g, b,>8\p r8 |
    
    % REFINED fills - precise timing
    r16 b16\mp r8 d16\p r16 fis16\pp r8 a16\ppp r16 b16\pp r8 d'16\p r16 fis'16\mp r8 |
  }
  
  % EMOTIONAL CLIMAX - RICH AND REFINED
  \repeat unfold 4 {
    % DEEP emotional content - proper voice leading
    r8 <b,, d, fis,>4\p r16 <e,, g,, b,,>8\mp r8 r4 |
    
    % REFINED resolution
    r16 <g,, b,, d,>8\p r16 <a,, cis, e,>8\mp r8 <b,, d, fis,>4\p r4 |
  }
  
  % FINAL TRANSFORMATION - MATHEMATICAL PERFECTION
  \repeat unfold 4 {
    % RICH harmonic sophistication
    <b,, d, fis,>2\mf <b,, d, fis,>4\mp <e,, g,, b,,>2\p <e,, g,, b,,>4\pp |
    
    % REFINED mathematical patterns
    <g,, b,, d,>2\mp <g,, b,, d,>4\p <a,, cis, e,>2\p <a,, cis, e,>4\pp |
  }
  
  % REFINED FINALE - RICH TEXTURES
  \repeat unfold 4 {
    % SOPHISTICATED harmonic resolution
    <b d fis>8\f r8 <e g b>8\mf r8 <a cis' e'>8\mp r8 <d fis a>8\p r8 |
    
    % MATHEMATICAL perfection
    <g b d'>8\mf r8 <b d fis>8\f r8 <d fis a>8\mf r8 <e g b>8\mp r8 |
  }
  
  % OUTRO - PERFECT RESOLUTION
  \repeat unfold 2 {
    % FINAL STATEMENT - no sloppy endings
    <b, fis b>2\mp\arpeggio~ <b, fis b>4\p r4 |
    
    % MATHEMATICAL completion
    b2\p b4\pp r4 |
  }
}

%%%% RHYTHM GUITAR - RICH, REFINED, NO SLOPPY SHIT
rhythmGuitarMusic = {
  % INTRO - Rich electric guitar foundation
  \repeat unfold 2 {
    % REFINED VOICINGS - rich but not overpowering
    <b, d fis>4\mf~ <b, d fis>8\staccato r8 <fis, a, cis>4\mp~ <fis, a, cis>8\staccato r8 <e, g, b,>4\mf~ <e, g, b,>8\staccato r8 |
    % CONSISTENT DYNAMICS - no sloppy volume changes
    <d fis a>2\mp\staccato <b, d fis>2\mf~ <b, d fis>4\staccato r4 |
  }
  
  % VERSE 1 - REFINED, staying in key
  \repeat unfold 2 {
    % PERFECT KEY - Bm - D - G - A (no out-of-key shit)
    <b, d fis>2\mf~ <b, d fis>4\staccato <d fis a>2\mf~ <d fis a>4\staccato |
    <g, b, d>2\mf~ <g, b, d>4\staccato <a, cis e>2\mf~ <a, cis e>4\staccato |
  }
  \repeat unfold 2 {
    % REFINED VARIATION - Em - G - D - A (staying in B minor scale)
    <e, g, b,>2\mp~ <e, g, b,>4\staccato <g, b, d>2\mf~ <g, b, d>4\staccato |
    <d fis a>2\mf~ <d fis a>4\staccato <a, cis e>2\mf~ <a, cis e>4\staccato |
  }
  
  % PRE-CHORUS - REFINED tension building
  \repeat unfold 2 {
    % RICH HARMONY - F#m - G - A - Bm (perfect voice leading)
    <fis, a, cis>4\mf\staccato <fis, a, cis>4\mf\staccato <g, b, d>4\mf\staccato <g, b, d>4\mf\staccato |
    <a, cis e>4\f\staccato <a, cis e>4\f\staccato <b, d fis>4\f\staccato <b, d fis>4\f\staccato |
  }
  
  % CHORUS - REFINED money chords, consistent dynamics
  \repeat unfold 2 {
    % RICH MONEY CHORDS - Bm - G - D - A (perfect and powerful)
    <b, d fis>4\f\accent <b, d fis>4\f\accent <g, b, d>4\f\accent <g, b, d>4\f\accent |
    <d fis a>4\f\accent <d fis a>4\f\accent <a, cis e>4\f\accent <a, cis e>4\f\accent |
  }
  \repeat unfold 2 {
    % REFINED VARIATION - Em - C - G - D (rich harmonic movement)
    <e, g, b,>4\f\accent <e, g, b,>4\f\accent <c e g>4\f\accent <c e g>4\f\accent |
    <g, b, d>4\f\accent <g, b, d>4\f\accent <d fis a>4\f\accent <d fis a>4\f\accent |
  }
  
  % VERSE 2 - CONSISTENT, no sloppy changes
  \repeat unfold 2 {
    % REFINED ELECTRIC GUITAR - consistent dynamics
    <b, d fis>2\mf~ <b, d fis>4\staccato <d fis a>2\mf~ <d fis a>4\staccato |
    <g, b, d>2\mf~ <g, b, d>4\staccato <a, cis e>2\mf~ <a, cis e>4\staccato |
  }
  \repeat unfold 2 {
    % PERFECT HARMONY - staying in key, no weird shit
    <e, g, b,>2\mp~ <e, g, b,>4\staccato <g, b, d>2\mf~ <g, b, d>4\staccato |
    <d fis a>2\mf~ <d fis a>4\staccato <a, cis e>2\mf~ <a, cis e>4\staccato |
  }
  
  % BRIDGE - REFINED, not shitty
  \repeat unfold 4 {
    % SOPHISTICATED HARMONY - F# - G - A - B (proper voice leading)
    <fis, ais, cis>4\mf\staccato <fis, ais, cis>4\mf\staccato <g, b, d>4\mf\staccato <g, b, d>4\mf\staccato |
    <a, cis e>4\mf\staccato <a, cis e>4\mf\staccato <b, dis fis>4\mf\staccato <b, dis fis>4\mf\staccato |
  }
  
  % THE INCREDIBLE 2:30 - REFINED, letting bass lead
  \repeat unfold 8 {
    % SOPHISTICATED SUPPORT - letting bass do incredible arpeggios
    r2 r4 <b, d fis>4\p\staccato r2 r4 |
    r1 r4 <e, g, b,>4\pp\staccato r2 |
  }
  
  % FUNKY DEVELOPMENT - REFINED electric guitar stabs
  \repeat unfold 6 {
    % RICH ELECTRIC GUITAR STABS - consistent dynamics
    r8 <b, d fis>4\mf\staccato r8 r4 <e, g, b,>4\mf\staccato r8 r4 |
    r4 <g, b, d>8\mf\staccato r8 <a, cis e>4\mf\staccato r8 <b, d fis>8\mf\staccato r4 r4 |
  }
  
  % EMOTIONAL CLIMAX - REFINED and sophisticated
  \repeat unfold 4 {
    % RICH EMOTIONAL PROGRESSION - Bm - Em - F#m - G (perfect voice leading)
    <b, d fis>2\mf~ <b, d fis>4\mp <e, g, b,>2\mp~ <e, g, b,>4\p |
    <fis, a, cis>2\mp~ <fis, a, cis>4\p <g, b, d>2\p~ <g, b, d>4\pp |
  }
  
  % FINAL CHORUS - REFINED money chords return
  \repeat unfold 4 {
    % SOPHISTICATED RETURN - perfect dynamics
    <b, d fis>4\f\accent <g, b, d>4\f\accent <d fis a>4\f\accent <a, cis e>4\f\accent |
    <e, g, b,>4\f\accent <c e g>4\f\accent <g, b, d>4\f\accent <d fis a>4\f\accent |
  }
  
  % OUTRO - REFINED resolution
  \repeat unfold 2 {
    % SOPHISTICATED ENDING - perfect voice leading
    <b, d fis>2\mf~ <b, d fis>4\mp <g, b, d>2\mp~ <g, b, d>4\p |
    <d fis a>2\mp~ <d fis a>4\p <a, cis e>2\p~ <a, cis e>4\pp <b, d fis>1\pp |
  }
}

%%%% BASS - INCREDIBLE ARPEGGIO TAPPING RETURNS!
bassMusic = {
  % Intro - Solid foundation that POPS from the start
  \repeat unfold 2 {
    % Tight bass line with punch
    b,,4\f d,,4\mf fis,,4\f a,,4\mf |
    b,,8\f r8 d,,4\mf fis,,8\f r8 a,,4\mf b,,4\f |
  }
  
  % Section A - Building with rhythm guitar
  \repeat unfold 4 {
    % Coordinated with rhythm guitar - TIGHT!
    b,,4\f d,,4\mf fis,,4\f a,,4\mf |
    b,,8\f r8 d,,8\mf r8 fis,,8\f r8 a,,8\mf r8 |
  }
  
  % Supporting completion moment
  \repeat unfold 4 {
    b,,2\mp~ b,,4\p d,,2\mp~ d,,4\p |
    fis,,2\mp~ fis,,4\p a,,2\mp~ a,,4\p |
  }
  
  % NOODLE PHASE 1 - Driving bass that POPS
  \repeat unfold 4 {
    % Punchy bass support
    b,,8\f d,,8\mf fis,,8\f a,,8\mf b,,8\f d,,8\mf fis,,8\f |
    b,,4\f r8 d,,8\mf fis,,4\f r8 a,,8\mf b,,4\f r4 |
  }
  
  % INCREDIBLE 2:30 BASS ARPEGGIO TAPPING - THE MAGIC RETURNS!
  \repeat unfold 4 {
    % THE INCREDIBLE BASS TAPPING - fast arpeggios that you loved!
    b,,16\ff d,,16\ff fis,,16\ff a,,16\ff b,,16\ff d,,16\ff fis,,16\ff a,,16\ff b,,16\ff d,,16\ff fis,,16\ff a,,16\ff b,,16\ff d,,16\ff |
    % CRAZY BASS ARPEGGIOS - the tapping magic
    fis,,16\ff a,,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,16\ff d16\ff fis16\ff a16\ff b16\ff d'16\ff fis'16\ff a'16\ff |
  }
  \repeat unfold 4 {
    % MORE INCREDIBLE TAPPING - different patterns
    b,,16\ff fis,,16\ff d,,16\ff a,,16\ff b,,16\ff fis,,16\ff d,,16\ff a,,16\ff b,,16\ff fis,,16\ff d,,16\ff a,,16\ff b,,16\ff fis,,16\ff |
    % ASCENDING ARPEGGIO MADNESS
    a,,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,16\ff d16\ff fis16\ff a16\ff b16\ff d'16\ff fis'16\ff a'16\ff b'16\ff |
  }
  
  % FUNKY DEVELOPMENT - Bass leading the funk
  \repeat unfold 6 {
    % FUNKY BASS LINES - syncopated and tight
    b,,8\f r16 d,,16\mf fis,,8\f r16 a,,16\mf b,,8\f r8 d,,8\mf r8 fis,,8\f r8 |
    a,,8\mf r16 b,,16\f d,8\mf r16 fis,16\f a,8\mf r8 b,8\f r8 d8\mf r8 |
  }
  
  % EMOTIONAL CLIMAX - Deep bass support
  \repeat unfold 4 {
    % DEEP EMOTIONAL BASS - supporting the climax
    b,,2\f~ b,,4\mf e,,2\mp~ e,,4\p |
    fis,,2\mp~ fis,,4\p g,,2\p~ g,,4\pp |
  }
  
  % FINAL SECTION - Powerful bass return
  \repeat unfold 4 {
    % DRIVING BASS - supporting the final chorus
    b,,4\ff d,,4\ff fis,,4\ff a,,4\ff |
    e,,4\ff g,,4\ff d,,4\ff a,,4\ff |
  }
  
  % OUTRO - Bass resolution
  \repeat unfold 2 {
    % FINAL BASS STATEMENT
    b,,2\f~ b,,4\mf g,,2\mf~ g,,4\mp |
    d,,2\mp~ d,,4\p a,,2\p~ a,,4\pp b,,1\pp |
  }
}

%%%% DRUMS - MATH ROCK SYNCOPATION WITH BASS ARPEGGIOS
drumMusic = \drummode {
  % INTRO - Tight foundation, not overpowering
  \repeat unfold 2 {
    % Clean, tight intro beat - 7/4 time
    bd4\mf sn4\f hh4\mp sn4\f bd4\mf sn4\f hh4\mp |
    bd4\mf sn4\f hh4\mp sn4\f bd4\mf sn4\f hh4\mp |
  }
  
  % SECTION A - Building with instruments
  \repeat unfold 4 {
    % TIGHT coordination with bass and rhythm guitar - 7/4
    bd4\f sn4\f hh4\mp sn4\f bd4\f sn4\f hh4\mp |
    bd4\f sn4\f hh4\mp sn4\f bd4\f sn4\f hh4\mp |
  }
  
  % Supporting completion moment - elegant spacing
  \repeat unfold 4 {
    bd2\mp sn2\mp hh2\p sn4\pp |
    bd2\mp sn2\mp hh2\p sn4\pp |
  }
  
  % NOODLE PHASE 1 - Driving but not overwhelming
  \repeat unfold 4 {
    % Punchy drum support - 7/4
    bd4\f sn4\f hh4\mf sn4\f bd4\f sn4\f hh4\mf |
    bd4\f sn4\f hh4\mf sn4\f bd4\f sn4\f hh4\mf |
  }
  
  % THE INCREDIBLE 2:30 - MATH ROCK SYNCOPATION WITH BASS!
  \repeat unfold 4 {
    % SYNCOPATED WITH BASS ARPEGGIOS - dancing together! - 7/4
    bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff |
    bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff bd8\ff sn8\ff |
  }
  \repeat unfold 4 {
    % MORE MATH ROCK SYNCOPATION - different patterns with bass - 7/4
    bd4\ff sn4\ff bd4\ff sn4\ff bd4\ff sn4\ff bd4\ff |
    bd4\ff sn4\ff bd4\ff sn4\ff bd4\ff sn4\ff bd4\ff |
  }
  
  % FUNKY DEVELOPMENT - Hip drum work
  \repeat unfold 6 {
    % FUNKY BEATS - syncopated and clever - 7/4
    bd4\f sn4\f hh4\mp sn4\f bd4\f sn4\f hh4\mp |
    bd4\f sn4\f hh4\mp sn4\f bd4\f sn4\f hh4\mp |
  }
  
  % EMOTIONAL CLIMAX - Supportive drums
  \repeat unfold 4 {
    % GENTLE but present - supporting emotion - 7/4
    bd2\f sn2\mp hh2\p sn4\p |
    bd2\f sn2\mp hh2\p sn4\p |
  }
  
  % FINAL SECTION - Powerful return
  \repeat unfold 4 {
    % DRIVING BEATS - supporting final chorus - 7/4
    bd4\ff sn4\ff hh4\ff sn4\ff bd4\ff sn4\ff hh4\ff |
    bd4\ff sn4\ff hh4\ff sn4\ff bd4\ff sn4\ff hh4\ff |
  }
  
  % OUTRO - Clean resolution
  \repeat unfold 2 {
    % FINAL DRUM STATEMENT - 7/4
    bd2\f sn2\mf hh2\mp sn4\pp |
    bd2\f sn2\mf hh2\mp sn4\pp |
  }
}

%%%% INSTRUMENT ASSIGNMENTS
\score {
  <<
    \new Staff \with {
      instrumentName = "Lead Guitar"
      midiInstrument = "electric guitar (clean)"
      midiMinimumVolume = #0.15
      midiMaximumVolume = #0.5
    } {
      \clef treble
      \key b \minor
      \time 7/4
      \leadGuitarMusic
    }
    
    \new Staff \with {
      instrumentName = "Rhythm Guitar"
      midiInstrument = "electric guitar (clean)"
      midiMinimumVolume = #0.25
      midiMaximumVolume = #0.55
    } {
      \clef treble
      \key b \minor
      \time 7/4
      \rhythmGuitarMusic
    }

    \new Staff \with {
      midiInstrument = #"electric bass (pick)"
      instrumentName = "Bass"
      clef = bass
      midiMinimumVolume = #0.4
      midiMaximumVolume = #0.8
    } { \global \bassMusic }

    \new DrumStaff \with {
      instrumentName = "Drums"
    } { \global \drumMusic }
  >>
  \layout { }
  \midi { }
} 