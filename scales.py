from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static
from music_theory import (
    interval_names,
    doremi,
    keys,
    scales
)

# TODO:
#   - Selection
#   - Intervals
#   - Do re mi
#   - top-right spacing


class ScalesApp(App):
    CSS_PATH = "scales.tcss"
    BINDINGS = [
        ("k", "key_change", "Change Key"),
        ("q", "quit", "Quit"),
    ]
    scale_key = "C"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with Vertical(id="left-pane"):
                yield Static("Key of: ")
                yield Static(f"{self.scale_key}", id="key")
                yield Static("Music comes from the heart")
            with Horizontal(id="top-right"):
                yield Static("C", id="note0")
                yield Static("D", id="note1")
                yield Static("E", id="note2")
                yield Static("F", id="note3")
                yield Static("G", id="note4")
                yield Static("A", id="note5")
                yield Static("B", id="note6")
                yield Static("C", id="note7")
            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("panel")
                yield Static("is")
                yield Static("using")
                yield Static("grid layout!", id="bottom-right-final")
        yield Footer()

    def update_note_widgets(self):
        self.query_one("#note0").update(scales[self.scale_key][0])
        self.query_one("#note1").update(scales[self.scale_key][1])
        self.query_one("#note2").update(scales[self.scale_key][2])
        self.query_one("#note3").update(scales[self.scale_key][3])
        self.query_one("#note4").update(scales[self.scale_key][4])
        self.query_one("#note5").update(scales[self.scale_key][5])
        self.query_one("#note6").update(scales[self.scale_key][6])
        self.query_one("#note7").update(scales[self.scale_key][7])
        self.query_one("#key").update(self.scale_key)

    def action_key_change(self):
        # increment the key and rollover at 12
        current_key = (keys.index(self.scale_key) + 1) % 12
        self.scale_key = keys[current_key]
        self.update_note_widgets()


if __name__ == "__main__":
    app = ScalesApp()
    app.run()
