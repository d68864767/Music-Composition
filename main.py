import argparse
from classical_generator import ClassicalGenerator
from jazz_generator import JazzGenerator
from edm_generator import EDMGenerator
from rainstorm_generator import RainstormGenerator
from city_ambiance_generator import CityAmbianceGenerator
from forest_ambiance_generator import ForestAmbianceGenerator
from voice_synthesizer import VoiceSynthesizer
from monologue_generator import MonologueGenerator
from speech_generator import SpeechGenerator
from violin_imitator import ViolinImitator
from piano_imitator import PianoImitator
from guitar_imitator import GuitarImitator
from mashup_creator import MashupCreator
from remix_creator import RemixCreator
from fusion_creator import FusionCreator

def main():
    # Initialize generators
    classical_gen = ClassicalGenerator()
    jazz_gen = JazzGenerator()
    edm_gen = EDMGenerator()
    rainstorm_gen = RainstormGenerator()
    city_ambiance_gen = CityAmbianceGenerator()
    forest_ambiance_gen = ForestAmbianceGenerator()
    voice_synthesizer = VoiceSynthesizer()
    monologue_gen = MonologueGenerator()
    speech_gen = SpeechGenerator()
    violin_imitator = ViolinImitator()
    piano_imitator = PianoImitator()
    guitar_imitator = GuitarImitator()
    mashup_creator = MashupCreator()
    remix_creator = RemixCreator()
    fusion_creator = FusionCreator()

    # Generate compositions
    classical_gen.generate_classical_piece(duration=2)
    jazz_gen.generate_jazz_track(duration=3)
    edm_gen.generate_edm_track(duration=5)

    # Generate sound effects
    rainstorm_gen.generate_rainstorm(duration=10)
    city_ambiance_gen.generate_city_ambiance(duration=15)
    forest_ambiance_gen.generate_forest_ambiance(duration=30)

    # Generate voice
    voice_synthesizer.generate_monologue(duration=1, gender='female', topic='environmental conservation')
    voice_synthesizer.generate_speech(duration=2, gender='male', topic='overcoming challenges')
    voice_synthesizer.generate_narration(duration=3, scene='peaceful beach')

    # Instrumental imitation
    violin_imitator.imitate_violin(duration=2)
    piano_imitator.imitate_piano(duration=4)
    guitar_imitator.imitate_guitar(duration=3)

    # Mashups and remixes
    mashup_creator.create_mashup(duration=5)
    remix_creator.create_remix(duration=4)
    fusion_creator.create_fusion(duration=6)

    print("All audio files have been generated successfully.")

if __name__ == "__main__":
    main()
