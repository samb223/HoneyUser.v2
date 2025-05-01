import os
import platform

class Monitor:
    def __init__(self, config):
        self.config = config
        self.platform = platform.system()
        self.username = config['user']['name']

    def start(self):
        print("[*] Monitor started...")

    def check_events(self):
        events = []

        if self.platform == "Linux":
            print("[*] Checking /var/log/auth.log for suspicious activity...")
            try:
                with open("/var/log/auth.log", "r") as f:
                    lines = f.readlines()
                    for line in lines[-50:]:
                        if self.username in line:
                            #print(f"[!] Suspicious activity for {self.username}: {line.strip()}")
                            events.append({"event": line.strip()})
            except FileNotFoundError:
                print("[!] /var/log/auth.log not found. Is this a non-Debian system?")
            except Exception as e:
                print(f"[!] Error reading auth.log: {e}")

        elif self.platform == "Windows":
            print("[*] Querying Windows Security log via WMI...")
            try:
                import wmi
                c = wmi.WMI()
                query = (
                    "SELECT * FROM Win32_NTLogEvent WHERE Logfile = 'Security' AND "
                    "(EventCode = '4624' OR EventCode = '4625')"
                )
                # 4624 = Successful login, 4625 = Failed login
                for event in c.query(query):
                    if self.username.lower() in str(event.InsertionStrings).lower():
                        evt_str = f"[!] {self.username} triggered EventCode {event.EventCode}: {event.Message}"
                        #print(evt_str)
                        events.append({"event": evt_str})
            except ImportError:
                print("[!] 'wmi' module not found. Install it with: pip install wmi")
            except Exception as e:
                print(f"[!] WMI query failed: {e}")

        return events

