import numpy as np
from sound_synthesis import white_noise, save_wave
from audio_processing import apply_reverb, fade_in, fade_out, mix_tracks, save_audio

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION_RAINSTORM = 600  # Duration of the rainstorm in seconds (10 minutes)
DURATION_THUNDER = 5  # Approximate duration of a thunder sound in seconds
THUNDER_FREQUENCY = 100  # Approximate frequency of thunder in Hz
INTENSITY_REVERB = 0.8  # Intensity of reverb for the rain sound
FADE_IN_DURATION = 5  # Duration of fade-in in seconds
FADE_OUT_DURATION = 5  # Duration of fade-out in seconds
BALANCE = 0.7  # Balance between rain and thunder sounds

def generate_rainstorm():
    # Generate white noise for rain sound
    rain_noise = white_noise(DURATION_RAINSTORM, amplitude=0.5)

    # Apply reverb to rain sound to simulate the sound of rain
    rain_with_reverb = apply_reverb(rain_noise, SAMPLE_RATE, intensity=INTENSITY_REVERB)

    # Generate a few thunder sounds and place them at random intervals
    thunder_sounds = []
    for _ in range(np.random.randint(3, 7)):  # Random number of thunders
        thunder_duration = np.random.uniform(DURATION_THUNDER - 2, DURATION_THUNDER + 3)
        thunder = white_noise(thunder_duration, amplitude=0.8)
        thunder = apply_reverb(thunder, SAMPLE_RATE, intensity=1)
        thunder_sounds.append(thunder)

    # Create a rainstorm track by mixing rain and thunder sounds
    rainstorm_track = rain_with_reverb
    for thunder in thunder_sounds:
        # Randomly choose a start time for the thunder sound
        start_time = np.random.uniform(0, DURATION_RAINSTORM - len(thunder) / SAMPLE_RATE)
        start_sample = int(start_time * SAMPLE_RATE)
        end_sample = start_sample + len(thunder)
        # Mix the thunder sound into the rainstorm track
        rainstorm_track[start_sample:end_sample] = mix_tracks(
            rainstorm_track[start_sample:end_sample], thunder, balance=BALANCE
        )

    # Apply fade-in and fade-out to the rainstorm track
    rainstorm_track = fade_in(rainstorm_track, SAMPLE_RATE, FADE_IN_DURATION)
    rainstorm_track = fade_out(rainstorm_track, SAMPLE_RATE, FADE_OUT_DURATION)

    # Save the rainstorm sound to a file
    save_audio('rainstorm.wav', rainstorm_track, SAMPLE_RATE)

# Call the function to generate the rainstorm sound
generate_rainstorm()
