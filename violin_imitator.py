import numpy as np
from sound_synthesis import sine_wave, save_wave
from music_theory import frequency_of_note, generate_scale, MINOR_SCALE_INTERVALS
from audio_processing import apply_reverb, fade_in, fade_out, save_audio

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 120  # Duration of the piece in seconds
VIOLIN_AMPLITUDE = 0.5  # Amplitude for the violin sound
REVERB_INTENSITY = 0.3  # Reverb intensity for the violin sound
FADE_IN_DURATION = 2  # Duration of fade-in in seconds
FADE_OUT_DURATION = 2  # Duration of fade-out in seconds

def violin_timbre(frequency, duration, amplitude=VIOLIN_AMPLITUDE, sample_rate=SAMPLE_RATE):
    """Generate a violin-like timbre using a combination of sine waves."""
    fundamental = sine_wave(frequency, duration, amplitude, sample_rate)
    second_harmonic = sine_wave(frequency * 2, duration, amplitude * 0.5, sample_rate)
    third_harmonic = sine_wave(frequency * 3, duration, amplitude * 0.25, sample_rate)
    # Combine harmonics to create a richer sound
    violin_sound = fundamental + second_harmonic + third_harmonic
    return violin_sound

def generate_violin_melody():
    """Generate a melancholic melody for a violin."""
    # Generate a minor scale starting from A3
    scale = generate_scale(9, 3, 'minor')
    melody = np.array([], dtype=np.float32)

    # Create a simple melody using the minor scale
    for note in scale:
        freq = frequency_of_note(note, 4)  # A4 is the reference note
        duration = np.random.uniform(0.2, 0.5)  # Random duration for each note
        note_sound = violin_timbre(freq, duration)
        note_sound = fade_in(note_sound, SAMPLE_RATE, FADE_IN_DURATION)
        note_sound = fade_out(note_sound, SAMPLE_RATE, FADE_OUT_DURATION)
        melody = np.concatenate((melody, note_sound))

    # Ensure the melody fits within the desired duration
    if len(melody) / SAMPLE_RATE > DURATION:
        melody = melody[:int(DURATION * SAMPLE_RATE)]

    # Apply reverb to the melody to simulate the acoustics of a concert hall
    melody = apply_reverb(melody, SAMPLE_RATE, REVERB_INTENSITY)

    return melody

def save_violin_melody(file_path):
    """Save the generated violin melody to a file."""
    melody = generate_violin_melody()
    save_audio(file_path, melody, SAMPLE_RATE)

if __name__ == "__main__":
    # Generate and save the violin melody to a file
    save_violin_melody("violin_melody.wav")
