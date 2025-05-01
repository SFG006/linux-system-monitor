# Linux System Monitor

A real-time system monitoring tool built with Python.

## Features:
- Monitors CPU usage, memory usage, disk usage, and network statistics.
- Logs system stats to CSV and text files.
- Displays data in a visually appealing format using the rich library.
- Supports progress bars and spinner animations.

## Requirements:
- Python 3.6+
- psutil
- rich

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/linux-system-monitor.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python display.py
   ```

## Usage:
- `display.py`: Main script to display real-time system stats.
- `logger.py`: Logs stats to CSV and text files.
- `monitor.py`: Contains system statistics gathering logic.
