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
@click.option('--solfege', default=True, help='Display Do Re Mi...')
@click.option('--intervals', default=True, help='Display interval names')
def major_scales(solfege, intervals):
    console.clear()
    console.rule(f"[bold blue]:musical_notes: Around the COFs :musical_notes:[/]\n")
    table = Table(title="Major Scales In Every Key", show_lines=False)

    for idx in range(8):
        table.add_column(str(idx), style="normal_note", justify="center")

    if intervals:
        table.add_row(*(interval_names), style="interval_name")
        table.add_section()

    if solfege:
        table.add_row(*(doremi), style="doremi")
        table.add_section()

    for i, (k, v) in enumerate(scales.items()):
        notes = []
        for note in v:
            note_label = Text(str(note), style="normal_note")
            if i == 0:
                note_label.stylize("highlighted_note")
            notes.append(note_label)
        table.add_row(*notes)

    console.print(table, justify="center")
    console.rule(f"[bold blue]:guitar: Know Your AXE! :guitar:[/]\n")

if __name__ == "__main__":
    major_scales()
