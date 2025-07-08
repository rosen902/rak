from rich.console import Console
import typer

class Logger:
    def __init__(self):
        self.console = Console()

    def info(self, msg : str):
        self.console.print(f"[green]INFO: {msg}[/green]")
    
    def warn(self, msg : str):
        self.console.print(f"[orange]WARN: {msg}[/orange]")
    
    def panic(self, msg : str):
        self.console.print(f"[red]ERR: {msg}[/red]")
        raise typer.Exit(-1)