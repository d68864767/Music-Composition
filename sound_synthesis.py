import numpy as np
from scipy.signal import chirp, sawtooth, square
from scipy.io.wavfile import write

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz

def sine_wave(frequency, duration, amplitude=1.0, sample_rate=SAMPLE_RATE):
    """Generate a sine wave for a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

def saw_wave(frequency, duration, amplitude=1.0, sample_rate=SAMPLE_RATE):
    """Generate a sawtooth wave for a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * sawtooth(2 * np.pi * frequency * t)
    return wave

def square_wave(frequency, duration, amplitude=1.0, sample_rate=SAMPLE_RATE):
    """Generate a square wave for a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * square(2 * np.pi * frequency * t)
    return wave

def white_noise(duration, amplitude=1.0, sample_rate=SAMPLE_RATE):
    """Generate white noise for a given duration."""
    noise = amplitude * np.random.normal(size=int(sample_rate * duration))
    return noise

def save_wave(file_path, wave, sample_rate=SAMPLE_RATE):
    """Save a wave to a file."""
    # Ensure wave values are in the range [-1, 1]
    normalized_wave = np.int16((wave / np.max(np.abs(wave))) * 32767)
    write(file_path, sample_rate, normalized_wave)

def generate_tone(frequency, duration, wave_type='sine', amplitude=1.0, sample_rate=SAMPLE_RATE):
    """Generate a tone with a specified wave type."""
    if wave_type == 'sine':
        return sine_wave(frequency, duration, amplitude, sample_rate)
    elif wave_type == 'saw':
        return saw_wave(frequency, duration, amplitude, sample_rate)
    elif wave_type == 'square':
        return square_wave(frequency, duration, amplitude, sample_rate)
    else:
        raise ValueError("Invalid wave type specified")

def generate_chord(frequencies, duration, wave_type='sine', amplitude=1.0, sample_rate=SAMPLE_RATE):
    """Generate a chord from a list of frequencies."""
    chord = np.zeros(int(sample_rate * duration))
    for frequency in frequencies:
        chord += generate_tone(frequency, duration, wave_type, amplitude, sample_rate)
    # Normalize the amplitude of the chord
    max_amplitude = np.max(np.abs(chord))
    if max_amplitude > 0:
        chord = chord / max_amplitude * amplitude
    return chord

# Additional sound synthesis functions as needed for the project

