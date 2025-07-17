import click
from probability_tilt_toolkit.monty import MontyGame

@click.command()
@click.option("--doors", "-n", default=3, show_default=True)
def play(doors):
    game = MontyGame(doors)
    choice = click.prompt(f"Pick a door 0-{doors-1}", type=int)
    revealed = game.first_pick(choice)
    click.echo(f"Goat doors opened: {revealed}")
    win = game.switch() if click.confirm("Switch?") else game.stick()
    click.echo("You WIN!" if win else "You lose.")

if __name__ == "__main__":
    play()
