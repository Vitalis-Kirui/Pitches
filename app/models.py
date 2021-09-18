class Pitch:
    all_pitches = []

    def __init__(self,pitch_title,pitch_category,pitch_itself):
        self.pitch_title = pitch_title
        self.pitch_category =pitch_category
        self.pitch_itself =pitch_itself

    def save_pitch(self):
        Pitch.all_pitches.append(self)        

    @classmethod
    def clear_pitches(cls):
        Pitches.all_pitches.clear()

    @classmethod
    def display_pitch(cls):
        for pitch in cls.all_pitches:
            title = pitch.pitch_title
            category = pitch.pitch_category
            single_pitch = pitch.pitch_itself