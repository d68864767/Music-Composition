import random
import audio_processing
from sound_synthesis import Synthesizer

# Constants for the city ambiance
DURATION = 15 * 60  # 15 minutes in seconds
CAR_SOUNDS = ['car_passing_1.wav', 'car_passing_2.wav', 'car_horn_1.wav']
PEOPLE_SOUNDS = ['people_talking_1.wav', 'people_talking_2.wav']
INTERVAL_CAR = (1, 5)  # Interval in seconds between car sounds
INTERVAL_PEOPLE = (5, 15)  # Interval in seconds between people sounds

def generate_city_ambiance():
    # Create a new synthesizer instance
    synth = Synthesizer()

    # Initialize the city ambiance track
    city_ambiance = audio_processing.create_empty_audio_track(DURATION)

    # Add car sounds at random intervals
    next_car_sound = 0
    while next_car_sound < DURATION:
        car_sound = random.choice(CAR_SOUNDS)
        city_ambiance = audio_processing.mix_audio(city_ambiance, synth.load_sound(car_sound), start_time=next_car_sound)
        next_car_sound += random.uniform(*INTERVAL_CAR)

    # Add people talking sounds at random intervals
    next_people_sound = 0
    while next_people_sound < DURATION:
        people_sound = random.choice(PEOPLE_SOUNDS)
        city_ambiance = audio_processing.mix_audio(city_ambiance, synth.load_sound(people_sound), start_time=next_people_sound)
        next_people_sound += random.uniform(*INTERVAL_PEOPLE)

    # Save the final city ambiance audio
    audio_processing.save_audio(city_ambiance, 'city_ambiance.wav')

if __name__ == '__main__':
    generate_city_ambiance()
