import audio_processing
import music_theory
import sound_synthesis
from classical_generator import ClassicalMusicGenerator
from edm_generator import EDMGenerator

class MashupCreator:
    def __init__(self, duration_minutes):
        self.duration_seconds = duration_minutes * 60
        self.classical_generator = ClassicalMusicGenerator()
        self.edm_generator = EDMGenerator()

    def create_mashup(self):
        # Generate classical music piece
        classical_track = self.classical_generator.generate_classical_piece(self.duration_seconds / 2)

        # Generate EDM track
        edm_track = self.edm_generator.generate_edm_track(self.duration_seconds / 2)

        # Mix the two tracks together
        mashup_track = audio_processing.mix_tracks(classical_track, edm_track)

        # Apply additional effects if necessary
        mashup_track_with_effects = audio_processing.apply_effects(mashup_track, effects=['reverb', 'chorus'])

        return mashup_track_with_effects

    def save_mashup(self, filename, mashup_track):
        # Save the mashup track to a file
        audio_processing.save_audio(filename, mashup_track)

if __name__ == "__main__":
    mashup_creator = MashupCreator(duration_minutes=5)
    mashup_track = mashup_creator.create_mashup()
    mashup_creator.save_mashup("classical_electronic_mashup.mp3", mashup_track)
