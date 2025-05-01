import os
import json
from datetime import datetime

class Logger:
    def __init__(self, config):
        self.file = config['logging']['file']
        self.format = config['logging']['format']
        self.console_output = config['logging'].get('console_output', False)
        os.makedirs(os.path.dirname(self.file), exist_ok=True)

    def log_event(self, event, level="info"):
        timestamp = datetime.utcnow().isoformat()
        entry = {
            "timestamp": timestamp,
            "level": level,
            **event
        }

        if self.format == 'json':
            with open(self.file, "a", encoding="utf-8") as f:
                json.dump(entry, f)
                f.write("\n\n")
        else:
            with open(self.file, "a", encoding="utf-8") as f:
                event_text = "\n".join([f"{key}: {value}" for key, value in entry.items()])
                f.write(f"{event_text}\n\n")

        if self.console_output:
            print(f"[{timestamp}][{level.upper()}] {entry}")


