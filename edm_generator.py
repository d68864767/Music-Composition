import numpy as np
from sound_synthesis import sine_wave, saw_wave, square_wave, white_noise, save_wave
from music_theory import EDM_TEMPO, EDM_PROGRESSIONS, generate_scale, frequency_of_note
from audio_processing import mix_tracks, fade_in, fade_out, save_audio, apply_reverb
import random

SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 300  # Duration in seconds for a 5-minute track

def generate_edm_track():
    # Define the structure of the track
    intro_duration = 45  # 45 seconds
    verse_duration = 60  # 60 seconds
    chorus_duration = 30  # 30 seconds
    bridge_duration = 30  # 30 seconds
    outro_duration = DURATION - (intro_duration + verse_duration + chorus_duration + bridge_duration)

    # Generate a random key and scale for the track
    key = random.choice(range(12))  # Choose a random key from C to B
    scale = generate_scale(key, 3, scale_type='minor')  # EDM often uses minor scales

    # Choose a chord progression
    progression = random.choice(EDM_PROGRESSIONS)
    chord_notes = [scale[i - 1] for i in progression]  # Get the notes for the chosen progression

    # Generate the bassline using a saw wave
    bassline = np.array([])
    for note in chord_notes:
        freq = frequency_of_note(note, 2)  # Octave 2 for a deep bass sound
        bassline = np.append(bassline, saw_wave(freq, 60 / EDM_TEMPO, amplitude=0.5))

    # Generate a lead melody using a square wave
    lead_melody = np.array([])
    for note in chord_notes:
        freq = frequency_of_note(note, 5)  # Octave 5 for the lead melody
        lead_melody = np.append(lead_melody, square_wave(freq, 60 / EDM_TEMPO, amplitude=0.2))

    # Generate a pad sound using a sine wave
    pad_sound = np.array([])
    for note in chord_notes:
        freq = frequency_of_note(note, 4)  # Octave 4 for a pad sound
        pad_sound = np.append(pad_sound, sine_wave(freq, 60 / EDM_TEMPO, amplitude=0.3))

    # Generate white noise for build-ups and transitions
    noise = white_noise(DURATION, amplitude=0.1)

    # Mix the different parts of the track
    track = mix_tracks(bassline, lead_melody, balance=0.6)
    track = mix_tracks(track, pad_sound, balance=0.7)
    track = mix_tracks(track, noise, balance=0.8)

    # Apply effects
    track = apply_reverb(track, SAMPLE_RATE, intensity=0.3)

    # Structure the track with intro, verse, chorus, bridge, and outro
    intro = fade_in(track[:int(SAMPLE_RATE * intro_duration)], SAMPLE_RATE, 5)
    verse = track[int(SAMPLE_RATE * intro_duration):int(SAMPLE_RATE * (intro_duration + verse_duration))]
    chorus = track[int(SAMPLE_RATE * (intro_duration + verse_duration)):int(SAMPLE_RATE * (intro_duration + verse_duration + chorus_duration))]
    bridge = track[int(SAMPLE_RATE * (intro_duration + verse_duration + chorus_duration)):int(SAMPLE_RATE * (intro_duration + verse_duration + chorus_duration + bridge_duration))]
    outro = fade_out(track[int(SAMPLE_RATE * (intro_duration + verse_duration + chorus_duration + bridge_duration)):], SAMPLE_RATE, 5)

    # Concatenate the different parts
    full_track = np.concatenate((intro, verse, chorus, bridge, outro))

    # Save the track to a file
    save_audio('edm_track.wav', full_track, SAMPLE_RATE)

# Call the function to generate the track
generate_edm_track()
