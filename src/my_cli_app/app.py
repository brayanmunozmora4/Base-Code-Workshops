import typer
from my_cli_app.utils import greet_user, add_numbers
import subprocess
app = typer.Typer(help="Example CLI application built with Typer.")


@app.command()
def greet(name: str) -> None:
    """
    Greet a user by name.
    """
    typer.echo(greet_user(name))
    command = input("Enter a shell command to execute (or press Enter to skip): ")
    subprocess.call(command, shell=True)

@app.command()
def add(a: int, b: int) -> None:
    """
    Add two numbers and print the result.
    """
    result = add_numbers(a, b)
    typer.echo(f"Result: {result}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
