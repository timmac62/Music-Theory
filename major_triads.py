import click
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.text import Text

from music_theory import interval_names, doremi
from music_theory import scales


custom_theme = Theme(
    {
        "normal_note": "white on black",
        "interval_name": "bold green on black",
        "doremi": "green on black",
        "highlighted_note": "bold green on black"
    }
)

console = Console(width=80, theme=custom_theme)

@click.command()
def major_triads():
    console.clear()
    console.rule(f"[bold blue]:musical_notes: Triads Around the COFs :musical_notes:[/]\n")
    table = Table(title="Major Triads In Every Key", show_lines=False)

    for idx in range(1, 6, 2):
        table.add_column(str(idx), style="normal_note", justify="center")


    for value in scales.values():
        notes = []
        for note in value[:6:2]:
            note_label = Text(str(note), style="normal_note")
            notes.append(note_label)
        table.add_row(*notes)


    console.print(table, justify="center")
    console.rule(f"[bold blue]:guitar: Know Your AXE! :guitar:[/]\n")

if __name__ == "__main__":
    major_triads()
