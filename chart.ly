\version "2.24.0"

\header {
  title = "I. love. lemon."
  composer = "Vienna Lager Vibes"
  subtitle = "MASTERPIECE MATH ROCK PERFECTION"
}

%%%% Global settings
global = {
  \tempo 4 = 120
  \time 7/4
  \key b \minor
}

%%%% LEAD GUITAR - RICH SUGARY ELECTRIC GUITAR MAGIC
leadGuitarMusic = {
  % INTRO - Rich sugary electric guitar beauty
  \repeat unfold 2 {
    % LUSH OPENING - rich chord extensions with guitar feel
    \arpeggioArrowUp
    <b, d fis a>4\mp\arpeggio r8 <fis, a, cis e>8\p\arpeggio r4 r8 |
    \arpeggioArrowDown
    <e, g, b, d>4\p\arpeggio r8 <a,, cis, e, g>8\pp\arpeggio r4 r8 |
    
    % SUGARY MELODIC STATEMENT - guitar-like phrasing
    b8\mp~ b16 d16\p~ d8 fis8\pp~ fis16 a16\ppp~ a8 r8 r8 |
  }
  
  % DEVELOPMENT 1 - Rich guitar textures
  \repeat unfold 4 {
    % RICH B minor extensions - sugary guitar voicings
    \arpeggioArrowUp
    <b, d fis a>4\mp\arpeggio r16 <d fis a cis'>8.\p\arpeggio r8 <g b d' fis'>4\mp\arpeggio r16 |
    <a cis' e' g'>4\p\arpeggio r16 <fis a cis' e'>8.\pp\arpeggio r8 <e g b d'>4\p\arpeggio r16 |
    
    % GUITAR TAPPING - rich electric guitar feel
    b16\mf~ b16 d16\mp~ d16 fis16\mf~ fis16 a16\mp~ a16 r16 r16 r16 r16 r8. |
  }
  
  % BRIDGE - Rich harmonic progressions
  \repeat unfold 4 {
    % RICH CHORD WORK - sugary guitar extensions
    <b, e a d'>4\p~ <b, e a d'>8\pp r8 <fis b e' a'>4\p~ <fis b e' a'>8\pp r8 |
    <g c' f' b'>4\pp~ <g c' f' b'>8\ppp r8 <a d' g' c''>4\pp~ <a d' g' c''>8\ppp r8 |
    
    % SUGARY MELODIC DEVELOPMENT - guitar phrasing
    b8\pp~ b16 d16\ppp~ d8 fis8\pppp~ fis16 a16\ppp~ a8 r8 r8 |
  }
  
  % NOODLE PHASE 1 - RICH GUITAR PATTERNS (1:05+)
  \repeat unfold 4 {
    % RICH MATHEMATICAL PATTERNS - sugary guitar feel
    \arpeggioArrowUp
    <b, d fis a>8\mp\arpeggio r16 <e g b d'>16\p\arpeggio r8 <a cis' e' g'>8\mp\arpeggio r16 <d fis a cis'>16\p\arpeggio r4 |
    
    % GUITAR SYNCOPATED PATTERNS - rich electric feel
    b16\mp~ b16 r16 d16\p~ d16 r16 fis16\pp~ fis16 r16 a16\ppp~ a16 r16 r8 |
  }
  
  % FIXED 0:45 SECTION - STAYING IN B MINOR MODAL TERRITORY!
  \repeat unfold 4 {
    % PROPER B MINOR MODAL MOVEMENT - NO FUCKING MAJOR DIRECTION!
    <b, d fis>4\p~ <b, d fis>8\pp <a, cis e>8\p~ <a, cis e>4\pp <g, b, d>8\p r8 |
    <fis, a, cis>4\p~ <fis, a, cis>8\pp <e, g, b,>8\p~ <e, g, b,>4\pp <d, fis, a,>8\p r8 |
  }
  
  % MATHEMATICAL EXPLORATION - B minor modal richness
  \repeat unfold 4 {
    % RICH MATHEMATICAL SEQUENCES - staying in B minor
    b16\mp d'16\p a'16\pp cis''16\ppp fis''16\pp b''16\p e'''16\mp a'''16\mf r16 r16 r16 r16 r8. |
    
    % RICH CHORD PROGRESSIONS - B minor modal
    <b,, e,, a,, d,>8\mp r16 <a,, d,, g,, c,>16\p r8 <g,, c,, f,, b,,>8\mp r16 <fis,, b,, e,, a,,>16\p r4 |
  }
  
  % SOPHISTICATED DEVELOPMENT - Rich guitar textures
  \repeat unfold 4 {
    % RICH COMPLEX PATTERNS - sugary guitar feel
    b16\mp d'16\p a'16\pp cis''16\ppp fis''16\pp b''16\p e'''16\mp a'''16\mf d''''16\f r16 r16 r16 r8 |
    
    % RICH HARMONIC RHYTHM - guitar extensions
    <b, e a d'>16\f <a, d g c'>16\mf <g, c f b>16\mp <fis, b e a>16\p r16 r16 r8 r4 |
  }
  
  % EMOTIONAL BRIDGE - Rich sugary guitar content
  \repeat unfold 4 {
    % RICH EMOTIONAL PROGRESSIONS - sugary guitar voicings
    <b d fis a cis'>8\f <e g b d' fis'>8\mf <a cis' e' g' b'>8\mp <d fis a cis' e'>8\p r8 r4 r8 |
    
    % SUGARY ASCENDING PATTERNS - guitar feel
    b16\f~ b16 d16\mf~ d16 fis16\mp~ fis16 a16\p~ a16 r16 r16 r16 r16 r16 r16 r16 r16 |
  }
  
  % THE INCREDIBLE 2:30 - BUILDING WITH BASS PERFECTION
  \repeat unfold 2 {
    % STARTING SPARSE - letting bass lead
    r8 <b,, d, fis, a,>4\p r16 <e,, g,, b,, d,>8\mp r8 r4 r8 |
    r16 <g,, b,, d, fis,>8\p r16 r8 r8 <b,, d, fis, a,>4\p r4 r4 |
  }
  \repeat unfold 2 {
    % BUILDING INTENSITY - rich harmonic support
    r8 <b,, d, fis, a,>4\p r16 <e,, g,, b,, d,>8\mp r8 <c,, e,, g,, b,,>4\p r8 |
    r16 <g,, b,, d, fis,>8\p r16 <a,, cis, e, g,>8\mp r8 <b,, d, fis, a,>4\p <c, e, g, b,>4\pp |
  }
  \repeat unfold 2 {
    % RISING INTENSITY - richer harmonies
    <b,, d, fis, a,>8\mp r8 <e,, g,, b,, d,>4\mp r16 <c,, e,, g,, b,,>8\p r8 <f,, a,, c, e,>4\mp |
    <g,, b,, d, fis,>8\mp r16 <a,, cis, e, g,>16\mp r8 <b,, d, fis, a,>4\mp <c, e, g, b,>4\p <d, fis, a, c>4\p |
  }
  \repeat unfold 2 {
    % CLIMAX - full harmonic richness
    <b,, d, fis, a,>8\mf <e,, g,, b,, d,>8\mf <c,, e,, g,, b,,>8\mp <f,, a,, c, e,>8\mp <g,, b,, d, fis,>8\p r8 r8 |
    <a,, cis, e, g,>8\mf <b,, d, fis, a,>8\mf <c, e, g, b,>8\mp <d, fis, a, c>8\mp <e, g, b, d>8\p r4 r8 |
  }
  
  % FUNKY DEVELOPMENT - Rich guitar content
  \repeat unfold 6 {
    % RICH HARMONIC CONTENT - sugary guitar extensions
    r8 <b, d fis a cis'>8\p r16 <fis, a, cis e g>8\pp r16 r8 <e, g, b, d fis>8\p r8 |
    
    % SUGARY RHYTHMIC FILLS - guitar feel
    r16 b16\mp~ b16 r8 d16\p~ d16 r16 fis16\pp~ fis16 r8 a16\ppp~ a16 r16 r16 r8 |
  }
  
  % EMOTIONAL CLIMAX - Rich sugary guitar content
  \repeat unfold 4 {
    % RICH EMOTIONAL DEPTH - sugary guitar voicings
    r8 <b,, d, fis, a, cis>4\p r16 <e,, g,, b,, d, fis>8\mp r8 <c,, e,, g,, b,, d>4\p r8 |
    
    % RICH RESOLUTION PATTERNS - guitar extensions
    r16 <g,, b,, d, fis, a>8\p r16 <a,, cis, e, g, b>8\mp r8 <b,, d, fis, a, cis>4\p <c, e, g, b, d'>4\pp |
  }
  
  % FINAL TRANSFORMATION - Rich guitar perfection
  \repeat unfold 4 {
    % RICH HARMONIC PROGRESSIONS - sugary guitar extensions
    <b,, d, fis, a, cis>2\mf <b,, d, fis, a, cis>4\mp <e,, g,, b,, d, fis>2\p <e,, g,, b,, d, fis>4\pp |
    
    % RICH MATHEMATICAL PATTERNS - guitar voicings
    <g,, b,, d, fis, a>2\mp <g,, b,, d, fis, a>4\p <a,, cis, e, g, b>2\p <a,, cis, e, g, b>4\pp |
  }
  
  % FINALE - Rich sugary resolution
  \repeat unfold 4 {
    % RICH HARMONIC RESOLUTION - sugary guitar voicings
    <b d fis a cis'>8\f r8 <e g b d' fis'>8\mf r8 <a cis' e' g' b'>8\mp r8 <d fis a cis' e'>8\p r8 |
    
    % GUITAR PERFECTION - rich extensions
    <g b d' fis' a'>8\mf r8 <b d fis a cis'>8\f r8 <d fis a cis' e'>8\mf r8 <e g b d' fis'>8\mp r8 |
  }
  
  % OUTRO - Rich sugary resolution
  \repeat unfold 2 {
    % FINAL RICH STATEMENT - sugary guitar voicings
    <b, fis b d' a'>2\mp\arpeggio~ <b, fis b d' a'>4\p <c g c' e' b'>4\pp |
    
    % GUITAR COMPLETION - rich resolution
    b2\p~ b8 cis'4\pp~ cis'8 d'4\ppp~ d'8 e'2\pppp r4 |
  }
}

%%%% RHYTHM GUITAR - TIGHT MATHEMATICAL PRECISION (FIXED!)
rhythmGuitarMusic = {
  % INTRO - TIGHT B MINOR MATH ROCK PRECISION
  \repeat unfold 2 {
    % TIGHT CHORD ATTACKS - sharp mathematical timing, ONLY B minor chords
    <b, d fis>8\mf r16 <b, d fis>16\mf r8 <fis, a, cis>8\mp r16 <fis, a, cis>16\mp r8 <e, g, b,>8\mf r16 <e, g, b,>16\mf |
    % MATHEMATICAL PRECISION - locked timing, staying in B minor scale
    <d, fis, a,>8\mp r16 <d, fis, a,>16\mp r8 <b,, d, fis,>8\mf r16 <b,, d, fis,>16\mf r8 <a,, cis, e,>8\mp r16 <a,, cis, e,>16\mp |
  }
  
  % VERSE 1 - TIGHT B MINOR MODAL PROGRESSIONS
  \repeat unfold 4 {
    % LOCKED B MINOR PROGRESSIONS - Bm - F#m - Em - D
    <b, d fis>8\mf r16 <b, d fis>16\mf r8 <fis, a, cis>8\mf r16 <fis, a, cis>16\mf r8 <e, g, b,>8\mf r16 <e, g, b,>16\mf |
    <d, fis, a,>8\mf r16 <d, fis, a,>16\mf r8 <b,, d, fis,>8\mf r16 <b,, d, fis,>16\mf r8 <a,, cis, e,>8\mf r16 <a,, cis, e,>16\mf |
  }
  
  % PRE-CHORUS - TIGHT MATHEMATICAL SYNCOPATION (B MINOR ONLY!)
  \repeat unfold 4 {
    % SHARP SYNCOPATED ATTACKS - mathematical precision, B minor scale only
    <b, d fis>16\f <b, d fis>16\f r8 <g, b, d>16\f <g, b, d>16\f r8 <d, fis, a,>16\f <d, fis, a,>16\f r8 <a,, cis, e,>16\f <a,, cis, e,>16\f |
    <e, g, b,>16\f <e, g, b,>16\f r8 <b,, d, fis,>16\f <b,, d, fis,>16\f r8 <fis,, a,, cis,>16\f <fis,, a,, cis,>16\f r8 <g,, b,, d,>16\f <g,, b,, d,>16\f |
  }
  
  % CHORUS - SHARP MATHEMATICAL CHORD ATTACKS (B MINOR SCALE!)
  \repeat unfold 4 {
    % TIGHT CHORD PRECISION - locked with drums, B minor modal harmony
    <b, d fis>16\ff r16 <b, d fis>16\ff r16 <g, b, d>16\ff r16 <g, b, d>16\ff r16 <d, fis, a,>16\ff r16 <d, fis, a,>16\ff r16 <a,, cis, e,>16\ff r16 |
    <e, g, b,>16\ff r16 <e, g, b,>16\ff r16 <b,, d, fis,>16\ff r16 <b,, d, fis,>16\ff r16 <fis,, a,, cis,>16\ff r16 <fis,, a,, cis,>16\ff r16 <g,, b,, d,>16\ff r16 |
  }
  
  % VERSE 2 - MATHEMATICAL DEVELOPMENT (B MINOR ONLY!)
  \repeat unfold 4 {
    % TIGHT MATHEMATICAL PATTERNS - sharp timing, B minor scale
    <b, d fis>8\mf r16 <fis, a, cis>16\mf r8 <e, g, b,>8\mf r16 <d, fis, a,>16\mf r8 <b,, d, fis,>8\mf r16 <a,, cis, e,>16\mf |
    <g,, b,, d,>8\mf r16 <fis,, a,, cis,>16\mf r8 <e,, g,, b,,>8\mf r16 <d,, fis,, a,,>16\mf r8 <b,,, d,, fis,,>8\mf r16 <a,,, cis,, e,,>16\mf |
  }
  
  % BRIDGE - TIGHT QUARTAL HARMONY (B MINOR SCALE!)
  \repeat unfold 4 {
    % MATHEMATICAL QUARTAL VOICINGS - B minor scale quartal harmony
    <fis, b, e>16\mf <fis, b, e>16\mf r8 <g, c fis>16\mf <g, c fis>16\mf r8 <a, d g>16\mf <a, d g>16\mf r8 <b, e a>16\mf <b, e a>16\mf |
    <cis fis b>16\mf <cis fis b>16\mf r8 <d g cis'>16\mf <d g cis'>16\mf r8 <e a d'>16\mf <e a d'>16\mf r8 <fis b e'>16\mf <fis b e'>16\mf |
  }
  
  % THE INCREDIBLE 2:30 - SPARSE MATHEMATICAL SUPPORT
  \repeat unfold 8 {
    % MATHEMATICAL SPACING - letting bass lead, tight when present
    r4 r8 <b, d fis>16\p <b, d fis>16\p r4 r8 <e, g, b,>16\pp <e, g, b,>16\pp |
    r2 r8 <d, fis, a,>16\pp <d, fis, a,>16\pp r4 r8 <a,, cis, e,>16\ppp <a,, cis, e,>16\ppp |
  }
  
  % FUNKY DEVELOPMENT - TIGHT MATHEMATICAL STABS
  \repeat unfold 6 {
    % SHARP MATHEMATICAL STABS - locked timing, B minor scale
    r16 <b, d fis>16\f r16 <b, d fis>16\f r8 <fis, a, cis>16\f <fis, a, cis>16\f r8 <e, g, b,>16\f <e, g, b,>16\f r8 |
    r8 <d, fis, a,>16\f <d, fis, a,>16\f r8 <g,, b,, d,>16\f <g,, b,, d,>16\f r8 <a,, cis, e,>16\f <a,, cis, e,>16\f r16 <b,, d, fis,>16\f |
  }
  
  % EMOTIONAL CLIMAX - MATHEMATICAL PRECISION
  \repeat unfold 4 {
    % TIGHT EMOTIONAL PROGRESSION - B minor modal movement
    <b, d fis>8\mf r16 <b, d fis>16\mf r8 <e, g, b,>8\mp r16 <e, g, b,>16\mp r8 <fis, a, cis>8\mp r16 <fis, a, cis>16\mp |
    <g, b, d>8\mp r16 <g, b, d>16\mp r8 <a, cis e>8\p r16 <a, cis e>16\p r8 <b, d fis>8\p r16 <b, d fis>16\p |
  }
  
  % FINAL CHORUS - SHARP MATHEMATICAL RETURN
  \repeat unfold 4 {
    % TIGHT MATHEMATICAL PRECISION - locked with drums, B minor scale
    <b, d fis>16\ff r16 <g, b, d>16\ff r16 <d, fis, a,>16\ff r16 <a,, cis, e,>16\ff r16 <e, g, b,>16\ff r16 <b,, d, fis,>16\ff r16 <fis,, a,, cis,>16\ff r16 |
    <g,, b,, d,>16\ff r16 <d,, fis,, a,,>16\ff r16 <a,,, cis,, e,,>16\ff r16 <e,, g,, b,,>16\ff r16 <b,,, d,, fis,,>16\ff r16 <fis,,, a,,, cis,,>16\ff r16 <b,,, d,, fis,,>16\ff r16 |
  }
  
  % OUTRO - MATHEMATICAL RESOLUTION
  \repeat unfold 2 {
    % FINAL MATHEMATICAL STATEMENT - B minor resolution
    <b, d fis>8\mf r16 <b, d fis>16\mf r8 <g, b, d>8\mp r16 <g, b, d>16\mp r8 <d, fis, a,>8\mp r16 <d, fis, a,>16\mp |
    <a,, cis, e,>8\mp r16 <a,, cis, e,>16\mp r8 <b,, d, fis,>8\p r16 <b,, d, fis,>16\p r8 <b,, d, fis,>2\pp |
  }
}

%%%% BASS - BASSY YUMMY ARPEGGIOS (FIXED TO STAY LOW!)
bassMusic = {
  % Intro - Rich bass foundation
  \repeat unfold 2 {
    % BASSY FOUNDATION - staying in low register
    b,,4\f d,8\mf r8 fis,4\f a,8\mf r8 b,,4\f |
    b,,8\f r16 d,16\mf fis,8\f r16 a,16\mf b,,8\f r8 d,4\mf fis,8\f r8 a,4\mf |
  }
  
  % Section A - Building with bassy patterns
  \repeat unfold 4 {
    % BASSY PATTERNS - staying low and growling
    b,,4\f d,8\mf r16 fis,16\f a,4\mf b,,8\f r16 d,16\mf |
    fis,8\f r16 a,16\mf b,,8\f r8 d,4\mf fis,8\f r16 a,16\mf b,,4\f |
  }
  
  % Supporting harmonic movement
  \repeat unfold 4 {
    % BASSY HARMONIC SUPPORT - deep and rich
    b,,2\mp~ b,,8\p r8 d,2\mp~ d,8\p r8 |
    fis,2\mp~ fis,8\p r8 a,2\mp~ a,8\p r8 b,,4\mp |
  }
  
  % NOODLE PHASE 1 - BASSY GROWLING ARPEGGIOS (1:12) - FIXED TO STAY LOW!
  \repeat unfold 4 {
    % BASSY GROWLING ARPEGGIOS - staying in lower register for maximum growl
    b,,8\f d,16\mf r16 fis,8\f a,16\mf r16 b,,8\f d,16\mf r16 fis,8\f |
    a,8\mf r16 b,,16\f d,8\mf r16 fis,16\f a,8\mf r16 b,,16\f d,8\mf r16 fis,16\f a,4\mf |
  }
  
  % THE INCREDIBLE 2:30 - BASSY ARPEGGIO TAPPING PERFECTION!
  \repeat unfold 4 {
    % INSANE BASSY ARPEGGIOS - staying in bass register for maximum impact
    b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff |
    % BASSY ARPEGGIO PATTERNS - keeping it low and growling
    b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff |
  }
  \repeat unfold 4 {
    % MORE BASSY TAPPING - different low patterns
    a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff a,16\ff b,,16\ff d,16\ff fis,16\ff |
    % BASSY DESCENDING PATTERNS - staying in bass range
    fis,16\ff d,16\ff b,,16\ff a,16\ff fis,16\ff d,16\ff b,,16\ff a,16\ff fis,16\ff d,16\ff b,,16\ff a,16\ff fis,16\ff d,16\ff b,,16\ff a,16\ff |
  }
  
  % FUNKY DEVELOPMENT - Bassy leadership
  \repeat unfold 6 {
    % BASSY FUNKY PATTERNS - staying low and groovy
    b,,8\f r16 d,16\mf fis,8\f r16 a,16\mf b,,8\f r16 d,16\mf fis,8\f r16 a,16\mf |
    b,,8\f r8 d,8\mf r16 fis,16\f a,8\mf r16 b,,16\f d,8\mf r16 fis,16\f a,8\mf r16 b,,16\f |
  }
  
  % EMOTIONAL CLIMAX - Deep bassy support
  \repeat unfold 4 {
    % BASSY EMOTIONAL SUPPORT - deep and rich
    b,,2\f~ b,,8\mf r8 e,2\mp~ e,8\p r8 |
    fis,2\mp~ fis,8\p r8 g,2\p~ g,8\pp r8 a,4\pp |
  }
  
  % FINAL SECTION - Powerful bassy return
  \repeat unfold 4 {
    % DRIVING BASSY PATTERNS - staying low and powerful
    b,,4\ff d,8\ff r16 fis,16\ff a,4\ff e,8\ff r16 g,16\ff |
    d,4\ff a,8\ff r16 b,,16\ff fis,4\ff c8\ff r16 g,16\ff d,4\ff |
  }
  
  % OUTRO - Bassy resolution
  \repeat unfold 2 {
    % FINAL BASSY STATEMENT
    b,,2\f~ b,,8\mf r8 g,2\mf~ g,8\mp r8 |
    d,2\mp~ d,8\p r8 a,2\p~ a,8\pp r8 b,,1\pp |
  }
}

%%%% DRUMS - SHARP RAD FUNKY MATH ROCK SYNCOPATION - ACTUALLY COMPLEX!
drumMusic = \drummode {
  % INTRO - Sharp mathematical foundation
  \repeat unfold 2 {
    % TIGHT INTRO BEAT - sharp 7/4 patterns with complexity
    bd16\mf sn16\f bd8\mf sn16\f r16 hh16\mp sn8\f bd16\mf r16 sn16\f hh8\mp sn4\f |
    bd16\mf r16 sn16\f hh16\mp r16 sn16\f bd8\mf sn16\f r16 hh16\mp sn8\f r16 bd16\mf sn4\f |
  }
  
  % SECTION A - Building sharp complex patterns
  \repeat unfold 4 {
    % SHARP MATHEMATICAL COORDINATION - complex 7/4 math rock
    bd16\f sn16\f bd8\f sn16\f r16 hh16\mf sn8\f bd16\f r16 sn16\f hh8\mf sn4\f |
    bd16\f r16 sn16\f hh16\mf r16 bd16\f sn8\f bd16\f r16 hh16\mf sn8\f r16 bd16\f sn4\f |
  }
  
  % Supporting development - mathematical spacing
  \repeat unfold 4 {
    % MATHEMATICAL ELEGANCE - complex but controlled
    bd8\mp sn16\mp r16 bd16\mp sn8\mp hh16\p r16 sn16\pp r16 bd16\pp sn8\pp r16 hh16\ppp |
    sn8\mp bd16\mp r16 sn16\mp bd8\mp hh16\p r16 bd16\pp r16 sn16\pp bd8\pp r16 hh16\ppp sn4\ppp |
  }
  
  % NOODLE PHASE 1 - INSANE SHARP RAD FUNKY MATH ROCK (1:05+) - ACTUALLY COMPLEX!
  \repeat unfold 4 {
    % INSANE SHARP FUNKY SYNCOPATION - REAL math rock complexity like Battles/Hella
    bd16\f sn16\f bd8\f sn16\f bd16\f sn8\f bd16\f sn16\f bd8\f sn16\f bd16\f sn16\f |
    hh16\mf bd16\f sn16\f hh16\mf bd16\f sn16\f hh16\mf bd16\f sn16\f hh16\mf bd16\f sn16\f hh16\mf bd8\f sn16\f |
  }
  
  % MORE INSANE MATH ROCK COMPLEXITY - different patterns
  \repeat unfold 4 {
    % COMPLEX SYNCOPATED PATTERNS - like Don Caballero/Shellac
    sn16\f bd16\f sn8\f bd16\f sn16\f bd8\f sn16\f bd16\f sn8\f bd16\f sn16\f bd16\f |
    hh8\mf sn16\f bd16\f hh8\mf bd16\f sn16\f hh8\mf sn16\f bd16\f hh8\mf bd16\f sn16\f hh16\mf |
  }
  
  % THE INCREDIBLE 2:30 - DRUMS BUILDING WITH PERFECT BASS!
  \repeat unfold 2 {
    % STARTING SPARSE - letting bass arpeggios lead but still complex
    bd8\mp r16 sn16\mp bd8\mp r16 sn16\mp bd8\mp sn16\mp r16 bd16\mp sn8\mp r8 |
    r8 hh16\p r16 bd16\p r16 sn16\pp r8 hh16\pp r16 sn8\pp r16 bd16\pp |
  }
  \repeat unfold 2 {
    % BUILDING INTENSITY - sharp rhythmic support with complexity
    bd16\mf sn16\mf bd8\mf sn16\mf bd16\mf sn8\mf bd16\mf sn16\mf bd8\mf sn16\mf hh8\mp bd16\mf |
    bd16\mf sn16\mf bd16\mf sn16\mf hh16\mp bd16\mf sn16\mf bd16\mf sn16\mf hh16\mp sn16\mf bd16\mf hh8\mp sn8\mf |
  }
  \repeat unfold 2 {
    % RISING INTENSITY - sharp complex syncopation matching bass
    bd16\f sn16\f bd16\f sn16\f hh16\f bd16\f sn16\f hh16\f bd16\f sn16\f hh16\f bd16\f sn16\f hh16\f bd8\mf |
    sn16\f bd16\f sn16\f bd16\f hh16\f sn16\f bd16\f hh16\f sn16\f bd16\f hh16\f sn16\f bd16\f hh16\f sn16\f bd8\mf |
  }
  \repeat unfold 2 {
    % CLIMAX - insane sharp syncopation matching bass complexity - REAL MATH ROCK!
    bd16\ff sn16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff |
    hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff bd16\ff sn16\ff hh16\ff |
  }
  
  % FUNKY DEVELOPMENT - INSANE SHARP RAD FUNKY BEATS
  \repeat unfold 6 {
    % INSANE FUNKY SYNCOPATION - sharp math rock complexity like Lightning Bolt
    bd16\f sn8\f bd16\f sn16\f bd8\f sn16\f bd16\f sn8\f bd16\f sn16\f bd16\f sn8\f |
    hh16\mf bd16\f sn16\f hh16\mf sn16\f bd16\f hh16\mf bd16\f sn16\f hh16\mf sn16\f bd16\f hh8\mf sn16\f bd16\f |
  }
  
  % EMOTIONAL CLIMAX - Sharp supportive drums with complexity
  \repeat unfold 4 {
    % SHARP EMOTIONAL SUPPORT - complex but tasteful
    bd8\f sn16\mp r16 bd16\f sn8\mp hh16\p r16 sn16\p r16 bd16\pp sn8\pp r16 hh16\ppp |
    sn8\f bd16\mp r16 sn16\f bd8\mp hh16\p r16 bd16\p r16 sn16\pp bd8\pp r16 hh16\ppp sn4\ppp |
  }
  
  % FINAL SECTION - Sharp powerful return with complexity
  \repeat unfold 4 {
    % DRIVING SHARP BEATS - complex final support like Faraquet
    bd16\ff sn16\ff bd8\ff sn16\ff r16 hh16\ff bd8\ff sn16\ff r16 hh16\ff sn8\ff bd16\ff |
    bd16\ff r16 sn16\ff hh16\ff bd8\ff sn16\ff r16 bd16\ff hh8\ff sn16\ff r16 bd16\ff sn8\ff r16 hh16\ff |
  }
  
  % OUTRO - Sharp clean resolution with final complexity
  \repeat unfold 2 {
    % FINAL SHARP STATEMENT - complex but resolving
    bd8\f sn16\mf r16 bd16\f sn8\mf hh16\mp r16 sn16\mp r16 bd16\pp sn8\pp r16 hh16\ppp |
    sn8\f bd16\mf r16 sn16\f bd8\mf hh16\mp r16 bd16\mp r16 sn16\pp bd8\pp r16 hh16\ppp sn4\pppp |
  }
}

%%%% INSTRUMENT ASSIGNMENTS - RICH SUGARY GUITAR TONES
\score {
  <<
    \new Staff \with {
      instrumentName = "Lead Guitar"
      midiInstrument = "distortion guitar"
      midiMinimumVolume = #0.1
      midiMaximumVolume = #0.9
    } {
      \clef treble
      \key b \minor
      \time 7/4
      \leadGuitarMusic
    }
    
    \new Staff \with {
      instrumentName = "Rhythm Guitar"
      midiInstrument = "overdriven guitar"
      midiMinimumVolume = #0.2
      midiMaximumVolume = #0.95
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
      midiMinimumVolume = #0.5
      midiMaximumVolume = #0.9
    } { 
      \clef bass
      \key b \minor
      \time 7/4
      \bassMusic 
    }

    \new DrumStaff \with {
      instrumentName = "Drums"
      midiInstrument = #"standard kit"
    } { 
      \time 7/4
      \drumMusic 
    }
  >>
  \layout { }
  \midi { }
} 