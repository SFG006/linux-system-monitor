import psutil

# CPU Usage
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

# Memory Usage
memory = psutil.virtual_memory()
print("Memory Usage:", memory.percent, "%")

# Disk Usage
disk = psutil.disk_usage('/')
print("Disk Usage:", disk.percent, "%")

# List top 5 processes by memory usage
print("\nTop 5 Memory Consuming Processes:")
for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
    try:
        print(proc.info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
