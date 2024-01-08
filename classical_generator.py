import numpy as np
from music_theory import frequency_of_note, CLASSICAL_PROGRESSIONS, TEMPO, MAJOR_SCALE_INTERVALS, MINOR_SCALE_INTERVALS
from sound_synthesis import sine_wave, save_wave
from audio_processing import apply_reverb, fade_in, fade_out, save_audio
from random import choice, randint

SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 120  # Duration in seconds for a 2-minute piece

def generate_classical_piece():
    # Choose a random key for the piece (C=0, C#=1, ..., B=11)
    key = randint(0, 11)
    # Choose a random octave for the piece (2-5, where 4 is middle C octave)
    octave = randint(2, 5)
    # Choose a random scale type (major or minor)
    scale_type = choice(['major', 'minor'])
    # Choose a random chord progression from classical progressions
    progression = choice(CLASSICAL_PROGRESSIONS)
    # Calculate the tempo in terms of beats per second
    bps = TEMPO / 60

    # Initialize the piece
    piece = np.zeros(int(DURATION * SAMPLE_RATE))

    # Generate the scale based on the key, octave, and scale type
    if scale_type == 'major':
        scale_intervals = MAJOR_SCALE_INTERVALS
    else:
        scale_intervals = MINOR_SCALE_INTERVALS

    current_note = key
    scale = [frequency_of_note(current_note, octave)]
    for interval in scale_intervals:
        current_note += interval
        if current_note >= 12:
            current_note -= 12
            octave += 1
        scale.append(frequency_of_note(current_note, octave))

    # Generate the piece by iterating over the chord progression
    for chord_index in progression:
        # Calculate the root note of the chord
        root_note = scale[chord_index - 1]
        # Generate the notes for the chord
        chord_notes = [root_note, scale[(chord_index + 1) % len(scale)], scale[(chord_index + 3) % len(scale)]]
        # Generate the duration for the chord based on the tempo
        chord_duration = 1 / bps
        # Generate the waves for each note in the chord and sum them
        for note in chord_notes:
            piece += sine_wave(note, chord_duration)

    # Apply effects
    piece = apply_reverb(piece, SAMPLE_RATE)
    piece = fade_in(piece, SAMPLE_RATE, 2)  # 2-second fade-in
    piece = fade_out(piece, SAMPLE_RATE, 2)  # 2-second fade-out

    # Save the piece to a file
    save_audio('classical_piece.wav', piece, SAMPLE_RATE)

# Call the function to generate the classical piece
generate_classical_piece()
