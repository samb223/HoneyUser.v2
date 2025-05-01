import os
import json
from datetime import datetime

class Logger:
    def __init__(self, config):
        self.file = config['logging']['file']
        self.format = config['logging']['format']
        os.makedirs(os.path.dirname(self.file), exist_ok=True)

    def log_event(self, event):
        timestamp = datetime.utcnow().isoformat()
        entry = {"timestamp": timestamp, **event}

        if self.format == 'json':
            with open(self.file, "a") as f:
                json.dump(entry, f)
                f.write("\n\n")  # Add newline for readability
        else:
            with open(self.file, "a") as f:
                f.write(f"[{timestamp}] {event}\n\n")
