import os
import random
from audio_processing import mix_tracks, add_reverb, export_audio
from sound_synthesis import generate_bird_chirp, generate_wind_noise

# Constants
FOREST_AMBIANCE_DURATION = 30 * 60  # 30 minutes in seconds
OUTPUT_DIRECTORY = 'output'
OUTPUT_FILENAME = 'forest_ambiance.wav'

def create_forest_ambiance(duration):
    # Create a list to hold all our sound samples
    sound_samples = []

    # Generate bird chirping sounds at random intervals
    for _ in range(random.randint(50, 100)):
        start_time = random.uniform(0, duration)
        bird_chirp = generate_bird_chirp(start_time)
        sound_samples.append(bird_chirp)

    # Generate wind noise as a base sound for the ambiance
    wind_noise = generate_wind_noise(duration)
    sound_samples.append(wind_noise)

    # Mix all the sound samples together
    forest_ambiance = mix_tracks(sound_samples, duration)

    # Add some reverb to simulate the forest environment
    forest_ambiance_with_reverb = add_reverb(forest_ambiance)

    return forest_ambiance_with_reverb

def save_forest_ambiance(audio_data, output_dir, filename):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    export_audio(audio_data, os.path.join(output_dir, filename))

def main():
    # Generate the forest ambiance audio data
    forest_ambiance_audio = create_forest_ambiance(FOREST_AMBIANCE_DURATION)

    # Save the forest ambiance audio to a file
    save_forest_ambiance(forest_ambiance_audio, OUTPUT_DIRECTORY, OUTPUT_FILENAME)
    print(f"Forest ambiance has been generated and saved to {os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILENAME)}")

if __name__ == '__main__':
    main()
