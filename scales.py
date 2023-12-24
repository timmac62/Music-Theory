from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Select, Label, Static
from music_theory import interval_names, doremi, keys, scales

# TODO:
#   - Blues & Triads set background for all notes black
#   - Scales add number sharps & flats
#   - Add 7 9 binding to select chord type:
#   -   7th
#   -   9th


class ScalesApp(App):
    CSS_PATH = "scales.tcss"
    TITLE = "Musical Scales"
    BINDINGS = [
        ("b", "blues", "Blues"),
        ("t", "triad", "Triad"),
        ("q", "quit", "Quit"),
    ]
    scale_key = "C"
    triad = False
    blues = False

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with Vertical(id="key-pane"):
                yield Static(f"Key of: {self.scale_key}", id="key")
                options = [(key, i) for i, key in enumerate(keys)]
                yield Select(options, prompt="Select Key:")
            with Horizontal(id="scale-pane"):
                yield Static("C", id="note1", classes="notes")
                yield Static("D", id="note2", classes="notes")
                yield Static("E", id="note3", classes="notes")
                yield Static("F", id="note4", classes="notes")
                yield Static("G", id="note5", classes="notes")
                yield Static("A", id="note6", classes="notes")
                yield Static("B", id="note7", classes="notes")
                yield Static("C", id="note8", classes="notes")
            with Container(id="theory-pane"):
                for note_number in range(1,9):
                    yield Static(f"{note_number}")
                for interval in interval_names:
                    yield Static(f"{interval}")
                for tone in doremi:
                    yield Static(f"{tone}")
            with Container(id="variants-pane"):
                yield Static("Major Pentatonic")
                yield Static("1 2 3 5 6")
                yield Static("C D E G A", id="majorpentatonic")
                yield Static("Minor Pentatonic")
                yield Static("1 ♭3 4 5 ♭7")
                yield Static("C D E♭ G B♭", id="minorpentatonic")
        yield Footer()

    def on_mount(self):
        key_pane = self.query_one("#key-pane")
        key_pane.border_title = "Key"
        scale_pane = self.query_one("#scale-pane")
        scale_pane.border_title = "Scale"
        theory_pane = self.query_one("#theory-pane")
        theory_pane.border_title = "Theory"
        variant_pane = self.query_one("#variants-pane")
        variant_pane.border_title = "Variants"

    def flatten_note(self, note_to_flatten):
        if "♯" in note_to_flatten:
            flatted_note = note_to_flatten.replace("♯", "")
        else:
            flatted_note = note_to_flatten + "♭"
        return flatted_note

    def update_note_widgets(self):
        self.query_one("#note1").update(scales[self.scale_key][0])
        self.query_one("#note2").update(scales[self.scale_key][1])
        self.query_one("#note3").update(scales[self.scale_key][2])
        self.query_one("#note4").update(scales[self.scale_key][3])
        self.query_one("#note5").update(scales[self.scale_key][4])
        self.query_one("#note6").update(scales[self.scale_key][5])
        self.query_one("#note7").update(scales[self.scale_key][6])
        self.query_one("#note8").update(scales[self.scale_key][7])
        self.query_one("#key").update(f"Key of: {self.scale_key}")
        mp1 = scales[self.scale_key][0]
        mp2 = scales[self.scale_key][1]
        mp3 = scales[self.scale_key][2]
        mp4 = scales[self.scale_key][4]
        mp5 = scales[self.scale_key][5]
        self.query_one("#majorpentatonic").update(f"{mp1} {mp2} {mp3} {mp4} {mp5}")
        mp1 = scales[self.scale_key][0]
        mp2 = self.flatten_note(scales[self.scale_key][2])  # flatten the 3rd
        mp3 = scales[self.scale_key][3]
        mp4 = scales[self.scale_key][4]
        mp5 = self.flatten_note(scales[self.scale_key][6])  # flatten the 7th
        self.query_one("#minorpentatonic").update(f"{mp1} {mp2} {mp3} {mp4} {mp5}")

    def action_triad(self):
        self.triad = not self.triad
        if self.triad:
            self.query_one("#note1").styles.background = "green"
            self.query_one("#note3").styles.background = "green"
            self.query_one("#note5").styles.background = "green"
        else:
            self.query_one("#note1").styles.background = "black"
            self.query_one("#note3").styles.background = "black"
            self.query_one("#note5").styles.background = "black"

    def action_blues(self):
        self.blues = not self.blues
        if self.blues:
            self.query_one("#note1").styles.background = "blue"
            self.query_one("#note4").styles.background = "blue"
            self.query_one("#note5").styles.background = "blue"
        else:
            self.query_one("#note1").styles.background = "black"
            self.query_one("#note4").styles.background = "black"
            self.query_one("#note5").styles.background = "black"

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.scale_key = keys[event.value]
        self.update_note_widgets()



if __name__ == "__main__":
    app = ScalesApp()
    app.run()
