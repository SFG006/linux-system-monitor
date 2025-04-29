import psutil

class SystemMonitor:
    def __init__(self):
        pass
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return memory.total, memory.used, memory.percent

    def get_disk_usage(self):
        disk = psutil.disk_usage('/')
        return disk.total, disk.used, disk.percent

    def get_network_stats(self):
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent, net_io.bytes_recv

    def get_stats(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net_io = psutil.net_io_counters()
        net_sent = net_io.bytes_sent
        net_recv = net_io.bytes_recv

        return {
            "cpu": cpu,
            "memory": memory,
            "disk": disk,
            "net_sent": net_sent,
            "net_recv": net_recv
        }