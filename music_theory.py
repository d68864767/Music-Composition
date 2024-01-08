import numpy as np

# Define some musical constants
A4_FREQ = 440.0  # Frequency of A4, the A note above middle C (Hz)
TEMPO = 120  # Beats per minute for classical pieces
JAZZ_TEMPO = 140  # Beats per minute for jazz tracks
EDM_TEMPO = 128  # Beats per minute for electronic dance music

# Define scale intervals for major and minor scales
MAJOR_SCALE_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_SCALE_INTERVALS = [2, 1, 2, 2, 1, 2, 2]

# Define chord progressions common in classical, jazz, and pop music
CLASSICAL_PROGRESSIONS = [
    [1, 5, 6, 4],  # I-V-vi-IV
    [2, 5, 1],     # ii-V-I
    [1, 4, 5, 1],  # I-IV-V-I
]

JAZZ_PROGRESSIONS = [
    [2, 5, 1, 6],  # ii-V-I-vi
    [3, 6, 2, 5, 1],  # iii-vi-ii-V-I
    [1, 6, 2, 5],  # I-vi-ii-V
]

EDM_PROGRESSIONS = [
    [1, 5, 6, 4],  # I-V-vi-IV
    [6, 4, 1, 5],  # vi-IV-I-V
    [1, 4, 2, 5],  # I-IV-ii-V
]

def frequency_of_note(note, octave):
    """Calculate the frequency of a note."""
    if note < 0 or note > 11 or octave < 0:
        raise ValueError("Invalid note or octave")
    # Calculate the number of half steps away from A4
    half_steps = (octave - 4) * 12 + note - 9
    # Calculate the frequency
    freq = A4_FREQ * (2 ** (half_steps / 12.0))
    return freq

def generate_scale(root_note, octave, scale_type='major'):
    """Generate a scale from a root note."""
    scale_intervals = MAJOR_SCALE_INTERVALS if scale_type == 'major' else MINOR_SCALE_INTERVALS
    scale = [frequency_of_note(root_note, octave)]
    current_note = root_note
    current_octave = octave
    for interval in scale_intervals:
        current_note += interval
        if current_note >= 12:
            current_note -= 12
            current_octave += 1
        scale.append(frequency_of_note(current_note, current_octave))
    return scale

def generate_chord_progression(scale, progression):
    """Generate a chord progression based on a scale and a progression pattern."""
    chords = []
    for degree in progression:
        if degree - 1 < len(scale):
            root_note = scale[degree - 1]
            # Generate a triad (root, third, fifth)
            third = scale[(degree + 1) % len(scale)]
            fifth = scale[(degree + 3) % len(scale)]
            chords.append((root_note, third, fifth))
    return chords

def bpm_to_seconds_per_beat(bpm):
    """Convert beats per minute to seconds per beat."""
    return 60.0 / bpm

# Additional music theory functions as needed for the project
