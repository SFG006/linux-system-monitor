import time
from monitor import SystemMonitor

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

monitor = SystemMonitor()

while True:
    print("\n================ System Monitor ================\n")
    print("🔍 CPU Usage:", monitor.get_cpu_usage(), "%")

    total, used, percent = monitor.get_memory_usage()
    print(f"🧠 Memory Usage: {format_bytes(used)} / {format_bytes(total)} ({percent}%)")

    total, used, percent = monitor.get_disk_usage()
    print(f"💾 Disk Usage: {format_bytes(used)} / {format_bytes(total)} ({percent}%)")

    sent, recv = monitor.get_network_stats()
    print(f"🌐 Network: Sent {format_bytes(sent)}, Received {format_bytes(recv)}")

    time.sleep(2)