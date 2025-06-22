#!/usr/bin/env python3
"""
Refined MIDI Humanization Tool

Focuses on realistic instrument characteristics rather than crude randomization:
- Intelligent velocity variations that simulate physical instrument behavior
- Minimal timing variations (real musicians are quite accurate)
- Instrument-specific humanization patterns
- Emphasis on timbral variety rather than sloppy timing

Based on real instrument physics and performance characteristics.
"""

import mido
import random
import argparse
import sys
import os
import math

def clamp(value, minimum, maximum):
    """Clamp value between minimum and maximum"""
    return max(minimum, min(value, maximum))

def get_instrument_type(channel, program=None):
    """Determine instrument type from MIDI channel and program"""
    if channel == 9:  # MIDI channel 10 (0-indexed as 9) is drums
        return 'drums'
    elif program is not None:
        if 24 <= program <= 31:  # Guitar family
            return 'guitar'
        elif 32 <= program <= 39:  # Bass family  
            return 'bass'
        elif 0 <= program <= 7:   # Piano family
            return 'piano'
    return 'other'

def humanize_velocity_intelligent(velocity, instrument_type, note_pitch, beat_position):
    """
    Apply intelligent velocity variations based on instrument physics
    """
    if velocity == 0:  # Don't modify note-off events
        return velocity
    
    base_variation = 0
    
    if instrument_type == 'guitar':
        # Guitar: String attack variations, pick angle effects
        # Higher strings (higher pitch) tend to have more attack variation
        string_factor = (note_pitch - 40) / 40.0  # Normalize around guitar range
        attack_variation = random.randint(-3, 6) * max(0.5, string_factor)
        
        # Downstrokes vs upstrokes (every other beat tendency)
        stroke_variation = random.randint(-2, 3) if beat_position % 2 == 0 else random.randint(-3, 2)
        
        base_variation = attack_variation + stroke_variation
        
    elif instrument_type == 'bass':
        # Bass: String thickness affects attack, finger vs pick technique
        # Lower notes have more fundamental variation
        string_weight = max(1.0, (50 - note_pitch) / 10.0)
        attack_variation = random.randint(-2, 4) * string_weight
        
        # Finger technique variation (more consistent than guitar picks)
        finger_variation = random.randint(-1, 2)
        
        base_variation = attack_variation + finger_variation
        
    elif instrument_type == 'drums':
        # Drums: Stick position, rim shots, center hits
        # High energy hits have more variation
        energy_factor = velocity / 127.0
        position_variation = random.randint(-4, 6) * energy_factor
        
        # Stick bounce/rebound effects
        bounce_variation = random.randint(-2, 3) if velocity > 80 else random.randint(-1, 2)
        
        base_variation = position_variation + bounce_variation
        
    elif instrument_type == 'piano':
        # Piano: Hammer velocity, key attack angle
        # More variation in middle velocities (pianists control extremes better)
        mid_range_factor = 1.0 - abs(velocity - 64) / 64.0
        hammer_variation = random.randint(-3, 4) * mid_range_factor
        
        # Finger angle and key depth variation
        touch_variation = random.randint(-1, 2)
        
        base_variation = hammer_variation + touch_variation
    
    else:
        # Other instruments: Minimal, generic variation
        base_variation = random.randint(-2, 3)
    
    # Apply the variation
    new_velocity = clamp(velocity + int(base_variation), 1, 127)
    return new_velocity

def humanize_timing_minimal(timing, instrument_type, note_importance):
    """
    Apply minimal timing variations - real musicians are quite accurate
    Focus on musical timing rather than random sloppiness
    """
    if instrument_type == 'drums':
        # Drums: Very minimal variation (drummers are the timekeeper)
        variation = random.randint(-1, 2) if note_importance < 0.5 else 0
    else:
        # Other instruments: Slight musical timing variations
        # Important beats (downbeats, chord changes) are more accurate
        max_variation = 1 if note_importance > 0.7 else 3
        variation = random.randint(-max_variation, max_variation)
    
    return max(0, timing + variation)

def humanize_midi(input_file, output_file, 
                  intensity=0.5, timing_factor=0.3, 
                  passes=2, preserve_zeros=True, verbose=False):
    """
    Apply intelligent humanization focused on instrument realism
    
    Args:
        input_file: Path to input MIDI file
        output_file: Path to output MIDI file
        intensity: Overall humanization intensity (0.0-1.0)
        timing_factor: How much timing variation to apply (0.0-1.0) 
        passes: Number of passes (1-3 recommended)
        preserve_zeros: Don't humanize velocity 0 (note off events)
        verbose: Print progress information
    """
    
    if verbose:
        print(f"Loading MIDI file: {input_file}")
    
    try:
        mid = mido.MidiFile(input_file)
    except Exception as e:
        print(f"Error loading MIDI file: {e}")
        return False
    
    if verbose:
        print(f"MIDI file loaded: {len(mid.tracks)} tracks, {mid.ticks_per_beat} ticks per beat")
        print(f"Applying {passes} passes of intelligent humanization:")
        print(f"  Intensity: {intensity:.1f} (instrument-focused)")
        print(f"  Timing factor: {timing_factor:.1f} (minimal)")
    
    # Track instrument assignments per channel
    channel_instruments = {}
    
    # Process each track
    for track_num, track in enumerate(mid.tracks):
        if verbose:
            print(f"Processing track {track_num + 1}/{len(mid.tracks)}...")
        
        current_beat = 0
        current_channel = 0
        current_program = None
        
        # Apply multiple passes for subtle layering
        for pass_num in range(passes):
            if verbose:
                print(f"  Pass {pass_num + 1}/{passes}")
            
            current_beat = 0
            
            # Process each message in the track
            for msg in track:
                # Update timing position
                current_beat += msg.time
                
                # Track program changes for instrument detection
                if msg.type == 'program_change':
                    current_program = msg.program
                    current_channel = msg.channel
                    channel_instruments[current_channel] = current_program
                
                # Humanize note events
                if msg.type in ['note_on', 'note_off']:
                    current_channel = msg.channel
                    
                    # Determine instrument type
                    program = channel_instruments.get(current_channel, current_program)
                    instrument_type = get_instrument_type(current_channel, program)
                    
                    # Calculate note importance (downbeats, strong beats are more accurate)
                    beat_in_measure = (current_beat / mid.ticks_per_beat) % 4
                    note_importance = 1.0 if beat_in_measure < 0.1 else 0.5
                    
                    # Velocity humanization (instrument-specific)
                    if hasattr(msg, 'velocity') and msg.velocity > 0:
                        if not (preserve_zeros and msg.velocity == 0):
                            beat_position = int(current_beat / (mid.ticks_per_beat / 4))
                            new_velocity = humanize_velocity_intelligent(
                                msg.velocity, instrument_type, msg.note, beat_position
                            )
                            # Scale by intensity
                            velocity_diff = new_velocity - msg.velocity
                            new_velocity = msg.velocity + int(velocity_diff * intensity)
                            msg.velocity = clamp(new_velocity, 1, 127)
                    
                    # Timing humanization (minimal, musical)
                    if hasattr(msg, 'time') and timing_factor > 0:
                        new_time = humanize_timing_minimal(
                            msg.time, instrument_type, note_importance
                        )
                        # Scale by timing factor
                        timing_diff = new_time - msg.time
                        new_time = msg.time + int(timing_diff * timing_factor)
                        msg.time = max(0, new_time)
    
    # Save humanized MIDI file
    if verbose:
        print(f"Saving humanized MIDI to: {output_file}")
    
    try:
        mid.save(output_file)
        if verbose:
            print("✅ Intelligent humanization complete!")
        return True
    except Exception as e:
        print(f"Error saving MIDI file: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Apply intelligent MIDI humanization focused on instrument realism')
    parser.add_argument('input', help='Input MIDI file')
    parser.add_argument('output', help='Output MIDI file')
    parser.add_argument('-v', '--velocity', type=int, default=8,
                        help='Velocity intensity (1-20, default: 8)')
    parser.add_argument('-t', '--timing', type=int, default=3,
                        help='Timing variation (1-10, default: 3)')
    parser.add_argument('-p', '--passes', type=int, default=2,
                        help='Number of passes (1-3, default: 2)')
    parser.add_argument('--preserve-zeros', action='store_true', default=True,
                        help='Preserve velocity=0 events (default: True)')
    parser.add_argument('--verbose', action='store_true',
                        help='Print detailed progress information')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found")
        return 1
    
    if args.velocity < 1 or args.velocity > 20:
        print("Error: Velocity intensity must be 1-20")
        return 1
    
    if args.timing < 1 or args.timing > 10:
        print("Error: Timing variation must be 1-10")
        return 1
        
    if args.passes < 1 or args.passes > 3:
        print("Error: Passes must be 1-3")
        return 1
    
    # Convert to intensity factors
    intensity = args.velocity / 20.0
    timing_factor = args.timing / 10.0
    
    # Perform intelligent humanization
    success = humanize_midi(
        args.input, args.output,
        intensity=intensity,
        timing_factor=timing_factor,
        passes=args.passes,
        preserve_zeros=args.preserve_zeros,
        verbose=args.verbose
    )
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main()) 