import os
import platform
import wmi
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
            c = wmi.WMI()
            # Check for login attempts or access events from the Windows Event Log
            query = "SELECT * FROM Win32_NTLogEvent WHERE Logfile = 'Security' AND (EventCode = '528' OR EventCode = '529')"
            # EventCode 528 - Successful login, 529 - Failed login attempt
            for event in c.query(query):
                events.append({"event": f"Windows Event: {event.EventCode} - {event.Message}"})
        return events
