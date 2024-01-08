import random
from music_theory import ChordProgression, Scale
from sound_synthesis import Synthesizer
from audio_processing import save_audio

class JazzGenerator:
    def __init__(self, duration_minutes=3):
        self.duration_minutes = duration_minutes
        self.duration_seconds = duration_minutes * 60
        self.bpm = random.choice(range(110, 151))  # Typical jazz BPM range
        self.scale = Scale('D', 'dorian')  # A common jazz scale
        self.chord_progression = ChordProgression(self.scale, 'jazz')
        self.synth = Synthesizer()

    def generate_jazz_piece(self):
        # Generate a chord progression for the jazz piece
        chords = self.chord_progression.generate_progression(self.duration_seconds, self.bpm)

        # Initialize instruments
        sax = self.synth.initialize_instrument('saxophone')
        bass = self.synth.initialize_instrument('double_bass')

        # Create a soothing jazz track
        sax_track = self.synth.improvise_melody(sax, chords, self.scale, self.duration_seconds, self.bpm)
        bass_track = self.synth.generate_bassline(bass, chords, self.duration_seconds, self.bpm)

        # Mix the tracks together
        jazz_track = self.synth.mix_tracks([sax_track, bass_track])

        # Apply jazz-specific audio effects like reverb
        jazz_track = self.synth.apply_effects(jazz_track, effects=['reverb'])

        return jazz_track

    def save_jazz_piece(self, filename='soothing_jazz_track.wav'):
        jazz_track = self.generate_jazz_piece()
        save_audio(jazz_track, filename)

if __name__ == '__main__':
    generator = JazzGenerator()
    generator.save_jazz_piece()
