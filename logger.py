import csv
import time
from datetime import datetime
from monitor import SystemMonitor  # Make sure this path is correct

monitor = SystemMonitor()
csv_file = "system_log.csv"

# Write header if file is empty/new
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:  # file is empty
        writer.writerow(["Timestamp", "CPU (%)", "Memory (%)", "Disk (%)", "Sent (MB)", "Recv (MB)"])

# Logging loop
try:
    while True:
        stats = monitor.get_stats()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                stats["cpu"],
                stats["memory"],
                stats["disk"],
                round(stats["net_sent"] / (1024 * 1024), 2),
                round(stats["net_recv"] / (1024 * 1024), 2)
            ])

        print(f"Logged at {timestamp}")
        time.sleep(5)  # Log every 5 seconds

except KeyboardInterrupt:
    print("\nLogging stopped by user.")
