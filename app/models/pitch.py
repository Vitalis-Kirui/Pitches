class Pitch:
    all_pitches = []

    def __init__(self,pitch_title,pitch_sentence):
        self.pitch_title = pitch_title
        self.pitch_sentence = pitch_sentence

    def save_pitch(self):
        Pitch.all_pitches.append(self)        

    @classmethod
    def clear_pitches(cls):
        Pitches.all_pitches.clear()