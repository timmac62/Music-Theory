from textual.app import App, ComposeResult
from rich.text import Text
from textual.widgets import (
    Static,
    Header,
    Footer
)
from music_theory import (
    interval_names,
    doremi,
    keys,
    scales
)


class ScalesApp(App):
    BINDINGS = [
        ("k", "key_change", "Change Key"),
        ("q", "quit", "Quit"),
    ]
    TITLE = "Scales"
    CSS_PATH = "scales.tcss"
    scale_key = "C"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("C", id="note0", classes="box")
        yield Static("D", id="note1", classes="box")
        yield Static("E", id="note2", classes="box")
        yield Static("F", id="note3", classes="box")
        yield Static("G", id="note4", classes="box")
        yield Static("A", id="note5", classes="box")
        yield Static("B", id="note6", classes="box")
        yield Static("C", id="note7", classes="box")

    def update_note_widgets(self):
        self.query_one("#note0").update(scales[self.scale_key][0])
        self.query_one("#note1").update(scales[self.scale_key][1])
        self.query_one("#note2").update(scales[self.scale_key][2])
        self.query_one("#note3").update(scales[self.scale_key][3])
        self.query_one("#note4").update(scales[self.scale_key][4])
        self.query_one("#note5").update(scales[self.scale_key][5])
        self.query_one("#note6").update(scales[self.scale_key][6])
        self.query_one("#note7").update(scales[self.scale_key][7])


    def action_key_change(self):
        current_key = keys.index(self.scale_key)
        current_key += 1
        if current_key >= len(keys):
            current_key = 0
        self.scale_key = keys[current_key]
        print(f"New key: {current_key} in {self.scale_key}")
        self.update_note_widgets()


if __name__ == "__main__":
    app = ScalesApp()
    app.run()
