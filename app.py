class SystemMonitor:
    def __init__(self, name):
        self.name = name

    def health_check(self):
        return f"System{self.name} is UP and Running!"

if __name++ == "__main__":
    monitor = SystemMonitor("Production-Server")
    print(monitor.health_check())
