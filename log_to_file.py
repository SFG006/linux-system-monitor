import logging
import time
from datetime import datetime
from monitor import SystemMonitor

monitor = SystemMonitor()

# Configure logging
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - CPU: %(message)s%"
)

try:
    while True:
        stats = monitor.get_stats()
        log_line = f"{stats['cpu']} | MEM: {stats['memory']}% | DISK: {stats['disk']}% | Sent: {round(stats['net_sent'] / (1024 * 1024), 2)}MB | Recv: {round(stats['net_recv'] / (1024 * 1024), 2)}MB"
        logging.info(log_line)
        print(f"Logged to system.log at {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(5)

except KeyboardInterrupt:
    print("\nLogging stopped by user.")
