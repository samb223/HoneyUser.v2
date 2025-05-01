import os
import platform
import subprocess

class Monitor:
    def __init__(self, config):
        self.config = config
        self.platform = platform.system()

    def start(self):
        print("Monitor started...")

    def check_events(self):
        events = []
        if self.platform == "Linux":
            with open("/var/log/auth.log", "r") as f:
                lines = f.readlines()
                for line in lines[-50:]:
                    if self.config['user']['name'] in line:
                        events.append({"event": line.strip()})
        elif self.platform == "Windows":
            # Simulated event (real implementation would use pywin32/wmi)
            events.append({"event": "[SIMULATED] Windows EventLog check"})
        return events
