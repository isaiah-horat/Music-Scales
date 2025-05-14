note_positions = ["C", "Db", "D",
                  "Eb", "E", "F",
                  "Gb", "G", "Ab",
                  "A", "Bb", "B"]
music_mode_steps = {"Ionian":     [2, 2, 1, 2, 2, 2, 1],
                    "Dorian":     [2, 1, 2, 2, 2, 1, 2],
                  "Phrygian":     [1, 2, 2, 2, 1, 2, 2],
                    "Lydian":     [2, 2, 2, 1, 2, 2, 1],
                "Mixolydian":     [2, 2, 1, 2, 2, 1, 2],
                   "Aeolian":     [2, 1, 2, 2, 1, 2, 2],
                   "Locrian":     [1, 2, 2, 1, 2, 2, 2]}
music_mode_names = list(music_mode_steps.keys())
class Scale():
    def __init__(self, root_note, mode=music_mode_names[0]):
        self.root_note = root_note
        self.mode_name = mode
        self.name = (f"{root_note} {mode} Scale")
        self.steps = music_mode_steps[mode]
        self.notes = []
    def show_notes(self):
        self.counter = 0
        start = note_positions.index(self.root_note)
        end = note_positions.index(self.root_note)
        new_note_list = list(note_positions[start:] + note_positions[:end])
        self.note_pointer = 0
        for step in self.steps:
            self.notes.append(new_note_list[self.note_pointer])
            self.next_step = self.steps[self.counter]
            self.note_pointer += self.next_step
            self.counter += 1
        return self.notes


answer = input("What scale do you need to know? ")
answer2 = input("What mode? ")
scale = Scale(answer.title(), answer2.title())
print(scale.show_notes())
