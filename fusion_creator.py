import random
from audio_processing import mix_tracks, apply_effects
from music_theory import scale_picker, chord_progression_generator
from sound_synthesis import Synthesizer, Sitar, DrumMachine

class FusionCreator:
    def __init__(self, duration, style1, style2):
        self.duration = duration
        self.style1 = style1
        self.style2 = style2
        self.synthesizer = Synthesizer()
        self.sitar = Sitar()
        self.drum_machine = DrumMachine()

    def create_fusion(self):
        # Generate a scale and chord progression for the fusion piece
        scale = scale_picker(self.style1)
        chord_progression = chord_progression_generator(scale, self.duration)

        # Create the traditional Indian music component with sitar
        sitar_track = self.sitar.generate_track(chord_progression, self.duration)

        # Create the modern pop component with synthesizers and drum machine
        pop_melody = self.synthesizer.generate_melody(scale, self.duration)
        pop_beat = self.drum_machine.generate_beat(self.style2, self.duration)

        # Mix the tracks together
        fusion_track = mix_tracks([sitar_track, pop_melody, pop_beat])

        # Apply any additional effects to enhance the fusion
        final_track = apply_effects(fusion_track, effects=['reverb', 'delay'])

        return final_track

    def save_track(self, track, filename):
        # Save the generated track to a file
        with open(filename, 'wb') as file:
            file.write(track.export(format='mp3'))

if __name__ == "__main__":
    fusion_duration = 6 * 60  # 6 minutes in seconds
    fusion_style1 = 'traditional Indian'
    fusion_style2 = 'modern pop'
    fusion_filename = 'fusion_indian_pop.mp3'

    fusion_creator = FusionCreator(fusion_duration, fusion_style1, fusion_style2)
    fusion_track = fusion_creator.create_fusion()
    fusion_creator.save_track(fusion_track, fusion_filename)
