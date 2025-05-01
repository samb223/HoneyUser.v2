# 🐝 HoneyUser - Decoy User Activity Simulator

HoneyUser is a cross-platform security deception tool that creates a **decoy user** and simulates **realistic system activity** to lure and detect unauthorized access or malicious behavior.

> Supports both **Windows** and **Linux**, with OS-specific logging and simulation!

---

##  Features

-  Creates a fake decoy user account (`honeyuser`)
-  Simulates activity:
  -   Command-line history
  -   File/document creation
  -   Fake browser artifacts
-  Logs system-level authentication and session events
-  Alerts via logs when suspicious actions are detected (Windows only)
-  `exit` command to stop the tool gracefully

---

##  Installation

```bash
git clone https://github.com/yourusername/HoneyUser.v2.git
cd HoneyUser.v2
pip install -r requirements.txt
```
##  Usage

1. **Configure the system**  
   Edit `config.yaml` to define the decoy user details and logging preferences.

2. **Run the tool**  
   ```bash
   python honeyuser.py
   ```
3. **Simulated Activity**

The tool will:

-  Create a decoy user (`honeyuser`) if it doesn’t exist
-  Simulate normal user behavior:
  -   Accessing files
  -   Populating bash history
  -   Creating browser artifacts
-  Start monitoring for suspicious events (**Windows only**)

4. **Exit**

To stop the tool, type:
```bash
exit
```

##  Logs

### 🪟 Windows

- **`honeyuser_event_log.txt`**  
  Captures WMI-based detections and simulated alerts.

- **`honeyuser.log`**  
  General logging of all simulated behavior and activity.

---

### 🐧 Linux

- **`honeyuser.log`**  
  Includes simulated activity and parsed `/var/log/auth.log` entries for the decoy user.

- **`/var/log/auth.log`** *(system file)*  
  Real system events are parsed here if accessible.

>  **Note:** Logs are written in **JSON** or **plain text** based on the `config.yaml` setting.

---

##  Features

-  **Cross-platform decoy user deployment** (Windows + Linux)
-  **Realistic simulated activity**, including:
  -   Shell usage
  -   Document access
  -   Cron job activity
  -   Browser history
-  **Pluggable detection engine** (WMI-based for Windows)
-  **Flexible logging system** with optional email alerts
-  **Modular code structure**:
  -   `/activity`
  -   `/monitor`
  -   `/alert`
  -   `/osplatform`



