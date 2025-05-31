\version "2.24.0"

\header {
  title = "example_song – Chart v3"
  composer = "AI Demo"
}

%%%% Global settings
global = {
  \tempo 4 = 140
  \time 4/4
  \key b \minor
}

%%%% Music materials

guitarMusic = {
  \repeat unfold 3 {
    % Bm chord bar
    <b' fis' d''>4 <b' fis' d''> <b' fis' d''> <b' fis' d''> |
    % Gmaj7
    <g' b' d''>4 <g' b' d''> <g' b' d''> <g' b' d''> |
    % Dmaj7
    <d' fis' a'>4 <d' fis' a'> <d' fis' a'> <d' fis' a'> |
    % Aadd9
    <a' cis'' e''>4 <a' cis'' e''> <a' cis'' e''> <a' cis'' e''> |
  }
}

bassMusic = {
  \clef bass
  \repeat unfold 3 {
    b,1 | g,1 | d,1 | a,1 |
  }
}

drumsPattern = \drummode {
  \repeat unfold 12 {
    bd4 sn bd sn |
  }
}

%%%% Staff definitions
GuitarStaff = \new Staff \with {
  midiInstrument = #"acoustic guitar (nylon)"
  midiChannel    = #0
  instrumentName = "Gtr"
} { \global \guitarMusic }

BassStaff = \new Staff \with {
  midiInstrument = #"electric bass (finger)"
  midiChannel    = #1
  instrumentName = "Bass"
  clef = bass
} { \global \bassMusic }

DrumStaff = \new DrumStaff \with {
  instrumentName = "Drums"
} { \global \drumsPattern }

\score {
  << \GuitarStaff \BassStaff \DrumStaff >>
  \layout { }
  \midi { }
} 