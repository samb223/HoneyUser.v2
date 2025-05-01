import platform
if platform.system() == "Windows":
    import wmi
import time
from alert.logger import Logger

class Monitor:
    def __init__(self, config):
        self.config = config
        self.platform = platform.system()
        self.logger = Logger(config)

    def start(self):
        print("[*] Monitor started...")
        while True:
            self.check_events()
            time.sleep(10)  # Poll every 10 seconds

    def check_events(self):
        events = []
        if self.platform == "Windows":
            print("[*] Querying Windows Security log via WMI...")
            c = wmi.WMI()

            query = """
            SELECT * FROM Win32_NTLogEvent 
            WHERE Logfile = 'Security' 
            AND (EventCode = '4624' OR EventCode = '4625' OR EventCode = '4740' OR EventCode = '4688') 
            AND Message LIKE '%honeyuser%'
            """
        
            try:
                wmi_events = c.query(query)

                if not wmi_events:
                    print("[*] No relevant events found.")
                else:
                    for event in wmi_events:
                        if 'honeyuser' in event.Message:
                            msg = event.Message
                            events.append({
                                "event_code": event.EventCode,
                                "message": msg,
                                "source": "wmi"
                            })
                            with open('logs/honeyuser_event_log.txt', 'a') as log_file:
                                log_file.write(f"{time.ctime()} - {msg}\n\n")

            except Exception as e:
                print(f"[!] WMI query failed: {e}")
        else:
            print("[!] Unsupported platform, only Windows is supported for WMI queries.")

        return events  

