import wmi
import platform
import time

class Monitor:
    def __init__(self, config):
        self.config = config
        self.platform = platform.system()

    def start(self):
        print("Monitor started...")
        while True:
            self.check_events()
            time.sleep(2)  # Wait for 10 seconds before checking again

    def check_events(self):
        events = []
        if self.platform == "Windows":
            print("[*] Querying Windows Security log via WMI...")
            c = wmi.WMI()

            # Query for failed logins or events related to the honeyuser account
            query = """
            SELECT * FROM Win32_NTLogEvent 
            WHERE Logfile = 'Security' 
            AND (EventCode = '4624' OR EventCode = '4625' OR EventCode = '4740' OR EventCode = '4688') 
            AND Message LIKE '%honeyuser%'
            """
            
            try:
                # Execute WMI query to get relevant log events
                events = c.query(query)

                if not events:
                    print("[*] No relevant events found.")
                else:
                    for event in events:
                        event_message = event.Message
                        # Only log the message if it relates to the 'honeyuser' account
                        if 'honeyuser' in event_message:
                            #print(f"[!] honeyuser triggered {event.EventCode}: {event.Message}")

                            # You can log this into a file or handle it further here
                            with open('logs/honeyuser_event_log.txt', 'a') as log_file:
                                log_file.write(f"{time.ctime()} - {event.Message}\n\n")

            except Exception as e:
                print(f"[!] WMI query failed: {e}")
        else:
            print("[!] Unsupported platform, only Windows is supported for WMI queries.")
