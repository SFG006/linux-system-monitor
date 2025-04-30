import time
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.spinner import Spinner
from monitor import SystemMonitor

monitor = SystemMonitor()
console = Console()

# Adding a spinner animation
spinner = Spinner("dots", text="Monitoring...", speed=0.1)  # You can change the style and speed here

# Creating a progress bar for CPU usage
with Progress() as progress:
    task = progress.add_task("[cyan]CPU Usage", total=100)

    try:
        while True:
            stats = monitor.get_stats()

            # Update the progress bar for CPU
            progress.update(task, completed=stats["cpu"])

            # Create the table with updated stats
            table = Table(title="Linux System Monitor", show_lines=True)

            table.add_column("Metric", style="cyan", justify="left")
            table.add_column("Value", style="magenta", justify="right")

            table.add_row("CPU Usage (%)", f"{stats['cpu']:.2f}")
            table.add_row("Memory Usage (%)", f"{stats['memory']:.2f}")
            table.add_row("Disk Usage (%)", f"{stats['disk']:.2f}")
            table.add_row("Network Sent (MB)", f"{stats['net_sent'] / (1024 * 1024):.2f}")
            table.add_row("Network Recv (MB)", f"{stats['net_recv'] / (1024 * 1024):.2f}")

            # Clear console and print updated table with progress and animation
            console.clear()
            console.print(table)
            console.print(spinner)  # Displaying the spinner animation

            time.sleep(3)

    except KeyboardInterrupt:
        console.print("\n[bold red]Monitoring stopped by user.[/bold red]")
